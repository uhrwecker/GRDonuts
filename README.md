# GRDonuts
Toolkit for creating plots and computing stable equipotential surfaces of fluids orbiting a compact stellar object (see Zarotti: Relativistic Hydrodynamics)

## Minimal example

For a minimal example, see main.py.

## Developement

See the issues for the current status of the code.
If you want to contrubute:
- working on the issues: create a new branch with namescheme: issue_no-user-title
- push and pull as you like, but do not merge. I will do the merging, ping me if you want to merge.

## Theoretical background

> For perfect fluids, orbiting a compact, spherical, staionary object, the Potential W (in terms of the metric) of the fluid is given by:

>  W = \frac{1}{2} \sqrt -(g_{tt} + 2l g_{t \phi} + l^2 g_{\phi \phi} ) 

This is implemented for various spacetimes (see spacetime directory/). 
Just import the explicit Potential you want, and instanciate it. 
In general, this will give you the Potential in terms of the distance r.

## Plotting

There a various plotters available in the vis/ directory. Import any Plotter you like, and instaciate it. 
To plot any potential, simply call Plotter.plot(potential) (see documentary).

## Inverse potential and plotting

Currently, for Kerr and Schwarzschild spacetimes, there is the possibility to look at the angular distribution, depending on the distance r. This will give you plots for a given value of the potential w. This is found in the inverse/ directory.

# 

For plotting the inverse problem, please see to using one of the inverse plotter in vis/ directory.
