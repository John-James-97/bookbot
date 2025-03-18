import sys
from stats import *

def get_book_text(filePath):
	with open(filePath) as f:
		contents = f.read()
	return contents

def print_report(charSorted, wordNums, filePath):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filePath}...")
	print("----------- Word Count ----------")
	print(f"Found {wordNums} total words")
	print("--------- Character Count -------")
	for i in charSorted:
		currentChar = i["char"]
		currentCount = i["count"]
		if currentChar.isalpha():
			print(f"{currentChar}: {currentCount}")
	print("============= END ===============")
	

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	contents = get_book_text(sys.argv[1])
	wordNums = get_word_num(contents)
	charNums = get_char_count(contents)
	charSorted = sort_char_nums(charNums)
	print_report(charSorted, wordNums, sys.argv[1])
	
