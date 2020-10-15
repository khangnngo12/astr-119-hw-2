#python exceptions let you deal with 
#unexpected result

try:
	print(a) #will cause an error
except:
	print("a is not defined!")

#there are specific errors to help with specific cases
try:
	print(a) #this is a NameError
except NameError: #using the name of the specific error
	print("a is still not defined!")
except: #any other errors will result in this instead
	print("Something else when wrong.")

print(a)