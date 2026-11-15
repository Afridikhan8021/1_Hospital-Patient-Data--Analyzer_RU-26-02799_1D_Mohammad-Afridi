import pandas as pd
import matplotlib.pyplot as plt
import os




# Load CSV
def load_data(filepath):
    if not os.path.exists(filepath):
        print(f"[ERROR] File not found: {filepath}")
        return None

    df = pd.read_csv(filepath)
    print(f"\n Data loaded successfully! Total rows: {len(df)}")
    return df



# Clean Data
def clean_data(df):
    original_len = len(df)

    # remove duplicate data
    df = df.drop_duplicates()
    removed = original_len - len(df)
    if removed > 0:
        print(f"Duplicates removed: {removed}")

    # fill missing age
    if df['Age'].isnull().any():
        median_age = df['Age'].median()
        df['Age'] = df['Age'].fillna(median_age)
        print(f"Missing Age filled with median: {int(median_age)}")

    # datetime
    df['Admit_Date']     = pd.to_datetime(df['Admit_Date'],     errors='coerce')
    df['Discharge_Date'] = pd.to_datetime(df['Discharge_Date'], errors='coerce')

    # Length of Stay (days) 
    df['Length_of_Stay'] = (df['Discharge_Date'] - df['Admit_Date']).dt.days

    print(f"Cleaned data has {len(df)} rows.\n")
    return df



# Analysis Functions

def dept_patient_count(df):
    print("\nDepartment-wise Patient Count:")
    print("─" * 35)
    counts = df['Department'].value_counts()
    for dept, cnt in counts.items():
        print(f"  {dept}: {cnt}")
    print(f"\n  Total patients: {len(df)}")



def avg_length_of_stay(df):
    print("\nAverage Length of Stay:")
    print("─" * 35)
    avg = df['Length_of_Stay'].mean()
    print(f"  Average stay: {avg:.2f} days")

    print("\n  Per-patient breakdown:")
    for _, row in df.iterrows():
        print(f"    {row['Patient_ID']}: {row['Length_of_Stay']} days")



def stay_and_age_groups(df):
    print("\nStay Duration & Age Group Analysis:")
    print("─" * 35)

    avg = df['Length_of_Stay'].mean()
    print(f"  Average stay: {avg:.2f} days")

    # define Age groups 
    bins   = [0, 40, 60, float('inf')]
    labels = ['0-40', '41-60', '61+']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)

    age_counts = df['Age_Group'].value_counts().reindex(labels, fill_value=0)
    print("\n  Age Group Distribution:")
    for grp, cnt in age_counts.items():
        print(f"    {grp}: {cnt}")

    # Bar Chart
    plt.figure(figsize=(7, 5))
    bars = plt.bar(age_counts.index, age_counts.values, edgecolor='black', width=0.5)

    # Value labels on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.05, str(int(yval)), ha='center', va='bottom', fontsize=12)

    plt.title('Patient Age Group Distribution', fontsize=14, fontweight='bold')
    plt.xlabel('Age Group',  fontsize=12)
    plt.ylabel('Number of Patients', fontsize=12)
    plt.ylim(0, age_counts.max() + 2)
    plt.tight_layout()
    plt.savefig('age_group_chart.png')   
    print("\nBar chart displayed! (also saved as age_group_chart.png)")
    plt.show()



# Menu
def show_menu():
    print("\n" + "=" * 40)
    print("HOSPITAL PATIENT DATA ANALYZER")
    print("=" * 40)
    print("  1. Department-wise patient count")
    print("  2. Average length of stay")
    print("  3. Stay duration & age group analysis")
    print("  0. Exit")
    print("=" * 40)
    choice = input("  Choose option (0/1/2/3): ").strip()
    return choice



#  MAIN
def main():
    filepath = input("Enter CSV filename (e.g. patients.csv): ").strip()

    df = load_data(filepath)
    if df is None:
        return

    df = clean_data(df)

    while True:
        choice = show_menu()

        if choice == '1':
            dept_patient_count(df)
        elif choice == '2':
            avg_length_of_stay(df)
        elif choice == '3':
            stay_and_age_groups(df)
        elif choice == '0':
            print("\nExiting... Goodbye!\n")
            break
        else:
            print("Invalid option! Please choose 0, 1, 2, or 3.")


if __name__ == "__main__":
    main()
