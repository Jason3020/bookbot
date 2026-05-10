def get_book_text():
    with open("books/frankenstein.txt",'r') as file:
        file_contents = file.read()
        print(file_contents)

def count_words():
    with open("books/frankenstein.txt") as file:
        words = file.read().split()
        
    return f"Found {len(words)} total words"
        
def main():
    print(count_words())

main()