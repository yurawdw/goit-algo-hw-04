'''
The script displays the structure of the directive using pseudo-graphic elements

'''
import sys
from pathlib import Path
from colorama import init, Fore, Style

# Initializing the colorama
init(autoreset=True)

# Symbols for visualizing the directory tree
decor_map = {
    "root": chr(128230),    # 🌍 root
    "folder": chr(128194),  # 📂 folder
    "file": chr(128221),     # 📝 file
    "pipe": chr(9474),      # |
    "branch": chr(9500),    # ├
    "dash": chr(9472),      # ─
    "corner": chr(9492),    # └
}

def parse_folder(path: Path, level=0, prev_has_sibling=True, show_hidden=False):
    """
    Recursively processes the directory structure and displays them as a tree.
    Can include or exclude hidden files and directories.
    """
    
    # Identifying the root element
    if level == 0:
        print(f"{decor_map['root']} {path.resolve().name}")
    
    # Get the list of subdirectories and files
    items = sorted(
        [item for item in path.iterdir() if show_hidden or not item.name.startswith('.')],
        key=lambda x: (not x.is_dir(), x.name.lower())
    )
    
    # Separate into folders and files
    folders = [item for item in items if item.is_dir()]
    files = [item for item in items if item.is_file()]



    if not files and not folders:
        indent = (decor_map["pipe"] + "  ") * (level - 1 if prev_has_sibling else level - 2)  + ("    " if not prev_has_sibling else "")
    else:
        indent = (decor_map["pipe"] + "  ") * (level if prev_has_sibling else level - 1) + ("  " if not prev_has_sibling else "")
    
    
    total_items = len(folders) + len(files)
    
    for index, item in enumerate(folders + files):
        is_last = index == total_items - 1
        if is_last:
            prefix = decor_map["corner"]
            prev_has_sibling = False
        else: prefix = decor_map["branch"]
        
        if item.is_dir():
            print(f"{indent}{prefix}{decor_map['dash']}{Fore.BLUE}{decor_map['folder']} {item.name}{Style.RESET_ALL}")
            parse_folder(item, level + 1, not is_last, show_hidden)
        else:
            print(f"{indent}{prefix}{decor_map['dash']}{Fore.GREEN}{decor_map['file']} {item.name}{Style.RESET_ALL}")

def main():
    """
    Main function: gets the path to the directory and starts processing.
    """
    if len(sys.argv) < 2:
        print(f"\nUsage: python3 {Path(sys.argv[0]).name} <path-to-dir> | -a \n")
        print(f"option:")
        print(f"\t-a: show all hiden files\n")
        folder_path = Path('..')
    else: 
        folder_path = Path(sys.argv[1])

    show_hidden = "-a" in sys.argv
    
    for arg in sys.argv[1:]:
        if arg != "-a":
            folder_path = Path(arg)
            break
    
    if folder_path is None or not folder_path.is_dir():
        print(f"\nError: '{folder_path}' is not a valid directory.\n")
        return
    
    parse_folder(folder_path, show_hidden=show_hidden)

if __name__ == "__main__":
    main()
