def main():
	i=0 #declare an integer 1
	x=119.0 #declare a float x 

	for i in range(120): #make a loop that loop 0 through 119
		if i%2 ==0: #if i is even
			x+=3 #add three to x
		else: #if i is odd
			x-=5 #subtract five from x 

	s = "%3.2e" % x #make a string containing x 
			#with scientific notation and two decimal places

	print(s)

if __name__ == "__main__": #if the main function exist, run it
	main ()
