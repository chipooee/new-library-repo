from math import pi
from fractions import Fraction
def Circle(r:int):
    #area unit:cm2
    s = pi*(r*r)
    return s
def Square(a:int):
    #area unit:cm2
    s=a*a
    return s
def Rectangle(a:int,b:int):
    #area unit:cm2
    s=a*b
    return s
def Triangle(a:int,h:int):
    #area unit:cm2
    s=a*h/2
    return s
def Cylinder(s:int,h:int):
    #volume unit:cm3
    v=s*h
    return v
def Cone(s:int,h:int):
    #volume unit:cm3
    v=s*h*Fraction(3,1)
    return v
def Sphere(r:int):
    #volume unit:cm3
    v=pi*(r*r*r)*Fraction(3,4)
    return v