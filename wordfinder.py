from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("./words.txt")
    14 words read
    >>> wf.random() in wf.word_list
    True

    """

    def __init__(self, filepath):
        """generates word list form filepath, and prints number of words"""
        self.filepath = filepath
        self.word_list = []
        self.read_file()
        print(f"{len(self.word_list)} words read")

    def read_file(self):
        """opens file, and appends word list from file"""
        with open(self.filepath, "r") as file:
            for line in file:
                self.word_list.append(line.removesuffix('\n'))

    def random(self):
        """returns a random word from word list"""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """ takes away empty lines and comments from word list"""

    def __init__(self, filepath):
        super().__init__(filepath)

    def read_file(self):
        """opens file, and appends word list, if line is empty or
        starts with #, words will not be appended"""
        super().read_file()
        self.word_list = [
            word for word in self.word_list if "#" not in word and word != '']
