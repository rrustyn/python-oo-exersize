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
        self.start = self.current = start

    def __repr__(self):
        return f"SerialGenerator: Start: {self.start} Next: {self.current + 1}"

    def generate(self):
        """Increments current by one"""
        self.current += 1
        return self.current - 1

    def reset(self):
        """Resets incrementer"""
        self.current = self.start
