class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    # make two methods __init__ generate and reset
    def __init__(self, start):
        """Saving the start value and making an incrementer"""
        self.start = start
        self.current = start - 1

    def __repr__(self):
        return f"SerialGenerator: Start: {self.start} Current: {self.current}"

    def generate(self):
        """Increments current by one"""
        self.current += 1
        return self.current

    def reset(self):
        """Resets incrementer"""
        self.current = self.start - 1