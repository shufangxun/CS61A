"""generalization"""
from math import pi, sqrt

def area(r,shape):
    assert r>0, 'a length must be positive'  
    assert shape>0, 'a shape must be positive'
    return r*r*shape



def area_squre(r):
    return area(r,1)

def area_circle(r):
    return area(r,pi)

def area_hexagon(r):
    return area(r,3*sqrt(3)/2)

