#! /usr/bin/python3

import argparse
import re
import glob


def replace_spaces(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    pattern = re.compile(r"\b[a-zA-Z]\s\w+\b")
    matches = pattern.finditer(content)
    for m in matches:
        index = m.start() + 1
        content = content[:index] + "~" + content[index + 1 :]
    with open(file_path, "w") as file:
        file.write(content)


def process_files(files):
    for file in files:
        elements = glob.glob(file)
        for element in elements:
            print(f"Processing file: {element}")
            replace_spaces(element)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Replace spaces with '~' after every single-letter word followed by another word."
    )
    parser.add_argument("files", nargs="+", help="Files to modify")

    args = parser.parse_args()
    process_files(args.files)
