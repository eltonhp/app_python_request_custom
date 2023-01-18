class Total:
    def __init__(self) -> None:
        self._nome = ''

    def read(self, filename):
        """ read a text file and return a list of numbers """
        with open(filename) as f:
            lines = f.readlines()
            return [float(line.strip()) for line in lines]


    def calculate_total(self, filename):
        """ return the sum of numbers in a text file """
        numbers = self.read(filename)
        return sum(numbers)