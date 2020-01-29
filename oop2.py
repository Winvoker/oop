#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:10:34 2020

@author: batuhan
"""
from abc import ABC,abstractmethod

class Shape(ABC): # my abstract class

    @abstractmethod
    def area(self): pass # my abstract method
    @abstractmethod
    def perimeter(self): pass # my abstract method
    
    def toString(self): pass
    
class Square(Shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        return(self.a*self.a)
    def perimeter(self):
        return(self.a*4)
        
    def toString(self):
        print("Square")
class Circle(Shape):
    def __init__(self,a):
        self.a=a
    def area(self,a):
        return(3.14*self.a**2)
    def perimeter(self):
        return(2*3.14*self.a)
    def toString(self):
        print("circle")
sekil=Square(2)