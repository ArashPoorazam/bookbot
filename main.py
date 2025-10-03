import sys
from stats import count_words, get_book_text, count_characters, sort_char_counts


def main():
	# Require exactly one argument: path to the book
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_path = sys.argv[1]

	book = get_book_text(book_path)
	count = count_words(book)
	char_counts = count_characters(book)

	# get sorted list of {'char': c, 'num': n}
	sorted_chars = sort_char_counts(char_counts)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {count} total words")
	print("--------- Character Count -------")

	# Print only alphabetical characters in order from the sorted list
	for item in sorted_chars:
		ch = item["char"]
		if not ch.isalpha():
			continue
		print(f"{ch}: {item['num']}")

	print("============= END ===============")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())