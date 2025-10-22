import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

def clean_data(file_path):
    # Read the raw dataset
    df = pd.read_csv(file_path)

    # Remove unnecessary whitespaces from column names
    df.columns = df.columns.str.strip()

    # Replace misleading text like "same as above" or "N/A" with NaN
    df.replace(
        to_replace=[
            "N/A",
            "na",
            "NaN",
            "Not Available",
            "-",
            "--",
            "unknown"
        ],
        value=np.nan,
        inplace=True
    )

    # Clean hospital names — remove leading "and", extra spaces, special characters
    df["Hospital Name"] = (
        df["Hospital Name"]
        .astype(str)
        .apply(lambda x: re.sub(r"^[Aa]nd\s+", "", x.strip()))
        .apply(lambda x: re.sub(r"[^a-zA-Z0-9\s.,'-]", "", x))
    )

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Drop rows with all NaN values
    df.dropna(how="all", inplace=True)

    # Fill missing numerical values with the median
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    for col in num_cols:
        df[col].fillna(df[col].median(), inplace=True)

    # Fill missing categorical values with mode
    cat_cols = df.select_dtypes(include=["object"]).columns
    for col in cat_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    # Save the cleaned dataset
    df.to_csv("HospInfo_cleaned.csv", index=False)
    print("Data cleaning complete. Cleaned file saved as 'HospInfo_cleaned.csv'.")

    return df

def perform_eda(df):
    print("Starting EDA...\n")

    # 1. Basic Overview
    print("Dataset Shape:", df.shape)
    print("\nColumns:\n", df.columns.tolist())
    print("\nDescriptive Statistics:\n", df.describe(include='all'))

    # 2. Data Types
    print("\nData Types:\n", df.dtypes)

    # 3. Missing Values
    print("\nMissing Values:\n", df.isnull().sum())

    # 4. Unique Value Counts
    print("\nUnique Values per Column:\n", df.nunique())

    # --- Visualization Section ---
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x="Hospital Type", palette="Set2")
    plt.title("Distribution of Hospital Types")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    # Distribution of Hospital Ownership Types (Fixed label overlap)
    plt.figure(figsize=(12, 6))
    ax = sns.countplot(data=df, x="Hospital Ownership", palette="Set3")
    plt.title("Distribution of Hospital Ownership Types")
    plt.xlabel("Hospital Ownership")
    plt.ylabel("Count")

    # Rotate and align labels properly
    plt.xticks(rotation=45, ha='right')  # Rotate 45° and align right
    plt.tight_layout()

    # Adjust text wrapping if needed (long names)
    for label in ax.get_xticklabels():
        label.set_wrap(True)  # Wrap long labels automatically
        label.set_fontsize(10)  # Adjust font size for readability

    plt.show()

    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x="Emergency Services", palette="pastel")
    plt.title("Hospitals with Emergency Services")
    plt.tight_layout()
    plt.show()

    # Top 10 states by number of hospitals
    state_counts = df["State"].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=state_counts.values, y=state_counts.index, palette="Blues_d")
    plt.title("Top 10 States by Number of Hospitals")
    plt.xlabel("Number of Hospitals")
    plt.ylabel("State")
    plt.tight_layout()
    plt.show()

    # 5. Correlation Analysis (if numeric data available)
    numeric_df = df.select_dtypes(include=["int64", "float64"])
    if not numeric_df.empty:
        plt.figure(figsize=(10, 6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show()

    print("\nEDA Completed Successfully.")

if __name__ == "__main__":
    # Step 1: Clean Data
    cleaned_df = clean_data(r"C:\Users\lenovo\PycharmProjects\Exploratory_Data_Analysis\HospInfo.csv")


    # Step 2: Perform EDA
    perform_eda(cleaned_df)
