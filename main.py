#!/usr/bin/python3

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text

def count_words(text):
    words = text.split()
    return len(words)

def main():
    book = get_book_text("books/frankenstein.txt")
    count = count_words(book)
    print(f"{count} words found in the document")


main()

