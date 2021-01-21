# polygon class (sequence of vertices)
from matrix import Matrix
from point import Point

# Polygon((x1, y1), (x2, y2)...)
class Polygon(Matrix):
    # make all setting be done using points
    def __setitem__(self, i, item): self._Matrix__array[i] = Point(*item)
    def append(self, item): self._Matrix__array.append(Point(*item))

# string versions
    # make the point show up as with str instead of repr
    def __str__(self): return "[{0}]".format(", ".join([str(item) for item in self._Matrix__array]))
    # string representation
    def __repr__(self): return f"<{type(self).__name__} vertices={self}>"
