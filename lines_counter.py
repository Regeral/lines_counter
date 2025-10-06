import os
from os.path import isdir

def parse_folder(path):
    files = []
    for file in os.listdir(path):
        if isdir(path + '/' + file):
            files.extend(parse_folder(path + '/' + file))
        else:
            files.append(str(path + '/' + file).replace('\\', '/'))

    return files


folder = input("Full path to the project folder: ")
all_files = parse_folder(folder)

total_lines = 0
for file in all_files:
    total_lines += sum(1 for line in open(file, encoding="utf-8"))

print("Total lines of code:", total_lines)
