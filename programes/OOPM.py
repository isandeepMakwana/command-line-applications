# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:04:10 2020

@author: Admin

"""
'''
# OOPS Conceots



1. class and object 
2. Encapsulation
3. Polymorphism
4. Inheritance
5. Abstraction
6. Modularity

'''

"""
#program 1=>>>>
class sample:
    # private datamember
    #__name__ = "private datatype"    #__ varibel__ private datamember
    __name__= None
    
    def __init__(self):
        print("Hello I'm default constrauctor ")
        
    def fun(self, name):
        self.__name__ = name
        print("Hello world by using class !!!", self.__name__)
        
        
obj = sample()
obj.fun("Sandeep Makwnna is under the funtion")
"""       


'''

class sample:
    # private datamember
    __name__= None
    
    def __init__(self):     # constructor 
        self.__name__ = 'Sandeep makwana under the constructor'
        print("Hello I'm default constrauctor ")
        
    def fun(self):
        print("Hello world by using class !!!",self.__name__)
        
        
obj = sample()
obj.fun()



'''

'''
class Sample:
    __name__ = None 
    def __init__(self, name):
        self.__name__=name
        print("Hello ", self.__name__)
        
    def  function():
        pass
    #print("whatever ther")
    
Sample("Sandeep makwana")
#obj.function()

'''


"""
class Sample:
    __name__ = None 
    def __init__(self):
        pass
        
    def  function(self , list1, list2):
        d={}
        for i in range(len(list1)):
            d[list1[i]]=list2[i] 
        print(d)
        #print("whatever ther")
    
obj= Sample()
obj.function([1,2,3,4],["Sumit","Ravi","vikas","Shikha"])




"""
'''

class Sample:
    __name__= None
    
    def setName(self, name):
        self.__name__= name 
        
        
    def getName(self):
        return self.__name__
    
    

'''

"""
# encapsulation 
class Example:
    __name = None 
    __age = None
    
    def setName (self , name):
        self.__name = name

    def setAge(self ,age):
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age


name = input("Enter your name :")
age = int(input("Enter your age :"))        
obj = Example()
obj.setName(name)
obj.setAge(age)
n= obj.getName()
a= obj.getAge()

if a>17:
    print(f"{n} you are eligible to vote")
else:
    print(f"{n} you are minor")
    
"""
'''
#static ploymorphism

def add(a, b, c=10):
    return (a+b+c)
print("result ", add(15,10,15))


def add(list):
    sum = 0
    for i in list:
        sum +=i
    return sum


print("result ", add([5,10,15]))

'''
"""
#Daynamic polymorphsim
class India:
    def currency(self):
        print("indian INR rupess")

    def capital(self):
        print("New Delhi")
        
        
    
class USA:
    def currency(self):
        print(" American Dollar")

    def capital(self):
        print(" Washington Dc")
        
#ind = India()
#usa= USA()

#for i in (ind, usa):
 #   i.capital()
  #  i.currency()



def display(country):
    country.capital()
    country.currency()
         
ind = India()
usa= USA()   

display(ind)
display(usa)
"""

"""
# inheritance
#simple

class Parent:
    __name = None
    def __init__(self):
        self.__name = "sandeep makwana"
        print(self.__name)
    def show(self):
        print("Please wait !!!!!!")
        
class Child(Parent): # if you two class c(a,b)
    def display(self):
        super().show()

obj = Child()
obj.display()

"""


#static anotation

class StaticAnnotation:
    
    @staticmethod
    def display():
        print("hello world !")
        
StaticAnnotation.display()



