def count_words():
    with open("books/frankenstein.txt") as file:
        words = file.read().split()
        
    return f"Found {len(words)} total words"