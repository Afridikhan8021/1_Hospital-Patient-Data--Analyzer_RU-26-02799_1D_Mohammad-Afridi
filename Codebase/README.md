# Hospital Patient Data Analyzer

A Python console application to clean and analyze dummy hospital patient data from a CSV file.

## Technologies
- Python 3
- Pandas
- Matplotlib

## Features
- Remove duplicate records and handle missing values.
- Count patients department-wise.
- Calculate individual and average length of stay.
- Analyze age groups and generate a bar chart.

## Installation
```bash
python -m pip install pandas matplotlib
```

## Run
```bash
python hospital_analyzer.py
```

Enter the CSV filename when prompted, then choose a menu option.

## CSV Columns
```text
Patient_ID,Age,Gender,Department,Admit_Date,Discharge_Date
```

## Test Cases
1. Normal input: department-wise patient count.
2. Same-day discharge: 0-day stay.
3. Duplicate and missing age: remove duplicate and fill median age.
4. Summary: average stay, age groups, and chart.

## Author
Mohammad Afridi
