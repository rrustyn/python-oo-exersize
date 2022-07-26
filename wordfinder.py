from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        """generates word list form filepath, and prints number of words"""
        self.filepath = filepath
        self.word_list = []
        self.read_file()
        self.print_num_words()

    def read_file(self):
        """opens file, and appends word list from file"""
        with open(self.filepath, "r") as file:
            for line in file:
                self.word_list.append(line.removesuffix('\n'))

    def print_num_words(self):
        """ prints number of words"""
        print(f"{len(self.word_list)} words read")

    def random(self):
        """returns a random word from word list"""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    def __init__(self, filepath):
        super().__init__(filepath)

    def read_file(self):
        """opens file, and appends word list, if line is empty or
        starts with #, words will not be appended"""
        with open(self.filepath, "r") as file:
            for line in file:
                if "#" not in line and line != '\n':
                    self.word_list.append(line.removesuffix('\n'))
