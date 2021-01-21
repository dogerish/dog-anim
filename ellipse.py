# ellipse class
from rect import Rect

class Ellipse(Rect):
# radii
    # x radius
    @property
    def rx(self): return self.w / 2
    @rx.setter
    def rx(self, rx): return self.w = rx * 2

    # y radius
    @property
    def ry(self): return self.h / 2
    @ry.setter
    def ry(self, ry): return self.h = ry * 2
