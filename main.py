from stats import count_words, count_chars
def get_book_text():
    with open("books/frankenstein.txt",'r') as file:
        file_contents = file.read()
        print(file_contents)
        
def main():
    print(count_words())
    print(count_chars())
main()