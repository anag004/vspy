VSPY - Vector Spaces in Python
============================

VSPY (_vespy_) is a Python[3] library which allows you to do algebra with vector spaces. You can define your own custom vector spaces and scalars and use them for vector algebra. VSPY is intuitive and uses overloaded numeric and comparison operators for vector operations. You can
- Find a spanning [vector] space of a set of vectors 
- Check if a vector space contains some vector
- Check if a vector space contains another vector space
- Intersect and add vector spaces

## Installation
Firstly, clone the repository and cd into it. VSPY uses the sympy and numpy python libraries, which you can install by typing in 

    python3 -m pip install -r requirements.txt
  
If you prefer creating a virtual environment, you create one and install the requirements by

    python3 -m virtualenv env
    pip install -r requirements.txt 
    source env/bin/activate
    
To test the installation simply run the following inside the repository

    python -m unittest
    
You should expect something like (the number of tests may vary)

    ............................................................................
    ----------------------------------------------------------------------
    Ran 76 tests in 0.050s

    OK
    
## Quick Guide

Check the `test*.py` files for a demo of the various modules. The test files are self-explanatory and exhaustive. 

## Defining your own vector spaces

This is simple to do and is what makes VSPY so powerful. To define a new vector you must write a class which inherits the abstract `Vector` class in `vector.py`. You must overload all the functions specified in the abstract class. Several examples are provided (see `simple_vectors.py`, `poly_univar.py` and `poly_hom_bivar.py`). These vectors can then be used to define vector spaces.

Likewise, if you wish to define new scalars you must define a custom class inheriting the `Scalar` class in `vector.py` overloading the abstract methods therein. For examples, see `real.py` and `mod_integer.py` which define the real numbers and integers modulo m. 
