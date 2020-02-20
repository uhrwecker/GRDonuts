from spacetime.schwarzschild import *
from spacetime.kerr import *
from inverse.kerr import InverseKerr
from inverse.schwarzschild import InverseSchwarzschild
from vis.simple import *
from vis.polar import *
import matplotlib.pyplot as pl

i = Schwarzschild()
p = BeautyPlotter(figsize=(10, 5), save='./schwarzschild.png')
p.plot(i, xmargin=2)
