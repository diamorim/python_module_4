#!/usr/bin/env python3
import sys
import typing

def ft_ancient_text():
	if len(sys.argv) != 2:
		print("number of arguments are invalid")
		return
	try:
		file = open(sys.argv[1], "r")
	except (FileNotFoundError, PermissionError):
		print("File was not found")
		return
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
	
	

if __name__ == "__main__":
	ft_ancient_text()