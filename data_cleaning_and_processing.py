import pandas as pd 

print("***Loading and exploring the dataset...")
# Load dataset
medical_data = pd.read_csv('KaggleV2-May-2016.csv')
# Display first few rows
print(medical_data.head())  
# Display summary information
print(medical_data.info())          
# Display statistical summary
print(medical_data.describe())

print("\n\n***Data Cleaning and Processing...")
# Data Cleaning and Processing Steps    
#1.Identify and handle missing values using .isnull() in Python or filters in Excel. 
missing_values = medical_data.isnull().sum()
print("Missing values in each column:\n", missing_values)
#print((medical_data=='').sum())
#print((medical_data=='None').sum())
#print((medical_data=='NA').sum())
#based on the output, there are no missing or null values in the dataset.


#2.Remove duplicate rows using .drop_duplicates() or Excel’s “Remove Duplicates”. 
print("Data shape before removing duplicates:", medical_data.shape)
medical_data = medical_data.drop_duplicates()
print("Data shape after removing duplicates:", medical_data.shape)
# Check for duplicate PatientId and No-show entries
print(medical_data[['PatientId','No-show']].duplicated().sum())
duplicated_medical_data = medical_data.drop_duplicates(subset=['PatientId','No-show'], keep=False)
print("Data shape after removing duplicates in pateindId and No-show entries:", medical_data.shape)
print(medical_data[['PatientId','No-show']].duplicated().sum())


#3.Standardize text values like gender, country names, etc.
print("Unique Gender values ",medical_data['Gender'].unique()) 


#4.Convert date formats to a consistent type (e.g., dd-mm-yyyy). 
# we have two data columns: AppointmentDay and ScheduledDay
print("\nData types before conversion:\n", medical_data[['AppointmentDay', 'ScheduledDay']].head())
medical_data['AppointmentDay'] = pd.to_datetime(medical_data['AppointmentDay'])
medical_data['ScheduledDay'] = pd.to_datetime(medical_data['ScheduledDay'])
print("\nData types after conversion:\n", medical_data[['AppointmentDay', 'ScheduledDay']].head())      


#5.Rename column headers to be clean and uniform (e.g., lowercase, no spaces). 
medical_data.columns = medical_data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')
print(medical_data.columns)

#6.Check and fix data types (e.g., age should be int, date as datetime).
print(medical_data.dtypes)
medical_data['patientid'] = medical_data['patientid'].astype('int64')
medical_data['age'] = medical_data['age'].astype(int)

