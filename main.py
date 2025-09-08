#!/usr/bin/python3

from stats import count_words

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text

def main():
    book = get_book_text("books/frankenstein.txt")
    count = count_words(book)
    print(f"{count} words found in the document")


main()

