from stats import count_words, count_chars, sort_dictionary
import sys

def get_text(file_path):
    with open(file_path) as f:
        return f.read()
        
def print_report( book_path, num_words, sorted_chars ):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

def main():
    print(f"argv: {sys.argv}")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_contents = get_text(book_path)
    num_words = count_words(book_contents)
    char_count_dict = count_chars(book_contents)
    sorted_chars = sort_dictionary(char_count_dict)
    # print(f"Found {num_words} total words")
    # print(char_count_dict)
    # print({k: v for k, v in sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True)})
    # print( sort_dictionary(char_count_dict) )
    print_report(book_path, num_words, sorted_chars)

if __name__ == "__main__":
    main()
