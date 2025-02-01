import sys
from pathlib import Path

def load_data(path):
    """
    Load data from the specified file.

    Args:
        path (str): Path to the file.

    Returns:
        list: List of lines read from the file.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Error while reading the file: {e}")
    return []

def clean_data(animal_data):
    """
    Parse a single line of animal data into a dictionary.

    Args:
        animal_data (str): A line containing cat information.

    Returns:
        dict or None: A dictionary with cat information, or None if invalid.
    """
    try:
        parts = animal_data.strip().split(",")
        if len(parts) != 3:
            raise ValueError("Invalid data format")

        cat_id, name, age = parts
        return {
            "id": cat_id.strip(),
            "name": name.strip(),
            "age": age.strip(),
        }
    except ValueError as e:
        print(f"Skipping invalid data: {animal_data.strip()} ({e})")
    return None

def get_cats_info(path):
    """
    Get a list of cat information from the specified file.

    Args:
        path (str): Path to the file.

    Returns:
        list: List of dictionaries containing cat information.
    """
    data = load_data(path)
    cats_info = []
    seen_ids = set()

    for line in data:
        cat = clean_data(line)
        if cat and cat["id"] not in seen_ids:
            cats_info.append(cat)
            seen_ids.add(cat["id"])

    return cats_info

def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) < 2:
        print(f"Usage: python3 {Path(sys.argv[0]).name} <path-to-file-with-cat-info>")
        return

    file_path = sys.argv[1]

    cats_info = get_cats_info(file_path)
    if cats_info:
        print("Cat information:")
        for cat in cats_info:
            print(cat)
    else:
        print("No valid cat information found.")

if __name__ == "__main__":
    main()
