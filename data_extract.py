import os
import pandas as pd
import ast

# Function to parse dictionary-like strings into actual dictionaries
def parse_dict_string(s):
    try:
        return ast.literal_eval(s)
    except (SyntaxError, ValueError):
        return {}

def process_xlsx_file(file_path):
    # Load xlsx file into a DataFrame
    df = pd.read_excel(file_path)

    # Initialize an empty DataFrame to store the extracted data
    extracted_data = []

    # Parse the dictionary-like string in columns and extract key-value pairs
    columns_to_parse = ['new_car_detail', 'new_car_overview', 'new_car_specs']
    for index, row in df.iterrows():
        for column in columns_to_parse:
            if column == 'new_car_detail':
                data_dict = parse_dict_string(row[column])
                if data_dict:
                    for key, value in data_dict.items():
                        row[key] = value
            else:
                data_dict = parse_dict_string(row[column])
                if data_dict:
                    if 'top' in data_dict:
                        for item in data_dict['top']:
                            row[item['key']] = item['value']
                    if 'data' in data_dict:
                        for item in data_dict['data']:
                            for sub_item in item['list']:
                                row[sub_item['key']] = sub_item['value']
        
        # Append the row to the list of extracted data
        extracted_data.append(row)

    # Create a new DataFrame from the extracted data
    extracted_df = pd.DataFrame(extracted_data)
    extracted_df.drop(columns=['new_car_detail', 'new_car_overview', 'new_car_specs', 'new_car_feature', 'car_links'], inplace=True)

    return extracted_df


# Get list of xlsx files in the folder
folder_path = r'data\Dataset'
xlsx_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Initialize an empty DataFrame to concat data
final_df = pd.DataFrame()

# Process each xlsx file and inner join the resulting DataFrames
for xlsx_file in xlsx_files:
    file_path = os.path.join(folder_path, xlsx_file)
    df = process_xlsx_file(file_path)
    if final_df.empty:
        final_df = df
    else:
        final_df = pd.concat([final_df, df], axis=0) 



final_df.to_csv('car_dataset.csv', index=False)

'''
 **Here are the key points explaining about the above code:**

1. **Purpose**: The code is designed to process multiple Excel files (.xlsx) stored in a folder and perform specific operations on each file.

2. **Libraries Used**:
   - `os`: Used to interact with the operating system and manage file paths.
   - `pandas (pd)`: Utilized for data manipulation and analysis, especially for handling tabular data with DataFrames.
   - `ast`: Imported to parse dictionary-like strings into actual dictionaries.

3. **Parsing Dictionary-like Strings**:
   - The `parse_dict_string` function is defined to convert dictionary-like strings in specific columns into actual dictionaries.
   - It handles cases where the string might contain invalid syntax or values that can't be evaluated.

4. **Processing Excel Files**:
   - The `process_xlsx_file` function is created to handle the processing of each Excel file.
   - It loads an Excel file into a DataFrame using `pd.read_excel`.
   - It parses specific columns containing dictionary-like strings into actual dictionaries, extracting key-value pairs and adding them as separate columns to the DataFrame.
   - After extracting the relevant information, it drops the original dictionary columns from the DataFrame.

5. **Looping Through Excel Files**:
   - The code iterates through each Excel file in the specified folder using `os.listdir`.
   - It filters out only the files with the ".xlsx" extension.
   - For each Excel file, it calls `process_xlsx_file` to process the file and obtain a DataFrame with the extracted information.
   - It concatenates the resulting DataFrames vertically using `pd.concat` along `axis=0` to combine data from all files.

6. **Final DataFrame**:
   - The final result is stored in the `final_df` DataFrame.
   - If `final_df` is empty, it assigns the DataFrame obtained from the first file. Otherwise, it concatenates subsequent DataFrames to `final_df`.

7. **Output**:
   - The code prints the columns of the final DataFrame to inspect the extracted information.

Overall, this code efficiently processes multiple Excel files, extracts relevant information stored in dictionary-like strings, and consolidates the data into a single DataFrame for further analysis or processing.'''