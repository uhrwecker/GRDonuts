from spacetime.schwarzschild import *
from spacetime.kerr import *
from inverse.kerr import InverseKerr
from vis.simple import *
from vis.polar import *
import matplotlib.pyplot as pl

i = Schwarzschild()
p = SimplePlotter()
p.plot(i)
