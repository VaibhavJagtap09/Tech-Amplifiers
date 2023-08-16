a = 10
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a/b)      # gives remainder as output
print(a%b)
print(a//b)
print(a**b)

# ternary operators
#WRC to find even odd numbers
# with normal code
a = 11
if a%2 == 0:
    print("even")
else:
    print("odd")
# with ternary operator
result = "even" if (a%2 == 0) else "odd"
print(result)    # ternary operator is useful only for single condition and not for multiple conditions


