class Matrix:
    def __init__(self, elements):
        """
        initen tester at vi har korrekt input, en liste samt den vil si noe om matrisen er kvadratisk og hvilken
        størrelse matrisen har
        """

        try:
            if isinstance(elements, list):
                self.elem = elements
        except Exception as e:
            raise e

        self.isquadratic = False
        # m er antall rader n er antall søyler, altså har vi en n x m matrise
        self.m = len(self.elem)
        self.n = [len(row) for row in self.elem][0]
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

    def __mul__(self, other):
        res = [[0]*self.n]*self.n
        if self.n == other.m:
            for i in range(self.m):
                for j in range(other.n):
                    for k in range(self.n):
                        res[i][j] += self.elem[i][k] * other.elem[k][j]
            return Matrix(res)

if __name__ == "__main__":

    a = [[2, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[2, 9, -5], [-1, 8, 8], [7, 2, 4]]
    c = [[1, 2], [3, 4]]
    d = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

    A = Matrix(a)
    B = Matrix(b)
    C = Matrix(c)
    D = Matrix(d)

    # print(A)
    # print(A - B)
    print(D * D)
