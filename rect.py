# rect class
from point import Point
from matrix import Matrix

# x, y, w, h, size, t, l, r, b, tl, tr, bl, br, w, h, m, mt, ml, mr, mb
# scale, move
class Rect(Point):
    # rel to top left corner, restrict to 4 required args
    def __init__(self, x, y, w, h):
        Matrix.__init__(self, x, y, w, h)

# size
    # width
    @property
    def w(self): return self[2]
    @w.setter
    def w(self, w): self[2] = w

    # height
    @property
    def h(self): return self[3]
    @h.setter
    def h(self, h): self[3] = h

    # size
    @property
    def size(self): return Matrix(self.w, self.h)
    @size.setter
    def size(self, size): self.w, self.h = size

# edges
    # top
    @property
    def t(self): return self.y
    @t.setter
    def t(self, t): self.y = t

    # left
    @property
    def l(self): return self.x
    @l.setter
    def l(self, l): self.x = l

    # right
    @property
    def r(self): return self.x + self.w
    @r.setter
    def r(self, r): self.x = r - self.w

    # bottom
    @property
    def b(self): return self.y + self.h
    @b.setter
    def b(self, b): self.y = b - self.h

# corners
    # top left
    @property
    def tl(self): return Point(self.l, self.t)
    @tl.setter
    def tl(self, tl): self.l, self.t = tl

    # top right
    @property
    def tr(self): return Point(self.r, self.t)
    @tr.setter
    def tr(self, tr): self.r, self.t = tr

    # bottom left
    @property
    def bl(self): return Point(self.l, self.b)
    @bl.setter
    def bl(self, bl): self.l, self.b = bl

    # bottom right
    @property
    def br(self): return Point(self.r, self.b)
    @br.setter
    def br(self, br): self.r, self.b = br

# midpoints
    # center/middle
    @property
    def m(self): return Point(*(self + (self.w / 2, self.h / 2)))
    @m.setter
    def m(self, m): self.set(m - (self.w / 2, self.h / 2))

    # middle top
    @property
    def mt(self): return Point(self.m.x, self.t)
    @mt.setter
    def mt(self, mt): self.m, self.t = (mt.x, self.m.y), mt.y

    # middle left
    @property
    def ml(self): return Point(self.l, self.m.y)
    @ml.setter
    def ml(self, ml): self.l, self.m = ml.x, (self.m.x, ml.y)

    # middle right
    @property
    def mr(self): return Point(self.r, self.m.y)
    @mr.setter
    def mr(self, mr): self.r, self.m = mr.x, (self.m.x, mr.y)

    # middle bottom
    @property
    def mb(self): return Point(self.m.x, self.b)
    @mb.setter
    def mb(self, mb): self.m, self.b = (mb.x, self.m.y), mb.y

# methods
    # move rect by offset, if not specified, y will be the same as x
    def move(self, x, y=None):
        self.tl += (x, x if y == None else y)
        return self
    # scale rect by ratio
    def scale(self, ratio):
        self.size *= [ratio]*2
        return self

# string versions
    # conv to string
    def __str__(self): return f"|{self.x}, {self.y}, {self.w}, {self.h}|"
    # string representation
    def __repr__(self): return f"<{type(self).__name__} x={self.x} y={self.y} w={self.w} h={self.h}>"
