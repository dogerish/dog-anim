# matrix class (1 dimensional)
class Matrix:
    def __init__(self, *array): self.__array = list(array)

    # to iterable
    def __iter__(self): return iter(self.__array)
    # to string
    def __str__(self): return str(self.__array)
    def __repr__(self): return f"<{type(self).__name__} array={self}>"
    # indexing
    def __getitem__(self, i): return self.__array[i]
    def __setitem__(self, i, x): self.__array[i] = x
    # length
    def __len__(self): return len(self.__array)

    # append
    def append(self, thing): return self.__array.append(thing)

# per item
    # executes f for each, giving i as the only argument
    def foreach(self, f): return Matrix(*[f(i) for i in range(len(self))])
    # gives the two values for each item, giving a and b values as the arguments
    def oneach(a, b, f): return a.foreach(lambda i: f(a[i], b[i]))
    # same as foreach and oneach except it applies directly to itself
    def foreachto(self, f):
        for i in range(len(self)):
            self[i] = f(i)
        return self
    def oneachto(a, b, f): return a.foreachto(lambda i: f(a[i], b[i]))

# operators
# on self version
    # addition
    def __add__(self, mat): return self.oneach(mat, lambda a, b: a+b)
    def add(self, mat): return self.oneachto(mat, lambda a, b: a+b)
    # subtraction
    def __sub__(self, mat): return self.oneach(mat, lambda a, b: a-b)
    def sub(self, mat): return self.oneachto(mat, lambda a, b: a-b)
    # multiplication
    def __mul__(self, mat): return self.oneach(mat, lambda a, b: a*b)
    def mul(self, mat): return self.oneachto(mat, lambda a, b: a*b)
    # division
    def __truediv__(self, mat): return self.oneach(mat, lambda a, b: a/b)
    def truediv(self, mat): return self.oneachto(mat, lambda a, b: a/b)

    # sets items to be same as mat
    def set(self, mat): return self.oneachto(mat, lambda a, b: b)
