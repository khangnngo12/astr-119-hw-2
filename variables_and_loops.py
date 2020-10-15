import numpy as np #importing numpy

def main():
	i=0 #declaring an interger
	n=10 #another interger
	x=119.0 #declare a point number using "."

	#use numpy to quickly create array 

	y=np.zeros(n,dtype=float) #declares 10 zeroes as float using numpy

	#use for loops to iterate with a variable 

	for i in range(n): #for i in range [0,n-1]
		y[i] = 2.0 * float(i) +1 #set y=2i+1 as floats

	#use for loops to iterate through a variable 
	for y_element in y:
		print(y_element)

#run main function:
if __name__ == "__main__":
	main()

#use numpy to create an array of zeroes 
#use for loop to loop through the array of zeroes and changing their values 
#use for loop to print out each individual elements in y 
#execute program 



