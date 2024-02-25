# Car-Price-Evaluation
This project aims to provide an accurate and efficient solution for Evaluating Car prices based on its various features.
**Try This Application here:** https://dinesh-car-evaluation.streamlit.app/
---

# Excel Data Processing and Model Building with Streamlit App

This Python script processes Excel files (.xlsx) located in a specified folder, performs data cleaning, exploratory data analysis (EDA), and builds a machine learning model to predict car prices. Additionally, it includes a Streamlit web application for interactive prediction of car prices.

## Data Processing Overview

1. **Import Necessary Libraries:** The script imports essential libraries including `os` for interacting with the operating system, `pandas` for data manipulation, `ast` for parsing dictionary-like strings, and various libraries for machine learning tasks.

2. **Define Utility Functions:** Utility functions like `parse_dict_string` are defined to handle specific data processing tasks.

3. **Process Excel Files:** The script loads Excel files into DataFrames, extracts relevant data, and combines them into a single DataFrame for analysis.

## Data Cleaning

1. **Identify and Drop Unwanted Columns:** Columns with a large number of unique values are dropped to avoid dimensionality issues.

2. **Encode Categorical Columns:** Categorical columns are marked for one-hot encoding to prepare them for machine learning models.

3. **Handle Specific Columns:** Certain columns are removed due to low correlation or redundancy.

4. **Clean Numerical Columns:** Outliers are removed, and transformations like Box-Cox are applied to make the data more normally distributed.

5. **Save Cleaned Data:** The cleaned DataFrame is saved to a CSV file for further analysis.

## Exploratory Data Analysis (EDA)

1. **Analysis of Categorical Columns:** Visualizations and statistical methods are used to analyze categorical columns like 'Build Type', 'OEM', 'Insurance Validity', etc.

2. **Analysis of Numerical Columns:** Various numerical columns like 'Kilo Meter', 'Model Year', 'Mileage', etc., are analyzed using visualizations and statistical methods.

3. **Handling Outliers:** Outliers are detected and removed from numerical columns to ensure data quality.

4. **Visualizations:** Distribution plots, histograms, and scatter plots are generated to explore relationships between variables.

## Model Building

1. **Import Necessary Libraries:** Libraries for model building including scikit-learn, XGBoost, etc., are imported.

2. **Define Pipelines and Grid Search:** Pipelines for different models are defined, and hyperparameters are tuned using grid search.

3. **Evaluate Models:** Models are evaluated on test data using metrics like Mean Squared Error, Mean Absolute Error, and R^2 Score.

4. **Select Best Model:** The model with the best performance (XGBoost with R^2 Score of 0.88) is selected based on evaluation metrics.

5. **Save Best Model:** The best model and its parameters are saved to a pickle file for future use.

## Streamlit App for Car Price Prediction

1. **Load Trained Model:** The trained machine learning model is loaded from the pickle file.

2. **Streamlit UI:** The Streamlit web application UI is created with title and image components.

3. **Preprocess Input:** User input for various car features is preprocessed using a function.

4. **Perform Prediction:** When the user clicks the prediction button, the preprocessed input is fed into the model for price prediction.

## Usage

1. **Clone the Repository:** Clone the repository to your local machine.
   ```bash
   git clone https://github.com/DINESHPANDIAN-J/Car-Price-Evaluation.git
   ```

2. **Install Dependencies:** Install required dependencies using pip.
   ```bash
   pip install -r requirements.txt
   ```

3. **Place Excel Files:** Place your Excel files (.xlsx) in the specified folder.

4. **Run the Script:** Execute the script `data_extract.py` for data extraction.
   ```bash
   python data_extract.py
   ```

5. **Run the Streamlit App:** Run the Streamlit app for interactive car price prediction.
   ```bash
   streamlit run streamlit_app.py
   ```

## Dependencies

- pandas
- scikit-learn
- XGBoost
- streamlit
- numpy
- scipy

## Example

```bash
streamlit run streamlit_app.py
```

## License

This project is licensed under the [MIT License](LICENSE).

---

