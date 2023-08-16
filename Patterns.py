# # # 1st try with while loop
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 2, 3, 4]
# [1, 2, 3, 4, 5]
lst = []
i = 1
while i <= 5:
    lst.append(i)
    print(lst)
    i = i+1 
print("\n")

#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print("\n")


# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1, 6):
    for j in range(1, i+1):
        print('*' , end=' ')
    print()
print("\n")


# pattern with for loop
#         *
#        * *
#       * * *
#      * * * *
#     * * * * *
for i in range(1, 6):
    for k in range(6, i, -1):
        print(end=' ')
    for j in range(1, i+1):
        print('*', end=' ')
    print()
print("\n")


    #     1
    #    1 2
    #   1 2 3
    #  1 2 3 4
    # 1 2 3 4 5
for i in range(1, 6):
    for k in range(6, i, -1):
        print(end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print("\n")


# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5
for i in range(1, 6):
    for j in range(i, 6):
        print(j, end=' ')
    print()
print("\n")


# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(1, 6):
    for j in range(i, 6):
        print('*', end=' ')
    print()
print("\n")


  #         1
  #       1 2
  #     1 2 3
  #   1 2 3 4
  # 1 2 3 4 5
for i in range(1, 6):
    for k in range(6, i, -1):
        print(' ',end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print("\n")


# * * * * *
#  * * * *
#   * * *
#    * *
#     *
for i in range(1, 6):
    for k in range(1, i+1):
        print(end=' ')
    for j in range(i, 6):
        print('*', end=' ')
    print()
print("\n")


# 1 2 3 4 5
#   1 2 3 4
#     1 2 3
#       1 2
#         1
for i in range(6, 1, -1):
    for k in range(i, 6):
        print(' ', end=' ')
    for j in range(1, i):
        print(j, end=' ')
    print()
print("\n")


# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
for i in range(6, 1, -1):
    for j in range(1, i):
        print(j, end=' ')
    print()
print("\n")


#       1 
#      1 *     
#     1 * 3    
#    1 * 3 *   
#   1 * 3 * 5  
#  1 * 3 * 5 * 
#   1 * 3 * 5  
#    * 3 * 5   
#     3 * 5    
#      * 5     
#       5 

for i in range(1, 7):
    for k in range(7, i, -1):
        print(end=' ')
    for j in range(1, i+1):
        if j%2==0:
            print('*', end=' ');
        else:
            print(j, end=' ')
    print()

for i in range(1, 6):
    for k in range(1, i+2):
        print(end=' ')
    for j in range(i, 6):
        if j%2==0:
            print('*', end=' ')
        else:
            print(j, end=' ')
    print()
print("\n")
