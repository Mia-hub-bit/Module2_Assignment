Pythonic Text Analyzer
Project Overview
This script, text_analyzer.py, is a tool for analyzing text files. It counts words, identifies unique words, and finds the most frequent ones. The code has been refactored to be more modern and efficient using key Python practices.

How to Run
Make sure you have a sample.txt file in the same folder. The script will create one for you if it doesn't exist.

Open your terminal.

Run the script with this command:
python text_analyzer.py

Why the Code is Better
PEP 8: Variables like word_counts now use snake_case, making the code easier to read.

Context Manager: Using with open(...) automatically handles file opening and closing, which is safer and prevents errors.

List Comprehension: A simple, one-line expression now creates the list of long words, replacing a longer for loop.

collections.Counter: Instead of a manual loop to count words, the script uses the highly efficient Counter class.  This is a built-in tool specifically designed for this task, making the code shorter and faster.
