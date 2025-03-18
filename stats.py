def get_word_num(contents):
	wordNums = len(contents.split())
	return wordNums

def get_char_count(contents):
	charCountDict = {}
	for char in contents:
		if char.lower() in charCountDict.keys():
			charCountDict[char.lower()] += 1
		else:
			charCountDict[char.lower()] = 1
	return charCountDict

def sort_on_count(dict):
	return dict["count"]

def sort_char_nums(charNums):
	charSort = [{"char": char, "count": count} 
				for char, count in charNums.items()]
	charSort.sort(reverse=True, key=sort_on_count)
	return charSort
