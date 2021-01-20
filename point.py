# point class
from matrix import Matrix

# x, y
class Point(Matrix):
    def __init__(self, x=0, y=0): super().__init__(x, y)
    # x
    @property
    def x(self): return self[0]
    @x.setter
    def x(self, x): self[0] = x

    # y
    @property
    def y(self): return self[1]
    @y.setter
    def y(self, y): self[1] = y

    # conv to str, use tuple to look more like coords
    def __str__(self): return str(tuple(self))
    # representation as string
    def __repr__(self): return f"<{type(self).__name__} x={self.x} y={self.y}>"
