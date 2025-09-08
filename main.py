#!/usr/bin/python3

from stats import count_words
from stats import count_chars
from stats import make_charlist

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text

def report(book, words, sortchar):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for alph in sortchar:
        if alph["char"].isalpha():
            print(f"{alph['char']}: {alph['num']}")


def main():
    bookname = "books/frankenstein.txt"
    book = get_book_text(bookname)
    count = count_words(book)
    cchar = count_chars(book)
    clist = make_charlist(cchar)
    report(bookname, count, clist)


main()

