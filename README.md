# CodeAlpha_Exploratory_Data_Analysis
# Exploratory Data Analysis on Hospital General Information

## Project Overview
This project performs Exploratory Data Analysis (EDA) on the Hospital General Information dataset from Kaggle. The objective is to analyze various aspects of hospital data such as ownership, location, ratings, and services to uncover key patterns and insights.

## Dataset Information
- Dataset Source: https://www.kaggle.com/datasets/cms/hospital-general-information  
- File Name: HospInfo.csv  
- The dataset provides information about hospitals in the U.S., including:
  - Hospital name and location  
  - Ownership type  
  - Emergency services availability  
  - Overall hospital rating  
  - Mortality and readmission measures  

## Project Structure
CodeAlpha_Exploratory_Data_Analysis/  
│  
├── main.py  
├── eda_hospital_analysis.py  
├── HospInfo.csv  
└── README.md  

### main.py
- The main driver script that runs the complete EDA process.  
- Loads the dataset, calls analysis functions from eda_hospital_analysis.py, and generates visualizations.  

### eda_hospital_analysis.py
- Contains modular functions for data exploration and visualization.  
- Includes cleaning, summary statistics, and visualizations for ownership types, ratings, and states.  
- X-axis labels for ownership type distribution are adjusted to avoid overlap and improve readability.  

## Key Analyses
- Ownership Type Distribution: Visualizes the number of hospitals per ownership type.  
- Hospital Rating Distribution: Shows the spread of overall hospital ratings.  
- Emergency Services: Compares hospitals with and without emergency services.  
- State-wise Hospital Count: Highlights states with the most hospitals.  

## Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  

## How to Run
1. Clone the repository:  
   git clone https://github.com/BushraSaleem98/CodeAlpha_Exploratory_Data_Analysis.git  
   cd CodeAlpha_Exploratory_Data_Analysis  

2. Install dependencies:  
   pip install pandas numpy matplotlib seaborn  

3. Run the script:  
   python main.py  

## Outputs
The analysis produces:  
- Summary statistics in the console  
- Visualizations for:  
  - Ownership type distribution  
  - Hospital rating distribution  
  - Emergency service availability  
  - State-wise hospital count  

## Repository Links
- Main Script: https://github.com/BushraSaleem98/CodeAlpha_Exploratory_Data_Analysis/blob/main/main.py  
- EDA Functions: https://github.com/BushraSaleem98/CodeAlpha_Exploratory_Data_Analysis/blob/main/eda_hospital_analysis.py  
- Dataset: https://www.kaggle.com/datasets/cms/hospital-general-information  

## Author
Bushra Saleem  
CodeAlpha Internship – Exploratory Data Analysis Project  
Language: Python
