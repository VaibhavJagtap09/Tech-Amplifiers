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
    "A" : "vaibhav",
    "B" : "sanjay",
    "C" : "jagtap",
    }
print(dictionary["C"] )     # printing elements in dictionary
dictionary["C"] = "JAGTAP"  # changing values of elements in dictionary
print(dictionary["C"])

