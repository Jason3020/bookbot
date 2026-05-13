def count_words():
    with open("books/frankenstein.txt") as file:
        words = file.read().split()
        
    return f"Found {len(words)} total words"

def count_chars():
    with open("books/frankenstein.txt") as file:
        words = file.read().lower()
        chars = {}
        for char in words:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

        
        
    