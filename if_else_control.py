#define a function
def flow_control(k):

	#define a string based on the value of k
	if (k==0):
		s = "Variable k = %d equal to 0" % k
	elif (k==1):
		s = "variable k = %d equal to 1" % k 
	else:
		s = "Variable k = %d does not equal to 0 or 1" % k

	print(s) #print the string
#define a main function
def main():

	#declare an interger
	i=0

	#try flow_control with different value for i 
	flow_control(i)
	i=1
	flow_control(i)
	i=2
	flow_control(i)

#run the program
if __name__ == "__main__":
	main()

#flow_control will output different string depend on what k is 
#main function will pass a value that is i
#i will be passed to flow_control and will be k
