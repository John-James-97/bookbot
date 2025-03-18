# BookBot

BookBot is a [Boot.dev](https://www.boot.dev) project!

BookBot is a simple Python script (involving two files) that analyzes the content of a book, counts the number of words and the frequency of each character, then generates a report displaying these statistics in a sorted manner.

## Features
- Reads a book text file from a specified relative path
- Counts the total number of words in the book
- Counts the occurrences of each character in the book (case insensitive)
- Sorts and displays the character count in descending order based on character count
- Generates a report on the different statistics and prints the report to console.

## Requirements
- Python 3.x
- A text file containing the book (e.g., `frankenstein.txt` located in the `books/` directory)

## Usage
1. Clone or download this repository.
2. Ensure that the `books/` directory contains the book text file you want to analyze.
3. Run the script using Python:
   ```sh
   python3 main.py books/{book_name.txt}
   ```

## How It Works
The script follows these steps:
1. **Load the Book:** Opens the specified text file and reads its content.
2. **Count Words:** Splits the text into words and calculates the total count.
3. **Count Characters:** Iterates through each character, converts it to lowercase, and counts occurrences.
4. **Generate Report:** Prints the word count and character frequencies in descending order (only alphabetic characters are considered).

## Code Structure
- `main()`: The main function that orchestrates the program.
- `get_book_text(filePath)`: Reads and returns the book text.
- `get_word_num(contents)`: Splits text into words and returns the count.
- `get_char_count(contents)`: Counts occurrences of each character and returns a dictionary.
- `sort_on_count(dict)`: Sorting helper function.
- `sort_char_nums(charNums)`: Sorts the get_char_count results based on the count of each character and returns a list of dictionaries.
- `print_report(charSorted, wordNums, filePath)`: Generates and prints the report.

## Example Output
```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
...
ë: 2
ô: 1
============= END ===============
```
## Author

John James

## License
This project is open-source and free to use.
