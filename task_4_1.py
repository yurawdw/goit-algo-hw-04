'''
Homework for the module 4. Task 1
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

def clean_data(salary_data: list[str]) -> list[float]:
    '''
    The function selects numeric values from a list of strings

    Input:
    * the list of strings (type: list[str])

    Output:
    * the list of numbers (type: list[float])
    '''

    clean_list = []
    for temp in salary_data:
        temp = temp.strip() # Remove leading/trailing whitespace
        if temp:
            match = search(r'-?\d+(\.\d+)?', temp)
            if match:
                try:
                    value = (float(match.group()) if float(match.group()) >= 0 else 0)  # Convert to float
                    clean_list.append(value)
                except ValueError:
                    print(f"Неможливо перетворити значення на число: {match.group()}")

    return clean_list


def total_salary(path: Path) -> tuple[float, float]:
    '''
    The function takes the path to the data file and returns the sum and average of the numeric data

    Input:
    * the path to the data file (type: str)

    Output:
    '''

    if not path:
        # Return 0 if the path is not valid
        return 0, 0
    
    # Load and clean the salary data
    salary_data = clean_data(load_data(path))
    # print(salary_data)
    if not salary_data:
        print("Файл не містить числових даних.")
        return 0, 0

    # Calculate total and average values
    total = sum(salary_data)
    average = total / len(salary_data)

    return (total, average)


def main() -> None:
    '''
    Main function to calculate and display the total and average salary.

    Input:
        * None

    Output:
        * None
    '''

    # Retrieve the file path from command line arguments
    file_path = get_file_name()
    if not file_path:
        # Exit if no valid file path is provided
        return
    
    # Calculate the total and average salary
    total, average = total_salary(file_path)
    print(f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}")


if __name__ == "__main__":
    main()
