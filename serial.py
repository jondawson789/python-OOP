"""Python serial number generator."""

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
    def __init__(self, start = 0):
        "create starting number"
        self.start = start
        self.next = start - 1

    def __repr__(self):
        return f"<SerialGenerator start = {self.start}>"

    def generate(self):
        "increment starting number"
        self.next = self.next + 1
        return self.next

    def reset(self):
        "reset number to starting number"
        self.next = self.start - 1
        

