from spacetime.schwarzschild import *
from spacetime.kerr import *
from spacetime.qmetric import *
from inverse.kerr import InverseKerr
from inverse.schwarzschild import InverseSchwarzschild
from inverse.qmetric import InverseQMetric
from vis.simple import *
from vis.polar import *
from vis.variation import *

import matplotlib.pyplot as pl

pot = InverseQMetric()


p = SimplePolarPlotter()
p.plot(pot)
