'''
Homework for the module 4. Task 1
'''
import sys
from re import search
from pathlib import Path


def load_data(path) -> list[str]:
    '''
    Load data from the specified file.

    Input:
        path (str): Path to the data file 

    Output:
        list of str: Data from file
    '''

    try:
        with open(path, "r", encoding='utf-8') as fh:
            return fh.readlines()
    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Error while reading the file: {e}")
    
    return []

def clean_data(salary_data: list[str]) -> list[float]:
    '''
    Parse string data into numeric values
    
    Input:
        list of str: List of data with/without numeric values

    Output:
        list of float: List of numeric values
    '''

    clean_list = []

    for temp in salary_data:
        temp = temp.strip()
        if temp:
            match = search(r'-?\d+(\.\d+)?', temp)
            if match:
                try:
                    value = (float(match.group()) if float(match.group()) >= 0 else 0)
                    clean_list.append(value)
                except ValueError:
                    print(f"Unable to convert a value to a number: {match.group()}")
            else:
                print(f"Incorrect data in line: '{temp}'. Skipped.")
    return clean_list


def total_salary(path) -> tuple[float, float]:
    '''
    Gets the list of employees' salaries from the specified file. Returns the total value of the payroll and the average salary 

    Input:
        path (str): Path to the file.

    Output:
        tuple[float, float]: Tuple with two float values
    '''
    
    salary_data = clean_data(load_data(path))

    if not salary_data:
        print("The file does not contain any numeric data.")
        return 0, 0

    total = sum(salary_data)
    average = total / len(salary_data)

    return (total, average)


def main() -> None:
    """
    Main function to execute the script.
    """
    if len(sys.argv) < 2:
        print(f"Usage: python3 {Path(sys.argv[0]).name} <path-to-file>")
        return

    file_path = sys.argv[1]
    
    # Calculate the total and average salary
    total, average = total_salary(file_path)
    print(f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}")


if __name__ == "__main__":
    main()
