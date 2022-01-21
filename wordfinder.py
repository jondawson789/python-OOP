"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """find random word from list

    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """
    def __init__(self, path):
        "read lines into list"
        with open(f"{path}") as f:
            word_list = f.readlines()


        self.lines = self.parse(word_list)

        print(f"{len(self.lines)} words read")
        f.close()

    def parse(self, word_list):
        for line in word_list:
                line = line.rstrip()

        return word_list
    def random(self):
        "return random word from list"
        return random.choice(self.lines)



class SpecialWordFinder(WordFinder):
    def parse(self, word_list):
        out = []
        for line in word_list:
            if not line == "\n" and line.startswith("#") == False:
                out.append(line.rstrip())

        return out

wf = SpecialWordFinder('complex.txt')
word = wf.random()
print(word)

