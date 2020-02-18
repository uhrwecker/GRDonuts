from spacetime.potential import *
from spacetime.inv import InverseKerr
from vis.simple import *
from vis.polar import *
from inverse.inverse import *
import matplotlib.pyplot as pl

i = InverseKerr(w=-0.042)
p = PolarPlotter()
p.plot(i)
