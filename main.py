#!/usr/bin/python3

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    print(text)

def main():
    get_book_text("books/frankenstein.txt")


main()

