import pandas as pd
data=[1,2,3,4]
s1 = pd.Series(data)

print(s1)

s1= pd.Series(data, index=['a','b','c','d'])

print(s1)

print(s1['c'])
print(s1['a'])
print(s1[:2])
print(s1[-2:])

d1 = {'a':1,'b':2,'c':3,'d':4}
print(d1)

s2 = pd.Series(d1)
print(s2)

s2=s2[::-1]
print(s2)

s2 = pd.Series(d1,index=['d','b','c','a'])
print(s2)

# creating a data fram

data = [1,2,3,4]

df =pd.DataFrame(data)
print(df)

fruit = {'fruits':['apple', 'mango' , 'banana' , 'guava'],'count':[10,20,40,30]}
fruit_df = pd.DataFrame(fruit)
print(fruit_df)
