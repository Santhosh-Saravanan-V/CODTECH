Name:Santhosh Saravanan V
Company : CODTECH IT SOLUTIONS
ID :CT08FGT
Domain : Artificial Intelligence
Duration : January to Febraury 2025

Project Overview
The goal of this project is to preprocess and analyze a student performance dataset to make it ready for further machine learning applications. This involves handling raw data through cleaning, transformation, and scaling. The processed dataset serves as a foundation for deriving actionable insights or applying predictive models.

Key Features of the Project
1.Data Cleaning: Removing noise and ensuring consistency in the dataset.
2.Feature Encoding and Scaling: Transforming categorical and numerical features to suit machine learning requirements.
3.Data Visualization: Identifying correlations between different variables.
4.Dataset Splitting: Preparing the dataset for training and testing machine learning models.


Objectives

Primary Objectives
1.Clean and preprocess the student performance dataset.
2.Handle missing values and duplicates effectively.
3.Encode categorical variables like gender and parental education.
4.Normalize numerical features for uniform scaling.
5.Save the processed dataset for further use.

Secondary Objectives
1.Provide visual insights into data relationships using correlation heatmaps.
2.Split the dataset into features and target for model training purposes.

Steps Performed
1. Loading the Dataset
The dataset student_performance.csv was loaded into a Pandas DataFrame for analysis.
![Screenshot 2024-12-23 071919](https://github.com/user-attachments/assets/e6654a91-f879-4e70-a473-4a67b9d0b484)

3. Exploratory Data Analysis
Displayed dataset information and summary statistics.
Checked for missing values and duplicates.
4. Data Cleaning and Preprocessing
Handled Missing Values: Filled numerical missing values with their column mean.
Removed Duplicates: Identified and removed duplicate rows.
Encoded Categorical Variables: Used LabelEncoder to transform text-based columns (e.g., Gender).
Scaled Numerical Features: Normalized features like Hours_Studied and Attendance (%).
5. Data Visualization
   Steps Performed
  A correlation heatmap was generated to identify the relationships between features like Hours_Studied, Attendance (%), and Test_Score.
6. Dataset Splitting
Separated the dataset into features (X) and target (y).
Split into training (80%) and testing (20%) subsets for model building.
7. Output Generation
The cleaned and processed dataset was saved as processed_data.csv.

Screenshots of Outputs
Dataset Correlation Heatmap
![Figure_1](https://github.com/user-attachments/assets/948dcf10-2438-4653-a885-8bf7ef6b4d1c)
Processed Data Sample
![Screenshot 2024-12-23 072021](https://github.com/user-attachments/assets/38822508-d3e7-4bec-8328-e2c4e0081c05)

Output screenshot
![Screenshot 2024-12-23 071406](https://github.com/user-attachments/assets/835cbb35-f2a0-4c55-8126-0741ee964883)
![Screenshot 2024-12-23 071346](https://github.com/user-attachments/assets/6d5980a1-9a11-42bc-a95b-2b859e016ab3)
![Screenshot 2024-12-23 071316](https://github.com/user-attachments/assets/a5454741-819d-46ce-b7c0-afd076b4f2d8)



Tools and Libraries Used
Programming Language: Python
Libraries:
1.pandas: Data manipulation and preprocessing.
2.numpy: Numerical computations.
3.matplotlib: Data visualization.
4.seaborn: Statistical data visualization.
5.scikit-learn: Machine learning preprocessing utilities.

How to Use This Project
Prerequisites:
Python 3.x installed.
Required libraries installed (pip install pandas numpy matplotlib seaborn scikit-learn).
Steps:
1.Place the student_performance.csv file in the project directory.
2.Run the Python script.
3.The processed dataset will be saved as processed_data.csv.


Conclusion
This project successfully demonstrated data preprocessing techniques, resulting in a clean and structured dataset ready for machine learning applications.


