#books
frankenstein = "/home/alemoum/workspace/github.com/Alemoum/bookbot/books/frankenstein.txt"
char_dict = {}

#funtion to get the book content
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

#function to count the num of words
def get_num_words():
    book_text = get_book_text(frankenstein)
    splited_book_text = book_text.split()
    num_words = len(splited_book_text)
    print(f"{num_words} words found in the document")
    
#function to counter characters
def get_count_char():
    book_text = get_book_text(frankenstein)
    book_lower =  book_text.lower()
    for c in book_lower:
        if c in char_dict:
            char_dict[c] +=1
        else:
            char_dict.update({c:1})
    print(char_dict)