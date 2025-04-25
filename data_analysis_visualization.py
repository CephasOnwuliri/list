import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Task 1:Loading and exploring the dataset
try:
    #Loading the dataset
    file_path = r'C:\Users\hp\Desktop\iris'  # Using a raw string
    df=pd.read_csv(file_path)
    #First few rows of the dataset
    print("First few rows of the dataset:")
    print(df.head())
    #Structure of the dataset
    print("Structure of the dataset(Information on the dataser):")
    print(df.info())
    #Checking for missing values
    print("Checking for missing values:")
    print(df.isnull().sum())
    #Descriptive statistics of the dataset
    print("Descriptive statistics of the dataset:")
    print(df.describe())
    #Data Cleaning
    print("Checking for duplicates:")
    df.fillna(method='ffill', inplace=True)
except Exception as e:
    print(f"An error occurred while loadin he daase: {e}")

try:
    # Compute basic statistics of numerical columns
    print("\nBasic Statistics:")
    print(df.describe())

    # Perform group analysis
    categorical_column = "target"  # Replace with your categorical column
    numerical_column = "petal length (cm)"  # Replace with your numerical column

    print(f"\nAverage {numerical_column} for each {categorical_column}:")
    grouped = df.groupby(categorical_column)[[numerical_column]].mean()
    print(grouped)

    # Insights:
    print("\nInsights:")
    print(f"The average {numerical_column} differs significantly among {categorical_column}.")
except Exception as e:
    print(f"An error occurred during basic data analysis: {e}")

# Task 3: Data Visualization
try:
    # Set a Seaborn style
    sns.set(style="whitegrid")

    # Line Chart (example: cumulative numerical column)
    df['Cumulative Numerical Column'] = df[numerical_column].cumsum()
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Cumulative Numerical Column'], label="Cumulative Value")
    plt.title(f"Cumulative {numerical_column} Over Index")
    plt.xlabel("Index")
    plt.ylabel(f"Cumulative {numerical_column}")
    plt.legend()
    plt.show()

    # Bar Chart
    plt.figure(figsize=(10, 6))
    sns.barplot(x=grouped.index, y=numerical_column, data=grouped.reset_index())
    plt.title(f"Average {numerical_column} by {categorical_column}")
    plt.xlabel(categorical_column)
    plt.ylabel(f"Average {numerical_column}")
    plt.show()

    # Histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df[numerical_column], bins=15, edgecolor='k', alpha=0.7)
    plt.title(f"Distribution of {numerical_column}")
    plt.xlabel(numerical_column)
    plt.ylabel("Frequency")
    plt.show()

    # Scatter Plot
    numerical_column_2 = "petal width (cm)"  # Replace with another numerical column
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=numerical_column, y=numerical_column_2, hue=categorical_column, palette="viridis", data=df)
    plt.title(f"{numerical_column} vs. {numerical_column_2}")
    plt.xlabel(numerical_column)
    plt.ylabel(numerical_column_2)
    plt.legend(title=categorical_column)
    plt.show()
except Exception as e:
    print(f"An error occurred during data visualization: {e}")

print("\nAnalysis and visualization completed successfully.")

