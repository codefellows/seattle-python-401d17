from corpus_loader import word_list, name_list
import re

candidates = [
    "j sofa jwm bread wrpqc",
    "a dark and stormy night",
    "n qnex naq fgbezl avtug",
    "j mjat jwm bcxavh wrpqc",
    "call me Ishmael",
    "call me Zebulon",
    "Billy Pilgrim has become unstuck in time",
    "All happy families are alike; each unhappy family is unhappy in its own way.",
    '"Where\'s Papa going with that ax?" said Fern to her mother as they were setting the table for breakfast.',
    "Off the hizzle fo shizzle",
    "Hey.",
]


def count_words(text):

    word_count = 0

    candidate_words = text.split()

    # print(candidate_words)

    for candidate in candidate_words:
        candidate = re.sub(r"[^A-Za-z]+", "", candidate)
        if candidate.lower() in word_list or candidate in name_list:
            word_count += 1
        else:
            pass
            # print("not english word or name", candidate)

    return word_count


for phrase in candidates:
    word_count = count_words(phrase)
    percentage = int(word_count / len(phrase.split()) * 100)
    if percentage > 65:
        print(phrase, percentage)
