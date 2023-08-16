# # using UDF
# def table(a):
#     if a % 17 == 0:
#         print(f'{a} is divisible by 17')
#     else:
#         print(f'{a} is not divisible by 17')
# table(90)
#
# a = lambda x:x%17==0
# print(a(56))
#
# def div(n):
#     return lambda a:a%n==0
# x = div(10)
# print(f'{140} is divisible by 10', x(140))
# y = div(13)
# print(f'{2334} is divisible by 13',y(2334))
#
# #map and filter function
# age = [20, 23, 34 ,21, 33,27, 26]
# print(list(filter(lambda a:a<25, age)))
#
# # program to find summation of given numbers of given numbers in list
# lis = [20,25,21,30,24,23,27]    # summation of first 20 no , first 25 no, first 21 no, first 30 no ....
# print(list(map(lambda n: n*(n+1)/2 , lis)))     # n*(n+1)/2 formula for summation
#
# print(list(filter(lambda a: a>= 350, list(map(lambda n: n*(n+1)/2 , lis)))))    # pragram to find summation greater than 350
#
# list1 = [20,25,21,30,25,23,27,235,652,984,25]
# print(list(filter(lambda n : n != 625, list(map(lambda n : n**2, list1)))))
# print(list(map(lambda n:n if n != 625 else 0, list(map(lambda n : n**2, list1)))))
#
# Prime_series=()
#
# number = int(input("Enter the input Range : "))
# is_prime = lambda number: all( number%i != 0 for i in range(2, int(number**.5)+1) )
# print(is_prime)

# Write a Python program to find numbers divisible by 19 or 23 from a list of numbers using Lambda.
List12 = [22, 38, 19, 65, 57, 39, 152, 621, 161, 44, 90, 190]
print("Numbers divisible by 19 and 23 are: ",type(filter(lambda x: x%19==0 or x%23==0, List12)))

