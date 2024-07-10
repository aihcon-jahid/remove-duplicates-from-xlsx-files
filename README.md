# Remove duplicates from XLSX files

## Overview
This Python script processes Excel files located in two specified folders (`previous` and `new`). It identifies and removes duplicates between these files based on specified columns, saving the cleaned data to an `output` folder.

## Functionality
The script performs the following steps:
- **Identify Files**: It retrieves the first Excel file from both the `previous` and `new` folders.
- **Load Data**: Loads data from these Excel files using pandas.
- **Filter Duplicates**: Determines duplicates based on columns specified by the user (either 'patient' or 'CPT/ICD').
- **Save Cleaned Data**: Saves the filtered data into an Excel file in the `output` folder.

## Usage
To run the script, execute it from the command line with the appropriate argument:
- `python script_name.py patient` to filter duplicates based on patient information.
- `python script_name.py cpt/icd` to filter duplicates based on CPT/ICD information.

## Requirements
- Python 3.x
- pandas library

## Example
Suppose you have Excel files with patient records in the `previous` and `new` folders. Running the script with `python script_name.py patient` will filter duplicates based on patient information and save the cleaned data to the `output` folder.

## Note
Ensure that the `previous`, `new`, and `output` folders exist in the same directory as the script for proper file handling.
