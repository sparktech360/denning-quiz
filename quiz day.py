import pandas as pd
import matplotlib.pyplot as plt
import csv

# Task 1: Data Analysis and Visualization
def task1_analysis_and_visualization(file_path):
    df = pd.read_csv(file_path)

    df['dteday'] = pd.to_datetime(df['dteday'])


    summary_stats = df.describe()  
    time_series = df.groupby(df['dteday'].dt.to_period('M')).mean()  

    plt.figure(figsize=(10, 6))

    plt.plot(df['dteday'], df['cnt'], label='Daily Counts')
    plt.title('Time-Series Analysis of Daily Counts')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.legend()
    plt.show()

    df['cnt'].hist(bins=20, edgecolor='black')
    plt.title('Distribution of Daily Counts')
    plt.xlabel('Count')
    plt.ylabel('Frequency')
    plt.show()

    return summary_stats, time_series

# Task 2: Data Cleaning and Transformation
def task2_cleaning_and_transformation(file_path):
    df = pd.read_csv(file_path)

    df['Nationality'] = df['Nationality'].str.replace(r'[()]', '', regex=True)
    df['Gender'] = df['Gender'].str.replace(r'[()]', '', regex=True)

    df['BeginData'] = df['BeginData'].str.replace('-', '', regex=True).astype('Int64', errors='ignore')
    df['EndDate'] = df['EndDate'].str.replace('-', '', regex=True).astype('Int64', errors='ignore')
    
    df['actual_age'] = df['EndDate'] - df['BeginData']
    df['actual_age'] = df['actual_age'].fillna('-')

    df['Date'] = df['Date'].str.replace(r'[^\d-]', '', regex=True)

    return df

# Task 3: Data Handling with CSV
def task3_csv_handling(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if any("Total" in str(value) for value in row.values()):
                continue

            if "Beginning Balance" in row['Date']:
                continue

            writer.writerow(row)

if __name__ == "__main__":
    # Task 1
    summary, trends = task1_analysis_and_visualization("Data Quest Task1.csv")
    print(summary)
    # Task 2
    # cleaned_data = task2_cleaning_and_transformation("Data Quest Task2.csv")
    # cleaned_data.to_csv("task2_cleaned_dataset.csv", index=False)
    # print("Task 2: Data Cleaning and Transformation")
    # print(cleaned_data.head())
    # Task 3
    task3_csv_handling("Data Quest Task3.csv", "task3_cleaned_transactions.csv")
    print("Task 3: Data Handling with CSV completed and saved to task3_cleaned_transactions.csv")








