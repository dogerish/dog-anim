# vector class
from math import sqrt, sin, cos, atan2
from point import Point

# x, y, heading, magnitude
# from_heading, normalize
class Vector(Point):
    # create vector from heading and magnitude
    def from_heading(heading, mag=1):
        vec = Vector(mag, 0)
        vec.heading = heading
        return vec

  # magnitude
    # sets magnitude to 1
    def normalize(self):
        h = self.heading
        return self.set((cos(h), sin(h)))

    @property
    def mag(self): return sqrt(self.x**2 + self.y**2)
    @mag.setter
    def mag(self, mag): self.normalize().mul([mag]*2)


    # heading
    @property
    def heading(self): return atan2(self.y, self.x)
    @heading.setter
    def heading(self, heading): self.set(Matrix(*([self.mag]*2)) * (cos(heading), sin(heading)))
