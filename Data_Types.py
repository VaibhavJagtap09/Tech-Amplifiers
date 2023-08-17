# List
list = ['vaibhav jagtap', 12, 12.12, True, ['ABCD', 13, 13.13, False]] # we can store any type of data in list
print(list)

# operations on list
list.append('Jagtap')
print(list)
print(list.index(12.12))
list[1] = "VAIBHAV"     # asign existing element in list to another value
print(list)
# reverse list without inbuild function
# inbuilt function is list.reverse
print(list[::-1])

# Tuple
tuple = (10, 12, 12.12, 34, 10)
print(tuple)
print(len(tuple))# length of tuple
print(max(tuple))# max element in tuple
print(min(tuple))# min element in tuple 
print(sorted(tuple))#sorts tuple
print(tuple[::-1])#prints reversed order in new tuple
print(tuple.count(10))#occurance of element
print(tuple.index(10))#give index of 1st occurance of element


# Dictionary
dictionary = {
    "A" : "Element1",
    "B" : "Element2",
    "C" : "Element3",
    "D" : "Element4",
    }
print(dictionary["C"] )     # printing elements in dictionary
dictionary["C"] = "ELEMENT3"  # changing values of elements in dictionary
print(dictionary["C"])
# Print keys in dictionary
for key in dictionary.keys():
    print(dictionary.get("key"))
# Print values in dictionary
for A in dictionary.values():
    print(A)
# Print both
for A,B in dictionary.items():
    print(A,":", B)
# Prints all key value pair
for i in dictionary.keys():
    print("Key : ",i," Value: ",dictionary[i])
#Get value associated to perticular key
print(dictionary.get("A"))
