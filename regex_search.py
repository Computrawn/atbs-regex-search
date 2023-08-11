#!/usr/bin/env python3
# regex_search.py — An exercise in reading and writin files.
# For more information, see README.md

import logging
from pathlib import Path
import re

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


def regex_search():
    """Open and read all .txt files in text_files directory,
    search for user-defined regex and print results."""
    file_path = Path.cwd() / Path("text_files")
    user_regex = re.compile(input("Please type a regular expression to start search: "))
    match_found = 0

    for text_file in file_path.glob("*.txt"):
        contents = text_file.read_text()
        num_of_files = len(list(file_path.glob("*.txt")))
        match_object = user_regex.findall(contents)
        length = len(match_object)

        for match in range(length):
            print(f"* {match_object[match]}")
            match_found += 1

    print(f"Your search yielded {match_found} matches from {num_of_files} text files.")


def main() -> None:
    regex_search()


if __name__ == "__main__":
    main()
