#!/usr/bin/python3
import argparse
from os import walk
from pathlib import Path
import sys
import os

def create_parser():
    parser = argparse.ArgumentParser(description='Pass path to a markdown file \
            to correct double spaced line endings so the lines format properly.')
    parser.add_argument("file_path", type=Path, help='The path to the \
            markdown file.')
    return parser

def edit_file(path):
    insert_string = "  " # set to "__" for visual testing purposes
    edited_file = ""
    file = open(path, 'r')
    for line in file:
        while line[-1:] == "\n" or line[-1:] == " ":
            # print("removing")
            line = line[:-1]
        line += insert_string
        edited_file += line + "\n"

    # print(edited_file)

    file = open(path, 'w')
    file.writelines(edited_file)
    file.close()

def get_list_of_files(path : str) -> list:
    file_path_list = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        file_path_list.extend(filenames)
    #print(l) for l in file_path_list.split()
    # print(file_path_list)
    assert False, f"TODO: Given a directory, return a list of file paths."
    return file_path_list

if __name__ == "__main__":
    arg_parser = create_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if os.path.exists(parsed_args.file_path):
        # get_list_of_files("./../")
        edit_file(parsed_args.file_path)
        

