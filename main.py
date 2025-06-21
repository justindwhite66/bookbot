from stats import count_words, count_characters,sort_dict
import sys

#/home/justindwhite/bookbot/books/frankenstein.txt
def main():

    if (len(sys.argv) !=2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
   
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    chars_dict = count_characters(text)
    num_words = count_words(text)
    sorted_list = sort_dict(chars_dict)
    print_results(book_path, num_words, sorted_list)

    
    


def print_results(path, num, list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for i in range(len(list)):
        if list[i]["char"].isalpha():
            print(f"{list[i]["char"]}: {list[i]["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

