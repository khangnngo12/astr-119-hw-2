# string

s = "This is a string"
print(type(s))

#boolean

yes=True #Boolean True
print(type(yes))

no=False #Boolean False
print(type(no))

#list - ordered and changable

alpha_list = ["a","b","c"] 
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d") #append "d" to the end of the list
print(alpha_list)

#tuple - ordered and unchangable
alpha_tuple = ("a","b","c")
print(type(alpha_tuple))

#to prove that tuple can't be changed
try: #try something
	alpha_tuple[2] = "d"
except TypeError: #if a TypeError occur, do this
	print("We can't add elements to tuples!")
print(alpha_tuple)
        
