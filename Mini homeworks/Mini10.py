'''
rite a class Car. Car should have following attributes:
make - Hidden attribute for make (brand) of the car.
model - Hidden attribute for model of the car.
fuel - Hidden attribute, fuel left in tank in litres.
litresPer100km - Fuel consumption per 100 kilometres.
Car class should have following methods:
constructor - It should take make and model as arguments and initialize attributes. Fuel's default value should be 0 and litresPer100km's - 8.0.
getMake, getModel, getFuel - getter functions which return current make, model and fuel of the car.
addFuel - method takes one argument, fuel in litres, and adds it into the tank (fuel attribute). You can assume that tank can hold infinite amount of fuel.
drive - this method is passed number of kilometres driven by the car and it should decrease amount of fuel accordingly. For example if fuel consumption (litresPer100km) is equal to 8.0 and distance is 150 kms, than car will consume 12.0 litres of fuel and 12.0 should be subtracted from fuel. You can assume that there always is enough fuel.
distanceToE - this method should return how many kms left until fuel tank becomes empty. For example, if fuel consumption is 6.0 and there still is 8.4 litres left in the car than fuel is enough to drive 140 kms until tank becomes empty.
'''

class Car:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model
        self.__fuel = 0
        self.__litresPer100km = 8.0
        
    def getMake(self):
        return self.__make
    
    def getModel(self):
        return self.__model
    
    def getFuel(self):
        return self.__fuel
    
    def addFuel(self, fuel):
        self.__fuel += fuel
        
    def drive(self, distance):
        self.__fuel -= distance * self.__litresPer100km / 100
        
    def distanceToE(self):
        return self.__fuel * 100 / self.__litresPer100km
    
car = Car("Ford", "Focus")