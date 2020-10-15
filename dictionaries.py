#define a dictionary data structure

#dictionaries have a key : value pair for elements
example_dict = {
	"class":"Astr 119",
	"prof":"Brant",
	"awesomeness":10
}
print(type(example_dict))

#get a value using a key
course = example_dict["class"]
print(course)

#change a value using a key 
example_dict["awesomeness"]+=1
print(example_dict)

#print element by element using a for loop
for x in example_dict.keys():
	print(x,example_dict[x])