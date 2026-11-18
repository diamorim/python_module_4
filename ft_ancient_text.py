#!/usr/bin/env python3
import sys
import typing

def ft_ancient_text():
	if len(sys.argv) != 2:
		print("number of arguments are invalid")
		return
	try:
		file = open(sys.argv[1], "r")
	except FileNotFoundError:
		print("File was not found")
		return
	in_file = file.read()
	print("=== Cyber Archives Recovery ===")
	print(f"Accessing file `{file.name}` ")
	print("---")
	print(in_file)
	file.close()
	print("---")
	print(f"File '{file.name}' closed.")
	#if sys.len != 2
		# break and print
	#var file
	#tries 
	#	while i < len(sys.argv)
			#file = sys.argv
	#except not file
		#print file not found
	#
	#in_file = read(file)
	#print(file)
	
	

if __name__ == "__main__":
	ft_ancient_text()