#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:10:34 2020

@author: batuhan
"""

class Vehicle():
    def __init__(self,stock):
        self.stock = stock
    def display(self):
        print("Stock :",self.stock)
    def rent(self,n,var):
        if var == 'car':
            if n <= 0:
                print("Error")
                return None
            elif n>=self.stock:
                print("We just have {} cars.".format(self.stock))
                return None
            else:
                self.stock -= n
                return self.stock
        elif var == 'bcy':
            if n <= 0:
                print("Error")
                return None
            elif n>=self.stock:
                print("We just have {} cars.".format(self.stock))
                return None
            else:
                self.stock -= n
                return self.stock
    def returnVehicle(self,n,var):
        carPrice = 100
        bcyPrice = 10
        if(var=='car'):
            self.stock += n
            price= carPrice*n
        elif(var=='bcy'):
            self.stock += n
            price = n*bcyPrice
        print("Price : $",price)
        return price

class Car(Vehicle):
    def __init__(self,stock):
        super().__init__(stock)
    def discount():
        pass

class Bicy(Vehicle):
    def __init__(self,stock):
        super().__init__(stock)
    
class Musteri():
    def __init__(self):
        self.car=0
        self.bcy=0
    def request(self):
        x =int(input("1.Araba 2.Bisiklet :"))
        if(x==1):
            num = int(input("Kac adet istiyorsunuz ?"))
            self.car=num
        elif(x==2):
            num = int(input("Kac adet istiyorsunuz ?"))
            self.bcy = num
    def returnVehicle(self, var):
        if(var=='bcy'):
            return self.car
        elif(var=='car'):
            return self.bcy
        
    
        