from spacetime import *
from inverse.kerr import InverseKerr
from inverse.schwarzschild import InverseSchwarzschild
from inverse.qmetric import InverseQMetric
from vis.simple import *
from vis.polar import *
from vis.variation import *

import time

import matplotlib.pyplot as pl
import numpy as np

pot2 = QMetric(l=3, q=1, r_range=(0, 5), num=100000)

p = BeautyPlotter()
p.plot(pot2, ymargin=1, label='q=1, l=3')

