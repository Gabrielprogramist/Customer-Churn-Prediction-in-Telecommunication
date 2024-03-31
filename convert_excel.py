import pandas as pd
# Define the path for the Excel file to be saved
file_path = 'Telco-Customer-Churn.csv'
data = pd.read_csv(file_path)
# Define the path for the new Excel file
excel_file_path = 'Telco-Customer-Churn.xlsx'

# Convert the CSV data to an Excel file
data.to_excel(excel_file_path, index=False)  # Not including the DataFrame index

excel_file_path



