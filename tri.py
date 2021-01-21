# triangle class
from matrix import Matrix
from point import Point

class Tri(Matrix):
    # 3 vertices
    def __init__(self, v1, v2, v3):
        super().__init__(Point(*v1), Point(*v2), Point(*v3))

# vertices
    # vertex 1
    @property
    def v1(self): return self[0]
    @v1.setter
    def v1(self, v1): self[0] = v1

    # vertex 2
    @property
    def v2(self): return self[1]
    @v2.setter
    def v2(self, v2): self[1] = v2

    # vertex 3
    @property
    def v3(self): return self[2]
    @v3.setter
    def v3(self, v3): self[2] = v3

# string versions
    # make the point show up as with str instead of repr
    def __str__(self): return "[{0}]".format(", ".join([str(item) for item in self.__array]))
    # string representation
    def __repr__(self): return f"<{type(self).__name__} vertices={self}>"
