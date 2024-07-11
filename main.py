import sys
import os
import pandas as pd

def get_first_file_in_folder(folder_path):
    files = os.listdir(folder_path)
    files = [f for f in files if not f.startswith('.') and os.path.isfile(os.path.join(folder_path, f))]
    return files[0] if files else None


def filter_file(filter_type):
    previous_folder = 'previous'
    new_folder = 'new'
    output_folder = 'output'

    previous_file = get_first_file_in_folder(previous_folder)
    new_file = get_first_file_in_folder(new_folder)

    if previous_file and new_file:
        previous_file_path = os.path.join(previous_folder, previous_file)
        new_file_path = os.path.join(new_folder, new_file)
        previous_df = pd.read_excel(previous_file_path)
        new_df = pd.read_excel(new_file_path)        
        if filter_type == 'patient':
            columns_to_check = ['Patient', 'DOB','Address','Phone']
        else:
            columns_to_check = ['Patient', 'DOB','DOS','Amount Paid']

        mask = ~new_df.set_index(columns_to_check).index.isin(previous_df.set_index(columns_to_check).index)
        cleaned_df = new_df[mask]
        output_file_path = os.path.join(output_folder, f'{new_file}')
        cleaned_df.to_excel(output_file_path, index=False)
        
        print(f"Duplicates removed and cleaned file saved as '{output_file_path}'")
    else:
        print("Files not found in one of the folders.")


def is_patient(command):    
    try:
        convert_type = command[1]
        filter_type = convert_type.lower()
        if "patient" in filter_type:
            print("------------- PATIENT -------------")
            return filter_type
        else:
            print("------------- CPT/ICD -------------")
            return None
    except:        
        return None

if __name__ == "__main__":
    filter_type = is_patient(sys.argv)
    filter_file(filter_type)