# Medical Appointment No-Show — Data Cleaning and Preprocessing

This project performs **data cleaning and preprocessing** on the Kaggle dataset  
📄 [Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments).  
The dataset contains information about patients who scheduled medical appointments in Brazil and indicates whether they showed up or not.

---

## 🧠 Objective

The goal is to:
- Explore the dataset to understand its structure and content.
- Identify and resolve data quality issues (missing values, duplicates, inconsistent formats).
- Standardize and prepare the data for analysis or modeling.

---

## 🧩 Steps Performed

### 1. **Load and Explore the Dataset**
- Load the CSV file using **pandas**.
- Display sample rows, dataset information, and statistical summaries.
- Identify numeric vs categorical columns for later processing.

### 2. **Handle Missing Values**
- Check for nulls using `.isnull().sum()`.
- Validate that no hidden missing values exist (`''`, `'None'`, `'NA'`, etc.).
- Replace any inconsistent missing representations with `pd.NA`.

### 3. **Remove Duplicates**
- Drop exact duplicate rows using `.drop_duplicates()`.
- Inspect and remove logical duplicates for (`PatientId`, `No-show`) combinations to maintain unique entries.

### 4. **Standardize Text Fields**
- Examine text columns like **Gender** for inconsistent casing or spacing.
- Apply `.str.upper()` and `.str.strip()` for clean and uniform formatting.

### 5. **Convert Date Fields**
- Convert `ScheduledDay` and `AppointmentDay` to datetime format using `pd.to_datetime()`.
- Ensure a consistent date format (`YYYY-MM-DD`).
- Optionally check for logical consistency (e.g., scheduled date should not be after appointment date).

### 6. **Rename Columns**
- Clean up column headers to make them Python-friendly:
  - Convert to lowercase.
  - Replace spaces and hyphens with underscores.
  - Example: `ScheduledDay → scheduled_day`

### 7. **Validate and Fix Data Types**
- Ensure numeric columns (like `age`) are integers.
- Convert date columns to datetime objects.
- Standardize the `patientid` field using `astype('Int64')`.

### 8. **Data Quality Summary**
At the end of the process, the script prints:
- Dataset shape after cleaning.
- Number of missing values per column.
- Duplicate counts.
- Data types summary.

---

## 🛠️ Requirements

Install required Python libraries before running the script:
python -m pip install pandas

## How to Run

Download the dataset from Kaggle:
[Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments)

Place the file in the same directory as the script (e.g., KaggleV2-May-2016.csv).

Run the script:

python data_cleaning.py


View the console output for step-by-step cleaning logs.