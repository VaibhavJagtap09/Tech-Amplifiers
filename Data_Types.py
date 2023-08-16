list = ['vaibhav jagtap', 12, 12.12, True, ['ABCD', 13, 13.13, False]] # we can store any type of data in list
print(list)
list.append('Jagtap')
print(list)
tuple = ('Vaibhav', 12, 12.12, True)
print(tuple)
dictionary = {
    "A" : "vaibhav",
    "B" : "sanjay",
    "C" : "jagtap",
    }
print(dictionary["C"] )     # printing elements in dictionary
dictionary["C"] = "JAGTAP"
print(dictionary["C"])
# operations on list
print(list.index(12.12))
list[1] = "VAIBHAV"     # asign existing element in list to another value
print(list)

# reverse list without inbuild function
# inbuilt function is list.reverse
print(list[::-1])