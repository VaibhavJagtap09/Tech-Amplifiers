# # User Defined Functions
# # organized
# # reusable
# def counting():
#     count = 0
#     name = input("enter string: ")
#     check_char = input('enter the character to count: ')
#     for i in name:
#         if check_char == i:
#             count += 1
#     print(count)
#
# counting()

def prime_no():
    a = int(input('enter first no: '))
    b = int(input('enter last no: '))
    prime = []
    for num in range(a, b):
        if num%num == 0 and num%num+1 < 1:

            prime.append(num)
    print(prime)

prime_no()