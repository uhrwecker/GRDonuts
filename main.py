from spacetime.schwarzschild import *
from spacetime.kerr import *
from spacetime.qmetric import *
from inverse.kerr import InverseKerr
from inverse.schwarzschild import InverseSchwarzschild
from vis.simple import *
from vis.polar import *
import matplotlib.pyplot as pl


k = QMetric()
p = BeautyPlotter()
p.plot(k, label='')
