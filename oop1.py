#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:26:13 2020

@author: batuhan
"""
class Calc(object):
    def __init__(self, a, b):
        self.var1 = a        
        self.var2 = b
    def add(self):
        return(self.var1+self.var2)
        
    def subtract(self):
        return(self.var1-self.var2)
        
    def multiply(self):
        return(self.var1*self.var2)        
    
    def divide(self):
        return(self.var1/self.var2)

a,b = input("İki sayı giriniz : ").split(" ")
a,b = int(a),int(b)

n = int(input("1.Toplama 2.Cıkarma 3.Carpma 4.Bolme : "))

obj1=Calc(a,b)
if(n==1):
    print(obj1.add())
elif(n==2):
    print(obj1.subtract())
elif(n==3):
    print(obj1.multiply())
elif(n==4):
    print(obj1.divide())
else:
    print("Hatalı islem")
    