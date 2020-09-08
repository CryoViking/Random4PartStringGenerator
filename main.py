# Author: CryosisOS
# Date Created: 2020-09-08

# IMPORTS
import random

FILES = ["./res/words/adjectives.txt", "./res/words/nouns.txt", "./res/words/adverbs.txt", "./res/words/verbs.txt"]
ADJECTIVES = 0; NOUNS = 1; ADVERBS = 2; VERBS = 3

def readFile(filepath):
    with open(filepath, "r") as file:
        contents = file.read().splitlines()
    return contents

def selectWord(collection):
    return random.choice(collection)

def __main__():
    all_words = [readFile(FILES[ADJECTIVES]), readFile(FILES[NOUNS]), readFile(FILES[ADVERBS]), readFile(FILES[VERBS])]

    words = [None] * 4
    for i in range(4):
        words[i] = selectWord(all_words[i])

    for word in words:
        print(word, end=" ")
    print("\n")

if __name__ == "__main__":
    __main__()
