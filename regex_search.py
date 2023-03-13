#! python3
"""
regex_search.py — An exercise in reading and writing files.
For more info, see project_details.txt.
"""

from pathlib import Path
import re


def regex_search():
    """Open and read all .txt files in text_files directory."""
    file_path = Path.cwd() / Path("text_files")
    user_input = input("Please type a regular expression to start search: ")
    user_regex = re.compile(user_input)
    found = 0

    for text_file in file_path.glob("*.txt"):
        contents = text_file.read_text()

        # Search contents for user-defined regular expression.
        mo = user_regex.findall(contents)

        # Print results to screen.
        for i in range(len(mo)):
            print(mo[i])
            found += 1

    print(f"Your search yielded {found} matches.")


regex_search()
