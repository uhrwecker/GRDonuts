# Welcome to GRDonuts  
  
This little software package is a toolkit for creating and computing (closed) equipotential surfaces of perfect fluids orbiting compact stellar objects (see Zarotti, Relativistic Hydrodynamics, ch. 11.7).   
In literature, these are also called Polish Doughnuts or geometrically thick tori. 

## Minimal example  
  
A always working minmal example can be found in `main.py`.   
  
  
At the time being, there are no plans on integrating a CLI, as it is recommended to use a python program to configure the donuts. Future plans include a config file, however.

## First time use

You need to download the repository from github either:

* directly from /github.com: [GRDonuts](https://github.com/uhrwecker/GRDonuts.git)  
* or clone it from the link:  
```git clone https://github.com/uhrwecker/GRDonuts.git```  
  
After this, change into the git repository and install the minimal requirements via pip:  
``` cd path/to/GRDonuts ```  
``` pip install -r requirements.txt ```
  
## Usage

The general usage is:  
1. Import the effective potential you want to investigate  
2. Import a suitable plotter for your purpose and potential  
3. Instanciate the potential with the set of parameters of your choice  
4. Instanciate the plotter with the set of parameters of your choice  
5. Use the `.plot` method of your plotter to show your result  
  
Minimal example:    
  
    from spacetime import *   
    from vis import *  
      
    potential = Schwarzschild()
    plotter = SimplePlotter()
    plotter.plot(potential)
