'''
Homework for the module 4. Task 2
'''
import sys
from re import search
from pathlib import Path

# variables
warn_msg = f"Файл не знайдено або шлях некоректний (Наприклад: {Path(sys.argv[0]).name} /path-to-file/example.txt)"

error_msg = f"Помилка при завантаженні файлу!"

# function definitions
def get_file_name() -> Path:
    '''
    The function returns the path to the data file from the command line

    Input:
    * None

    Output:
    * the path to the data file (type: string)
    '''

    try:
        # Get the file name from command line arguments
        file_name = Path(sys.argv[1])
    except IndexError:
        # Inform the user if the file name is missing
        print(warn_msg)
        return None

    # Check if the file exists and is a file
    if file_name.exists() and file_name.is_file():
        return file_name
    else:
        # Inform the user if the provided path is invalid
        print(warn_msg)
    return None


def load_data(path: Path) -> list[str]:
    '''
    The function loads data from a file

    Input:
    * the path to the data file (type: string)

    Output:
    * the list of strings (type: list[str])
    '''

    try:
        # Open the file and read all lines
        with path.open("r", encoding='utf-8') as fh:
            return fh.readlines()
    except Exception as e:
        print(error_msg, e, sep="  ")
        return []

def clean_data(animal_data: str) -> dict:
    '''
    The function receives string values, splits them, and creates a dictionary
    
    Input:
    * the string (type: str)

    Output:
    * the dictionary (type: dict["ID" : str, "Name" : str, "Age" : int])
    '''

    result = animal_data.split(',')
    
    if not animal_data or result == animal_data or len(result) < 3:
        print("Data not found. Exit...")
        return None

    animal_dict = {"ID" : result[0].strip(), \
                   "Name" : result[1].strip(), \
                   "Age" : int(result[2].strip())}

    return animal_dict

def get_cats_info(path: str) -> list[dict]:
    '''
    
    '''

    if not path:
        # Return 0 if the path is not valid
        return None

    info_list = []
    info_list.append(clean_data(el) for el in load_data(path))

    return info_list

def main():
    '''
    '''
    
    # Retrieve the file path from command line arguments
    file_path = get_file_name()
    if not file_path:
        print("Data file not found. Exit...")
        # Exit if no valid file path is provided
        return

    
    cats_info = get_cats_info("path/to/cats_file.txt")
    print(cats_info)pass

if __name__ == "__main__":
    main()
