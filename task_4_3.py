from pathlib import Path
from colorama import init, Fore, Back, Style

paren_folder_path = Path('./l1')

path_tree = []
level = 0
decor_str_map = [
    chr(9474), # |              0
    chr(9492), # ⎣              1
    chr(9472), # -              2
    chr(9500), # ⎬              3
    chr(128193), # folder 1     4
    chr(128194), # folder 2     5
    chr(128221), # file          6
    chr(128230) # root          7
]
decor_str = ""

def parse_folder(path: Path, level):
    global path_tree
    decor_prefix = decor_str_map[0] * (level + 1)
    path_iterdir = list(path.iterdir())
    for element in path.iterdir():
        if element == path_iterdir[-1]:
            decor_prefix = decor_str_map[1] + decor_str_map[2]
        if element.is_dir():
            # name = "|" * level
            path_tree.append({"type" : "d", "name" : decor_prefix + " " + decor_str_map[5] + "  " + str(element.name), "level" : level})
            path_tree.append(parse_folder(element, level + 1))
        if element.is_file():
            path_tree.append({"type" : "f", "name" : decor_prefix + " " + decor_str_map[6] + "  "  + str(element.name), "level" : level})
        else:
            continue

def parse_folder(path: Path, level):
    global path_tree
    decor_prefix = decor_str_map[0] * (level + 1)
    path_iterdir = list(path.iterdir())
    for element in path.iterdir():
        if element == path_iterdir[-1]:
            decor_prefix = decor_str_map[1] + decor_str_map[2]
        if element.is_dir():
            # name = "|" * level
            path_tree.append({"type" : "d", "name" : decor_prefix + " " + decor_str_map[5] + "  " + str(element.name), "level" : level})
            path_tree.append(parse_folder(element, level + 1))
        if element.is_file():
            path_tree.append({"type" : "f", "name" : decor_prefix + " " + decor_str_map[6] + "  "  + str(element.name), "level" : level})
        else:
            continue

def print_trees(path_tree):
    for i in range(len(path_tree)):
        n = path_tree[i].get("name")
        print(n)


parse_folder(paren_folder_path, level)
print(path_tree)
print_trees(path_tree)
