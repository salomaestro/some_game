class Matrix:
    def __init__(self, elements):
        """
        initen tester at vi har korrekt input, en liste
        """
        try:
            if isinstance(elements, list):
                self.elem = elements
        except Exception as e:
            raise e
        self.isquadratic = False
        # n er antall rader m er antall søyler, altså har vi en n x m matrise
        self.n = len(self.elem)
        self.m = [len(row) for row in self.elem][0]
        if self.n == self.m:
            self.isquadratic = True
        self.size = '{} x {}'.format(self.n, self.m)

    def __str__(self):
        string = ''
        for col in self.elem:
            string += str(col) + '\n'
        return string

    def __add__(self, other):
        added = [[ j + k for j, k in zip(i, l)]for i, l in zip(self.elem, other.elem)]
        return Matrix(added)

    def __sub__(self, other):
        subbd = [[ j - k for j, k in zip(i, l)]for i, l in zip(self.elem, other.elem)]
        return Matrix(subbd)

if __name__ == "__main__":
    a = [[2, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[2, 9, -5], [-1, 8, 8], [7, 2, 4]]
    c = [[1, 2], [3, 4]]
    m1 = Matrix(a)
    m2 = Matrix(b)
    m3 = Matrix(c)

    print(m1)
    print(m1 - m2)
