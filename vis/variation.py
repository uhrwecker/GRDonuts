from vis.simple import Plotter
import matplotlib.pyplot as pl
import numpy as np

class OneParamVarPlotter(Plotter):
    def __init__(self, figsize=(10, 10), save=None):
        super().__init__(figsize=figsize, save=save)

    def plot(self, potential, name, rang, num=1000,
             verbose=False):

        setattr(potential, 'verbose', verbose)

        print('Start calculating closed surfaces. \n This may take a while ...')

        y_val = potential.one_parameter_variation_stability_test(name, rang,
                                                                 num=num)

        print('Plotting ...')
        ax = pl.gca()
        ax.plot(np.linspace(rang[0], rang[1], num=len(y_val)), y_val,
                label='closure area (roche limit) for theta=pi/2')

        ax.set_ylim(0, 1.05)
        ax.set_xlim(rang[0], rang[1])

        ax.set_ylabel('closure rating')
        ax.set_xlabel(name)

        pl.legend()

        if self.save:
            pl.savefig(self.save)

        else:
            pl.show()

        

class TwoParamVarPlotter(Plotter):
    def __init__(self, figsize=(10, 10), save=None):
        super().__init__(figsize=figsize, save=save)

    def plot(self, potential, name1, rang1, name2,
             rang2, num1=100, num2=100, verbose=False):

        self.n1 = name1
        self.n2 = name2
        self.num1 = num1
        self.r1 = rang1
        self.r2 = rang2
        self.num2 = num2

        def format_func_x(value, tick_number):
            tick = self.r2[0] + (self.r2[1]-self.r2[0]) * value / self.num2 
            return str(tick)[:4]

        def format_func_y(value, tick_number):
            tick = self.r1[0] + (self.r1[1]-self.r1[0]) * value / self.num1
            return str(tick)[:4]
            
        
        setattr(potential, 'verbose', verbose)

        print('Start calculating closed surfaces. \n This may take a while ...')
        matrix = potential.two_parameter_variation_stability_test(name1,
                                                                  rang1,
                                                                  name2,
                                                                  rang2,
                                                                  num1=num1,
                                                                  num2=num2)
        print('Calculated Matrix.')
        print('Plotting ...')
        ax = self.figure.gca()
        cmap = pl.get_cmap('autumn')
        
        ax.imshow(matrix, cmap=cmap)
        
        ax.xaxis.set_major_formatter(pl.FuncFormatter(format_func_x))
        ax.yaxis.set_major_formatter(pl.FuncFormatter(format_func_y))

        ax.axvline(self.num2/2, c='black')
        ax.axhline(self.num1/2, c='black')


        ax.set_ylim(0, self.num1)
        ax.set_xlim(0, self.num2)

        ax.set_ylabel(self.n1)
        ax.set_xlabel(self.n2)

        if self.save:
            pl.savefig(self.save)

        else:
            pl.show()
        
        

        
        
        
