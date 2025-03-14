import sys
from stats import word_count
from stats import character_count
from stats import sort_character_counts

def check_args():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    check_args()
    path = sys.argv[1]
    text = get_book_text(path)
    
    # Print the headers and word count
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    num_words = word_count(text)
    print(f"Found {num_words} total words")
    
    # Get character count and sorted character count list
    char_count = character_count(text)
    sorted_char_list = sort_character_counts(char_count)

     # Print the character counts in the required format
    print("--------- Character Count ---------")
    for item in sorted_char_list:
        print(f"{item['character']}: {item['count']}")

main()