#Inbuilt functions in python for String
String  = 'I love PYTHon prograMMIng LanguagE'
print(String.upper()) #All capital
print(String.capitalize())#1st letter capital
print(String.lower())#All lower
print(String.title())#1st letter of each word capital

#Using inbuilt functions while taking inputs
name  = input("Enter your name: ").upper()
mailID = input("Enter your mail ID: ").lower()
print(name, mailID)
#Checks if string is in upper or not
print(name.isupper())
#Checks if string is lower or
print(mailID.islower())
#print(name[starting_index:ending_index:steps])
print(name[0:7:1])#print elemenst in string form index 0 to 7 while skipping 1 step
print(name[::-1])#Prints string in reverse order 