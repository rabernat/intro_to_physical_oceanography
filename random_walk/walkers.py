from pylab import *
from numpy.random import random_sample

class RandomWalker():
    """A random walker in two dimensions"""

    def __init__(self, x0=0., y0=0., amp=1., Nhist=5):        
        self.x0 = x0
        self.y0 = y0
        self.x = x0
        self.y = y0
        self.amp = amp
        # the previous 3 locations
        self.x_hist = x0 * zeros(Nhist)
        self.y_hist = y0 * zeros(Nhist)
        
    def step_forward(self):
        # dx^2 + dy^2 = amp2
        # random angle for vector
        theta = 2*pi*random_sample()
        dx = self.amp*cos(theta)
        dy = self.amp*sin(theta)
        self.x += dx
        self.y += dy
        self.x_hist[:-1] = self.x_hist[1:]
        self.y_hist[:-1] = self.y_hist[1:]
        self.x_hist[-1] = self.x
        self.y_hist[-1] = self.y
        
    def dist_from_origin(self):
        return sqrt((self.x - self.x0)**2 + (self.y - self.y0)**2)
