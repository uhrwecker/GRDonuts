from vis.simple import Plotter

class 3DPlotter(Plotter):
    def __init__(self, figsize=(10, 10), save=None):
        super().__init__(figsize=figsize, save=save)

    def plot(self, potential, label='', xlim=4, ylim=4, zlim=4,
             horizon=False):
        def x(r, theta, phi):
            return 2
        
        
