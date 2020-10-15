import numpy as np

#intergers

i = 10 #interger
print(type(i)) #data type of i

a_i=np.zeros(i,dtype=int) #declare an array on integers
print(type(a_i))
print(type(a_i[0]))

#floats

x = 119.0 #floating point number
print(type(x)) #print out data type of x

y = 1.19e2 #scientific notation
print(type(y)) #print out data type of y

z = np.zeros(i,dtype=float) #declare an array of float 
print(type(z))
print(type(z[0]))
