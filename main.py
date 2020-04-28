from spacetime import *
from inverse import *
from vis import *
from von_zeipel import *

import time

import matplotlib.pyplot as pl
import numpy as np

potential = Schwarzschild()
plotter = SimplePlotter()
plotter.plot(potential)
