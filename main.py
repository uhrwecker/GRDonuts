from spacetime.schwarzschild import *
from spacetime.kerr import *
from spacetime.qmetric import *
from inverse.kerr import InverseKerr
from inverse.schwarzschild import InverseSchwarzschild
from vis.simple import *
from vis.polar import *
from vis.variation import *

import matplotlib.pyplot as pl


k = Kerr()
p = TwoParamVarPlotter()
p.plot(k, 'a', (0, 1), 'l', (0, 8))



