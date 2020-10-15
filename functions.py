import numpy as np 
import sys

#define a function that return a value
def expo(x):
	return np.exp(x) #return e^x function

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))

#define a main function
def main():
	n = 10 #provide a default function for n

	#check if there is a command line argument line provided 
	if (len(sys.argv)>1):
		n = int(sys.argv[1]) #if an argument is provided, use it for n 

	show_expo(n) #call show_expo

#run the main function
if __name__ == "__main__":
	main()

#main function provide a value for n 
#n is passed into show_expo and is used in a for loop
#within the for loop, expo function is called 
#expo function take x and associate it with float(i) and take the exp of it
