from spacetime.schwarzschild import *
from spacetime.kerr import *
from inverse.kerr import InverseKerr
from inverse.schwarzschild import InverseSchwarzschild
from vis.simple import *
from vis.polar import *
import matplotlib.pyplot as pl

i = InverseSchwarzschild()
p = PolarPlotter()
p.plot(i, ymargin=15)
