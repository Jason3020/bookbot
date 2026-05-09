def get_book_text():
    with open("books/frankenstein.txt",'r') as file:
        file_contents = file.read()
        print(file_contents)

def main():
    get_book_text()

main()