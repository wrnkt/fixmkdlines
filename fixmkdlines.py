import argparse
from pathlib import Path
import sys
import os

def create_parser():
    parser = argparse.ArgumentParser(description='Pass path to a markdown file \
            to correct double spaced line endings so the lines format properly.')
    parser.add_argument("file_path", type=Path, help='The path to the \
            markdown file.')
    return parser

if __name__ == "__main__":
    arg_parser = create_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if os.path.exists(parsed_args.file_path):
        print("File exists")

