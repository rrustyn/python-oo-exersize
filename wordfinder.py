class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, filepath):
        self.filepath = filepath
        self.word_list = []
        self.read_file()

    def read_file(self):
        with open(self.filepath, "r") as file:
            for line in file:
                self.word_list.append(line)
