# # forloop
# # for loop is only used in iterable datatypes
# for i in range(0 , 10):
#     print(i)
#
# lst = [12,13,14,15,16,17,18,19,20]      # list is iterable
# for element in lst:
#     print(element*5)
#
#
# string1 = 'vaibhav sanjay jagtap'       #string is iterable
# for a in string1:
#     print(a)
#
# tuple1 = {True, False, 12.12, 36, 'Vaibhav'}        # tuple is iterable
# for b in tuple1:
#     print(b)
#
# dictionary = {                      # dictionary is also iterable
#     'key1' : 12,
#     'key2' : 13,
#     'key3' : 14,
#     'key4' : 15
# }
# for c in dictionary:
#     print(dictionary[c])
l = ['vaibhav']
while True:
    name = input("Enter your name: ").capitalize()
    if name in l:
        print("Welcome")
    else:
        print("You are not in list")
        admin_opinion = input(f'{name} wants to join classroom but not in list should we add or not(yes/no)')
        if admin_opinion == 'yes':
            l.append(name)
            print("you are allowed in classroom")
            print(l)
        else:
            print("you are not allowed in classroom")
