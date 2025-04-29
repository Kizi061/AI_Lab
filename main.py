import pandas as pd

dataset = pd.read_csv('Walmart.csv')

print("Dataset Loaded")
# print the csv file
print(dataset.describe) 

columns = ["Weekly_Sales","Holiday_Flag","Temperature","Fuel_Price","CPI","Unemployment"]

for column in columns:
    print(f"--------------column: {column}------------")
    print(f"Mean: {dataset[column].mean()}") 
    print(f"Median: {dataset[column].mean()}") 
    print(f"Mode: {dataset[column].mean()}") 
    print(f"Standard Deviation: {dataset[column].std()}") 
