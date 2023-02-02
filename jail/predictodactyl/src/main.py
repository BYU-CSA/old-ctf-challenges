import falcon
import json
import random
from collections import Counter


def parse_one_book(book_name):
    with open(book_name) as f:
        book = tuple(sanitize_word(word) for word in " ".join(line.strip()
                                                              for line in f.readlines()).split(" "))
    frequencies = {}
    for i, word in enumerate(book):
        if word not in frequencies:
            frequencies[word] = Counter()
        try:
            frequencies[word].update((book[i + 1],))
        except IndexError:
            pass
    return frequencies


def choose_random_from_collection(collection):
    # return weighted random choice
    return random.choices(list(collection.keys()), weights=list(collection.values()), k=1)


def combine_frequencies(frequencies):
    combined = {}
    for book in frequencies:
        for word in book:  # words are all counters here
            if word not in combined:
                combined[word] = Counter()
            combined[word].update(book[word])
    return combined


def sanitize_word(word):
    return "".join(c for c in word.lower().strip() if c.isalpha())


book_49288 = parse_one_book("books/49288-0.txt")
book_49829 = parse_one_book("books/49829-0.txt")
book_pg30217 = parse_one_book("books/pg30217.txt")
book_pg66333 = parse_one_book("books/pg66333.txt")
flag = parse_one_book("books/flag.txt")
frequencies = combine_frequencies(
    (book_49288, book_49829, book_pg30217, book_pg66333, flag))


class PredictResource:
    def on_post(self, req, resp):
        word = sanitize_word(req.media["word"].split(" ")[-1])
        try:
            next_word = choose_random_from_collection(frequencies[word])
        except KeyError:
            resp.status = falcon.HTTP_400
            resp.text = json.dumps({"error": "Word not found in corpus."})
            return
        resp.text = json.dumps({'next': next_word})


app = falcon.App()
app.add_route('/', PredictResource())
