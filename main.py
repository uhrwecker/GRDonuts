from spacetime import *
from inverse import *
from vis import *

import time

import matplotlib.pyplot as pl
import numpy as np

pot = DistortedSchwarzschild(r_range=(0, 50), num=100000)

p = TwoParamVarPlotter()
p.plot(pot, 'l', (0, 15), 'o', (-1, 1), num1=500, num2=500)

