#!/usr/bin/env python3
import sys
import typing

def ft_ancient_text():
    if len(sys.argv) != 2:
        sys.stderr.write("number of arguments are invalid\n")
        return None
    try:
        file = open(sys.argv[1], "r")
    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
        return None
    in_file = file.read()
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file `{file.name}` ")
    print("---")
    fragment = 0
    print(f"[FRAGMENT {fragment}]: ", end="")
    for char in in_file:
        if char == '\n':
            fragment += 1
            print(f"\n[FRAGMENT {fragment}]: ", end="")
        if char != '\n':
            print(char, end="")
    file.close()
    print("\n---")
    print(f"File '{file.name}' closed.")
    return in_file

def ft_archive_creation():
    file_content = ft_ancient_text()
    if file_content is None:
        return
    print("New file name: ", end="", flush=True)
    file_name = sys.stdin.readline().rstrip("\n")

    if file_name == "":
        sys.stderr.write("not saving any data")
        return
    try:
        file = open(file_name, "x")
    except FileExistsError:
        try:
            file = open(file_name, "w")
        except PermissionError as e:
                sys.stderr.write(f"[STDERR] Error opening file '{file_name}': {e}\n")
                return
    
    i = 0
    while i < len(file_content):
        if file_content[i] == '\n':
            file.write("#")
        file.write(file_content[i])
        i += 1
    file.write("#")
    print(f"Saving data to {file.name}")

if __name__ == "__main__":
	ft_archive_creation()