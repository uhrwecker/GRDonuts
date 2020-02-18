import numpy as np
import matplotlib.pyplot as pl
from vis.simple import Plotter

class SimplePolarPlotter(Plotter):
    def __init__(self, figsize=(10, 10), save=None):
        super().__init__(figsize=figsize, save=save)

    def plot(self, potential, label='', xmargin=0, ymargin=10):
        thetas = potential.compute_w()
        r = potential.get_r()
        rs = np.concatenate((r, r))

        theta_max = np.nanmax(np.abs(thetas))
        pl.polar(thetas, rs)
        pl.ylim(r[0] - xmargin, r[-1] + xmargin)
        pl.xlim((-theta_max-ymargin)/180*np.pi, (theta_max+ymargin)/180*np.pi)
        
        if self.save:
            pl.savefig(self.save)
        else:
            pl.show()

class PolarScharrPlotter(Plotter):
    def __init__(self, figsize=(10, 10), save=None):
        super().__init__(figsize=figsize, save=save)

    def plot(self, pot_list, label_list, xmargin=0, ymargin=0.003):
        for item, label in zip(pot_list, label_list):
            thetas = item.compute_w()
            r = item.get_r()
            rs = np.concatenate((r, r))

            theta_max = np.nanmax(np.abs(thetas))
            pl.polar(thetas, rs, label=label)
            
        pl.ylim(r[0] - xmargin, r[-1] + xmargin)
        pl.xlim((-theta_max-ymargin)/180*np.pi, (theta_max+ymargin)/180*np.pi)
            
        if self.save:
            pl.savefig(self.save)
        else:
            pl.show()
            
