import pandas as pd
from eda_hospital_analysis import perform_eda

def main():
    # Load the cleaned dataset
    file_path = r"C:\Users\lenovo\PycharmProjects\Exploratory_Data_Analysis\HospInfo_cleaned.csv"

    df = pd.read_csv(file_path)

    # Display initial info
    print("Initial Dataset Info:")
    print(df.info())
    print("\n")

    # Run Exploratory Data Analysis
    perform_eda(df)

if __name__ == "__main__":
    main()
