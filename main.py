from spacetime.schwarzschild import *
from spacetime.kerr import *
from spacetime.qmetric import *
from inverse.kerr import InverseKerr
from inverse.schwarzschild import InverseSchwarzschild
from vis.simple import *
from vis.polar import *
from vis.variation import *

import matplotlib.pyplot as pl


k = Kerr(verbose=False, r_range=(2, 200))

p = OneParamVarPlotter()
p.plot(k, 'l', (3, 5), num=1000)



