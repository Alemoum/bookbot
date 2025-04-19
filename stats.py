import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
book = sys.argv[1]


char_dict = {}
char_list = []

#funtion to get the book content
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

#function to count the num of words
def get_num_words():
    book_text = get_book_text(book)
    splited_book_text = book_text.split()
    num_words = len(splited_book_text)
    return num_words
    
#function to counter characters
def get_count_char():
    book_text = get_book_text(book)
    book_lower =  book_text.lower()
    for c in book_lower:
        if c in char_dict:
            char_dict[c] +=1
        else:
            char_dict.update({c:1})
    return char_dict



    
def print_report():
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words()} total words")
    print("--------- Character Count -------")
    get_count_char()
    for char in char_dict:
        char_list.append({"char": char, "count": char_dict[char]})
        
    char_list.sort(reverse=True, key=lambda x: x["count"])
    
    for item in char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    

