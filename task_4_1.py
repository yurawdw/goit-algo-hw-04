'''

'''
import sys
from re import search, sub
from pathlib import Path

# from processing import total_salary

def get_file_name() -> Path:
    '''
    Input:

    Output:
    '''

    try:
        file_name = Path("./salary_file.txt")
        # file_name = Path(sys.argv[1])
    except IndexError:
        print(f"1. Необхідно вказати файл з даними (Наприклад: {Path(sys.argv[0]).name} /path-to-file/example.txt)")
    else:
        if file_name.exists() and file_name.is_file():
            return str(file_name)
        else:
            print(f"2. Необхідно вказати файл з даними (Наприклад: {Path(sys.argv[0]).name} /path-to-file/example.txt)")
    return None

def load_data(path: str) -> list[str]:
    '''
    Input:

    Output:
    '''

    with open(path, "r") as fh:
        return fh.readlines()

def clean_data(salary_data: list[str]) -> list[int]:
    '''
    Input:

    Output:
    '''

    clean_list = []
    for temp in salary_data:
        temp = temp.strip()
        if temp:
            temp = search(r'[-+]?\d+\.?\d?', temp.strip())
            if temp is None:
                temp = 0
            else:
                temp = float(temp.group())
        else:
            continue
        clean_list.append(temp)

    return clean_list    

def total_salary(path: str) -> tuple:
    '''
    Input:

    Output:
    '''

    total, average = 0, 0

    if path:
        salary_data = clean_data(load_data(path))
        for temp in salary_data:
            total += temp
        average = total / len(salary_data)
    else:
        return (0, 0)

    return (round(total, 2), round(average, 2))

def main() -> None:

    '''
    Input:

    Output:
    '''

    total, average = total_salary(get_file_name())
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()
