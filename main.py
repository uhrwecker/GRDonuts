from spacetime.schwarzschild import *
from spacetime.kerr import *
from inverse.kerr import InverseKerr
from inverse.schwarzschild import InverseSchwarzschild
from vis.simple import *
from vis.polar import *
import matplotlib.pyplot as pl

i1 = InverseKerr()
i2 = InverseKerr(w=-0.041)
p = PolarScharrPlotter()
p.plot([i1, i2], ['w=-0.042', 'w=-0.041'], ymargin=15)
