def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    lstr = text.lower()
    ccount = {}
    for c in lstr:
        if c in ccount:
            ccount[c] += 1
        else:
            ccount[c] = 1

    return ccount

def sort_char(c):
    return c["num"]

def make_charlist(charcount):
    dalist = []
    for c in charcount:
        dalist.append({"char": c, "num": charcount[c]})

    dalist.sort(reverse=True, key=sort_char)

    return dalist
