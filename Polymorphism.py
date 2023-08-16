# poly = many & morphism = forms
# method overloading
# same name and different parameters/arguments

class Addition:
    def __init__(self):
        print('I am a constructor')

    def add(self, a, b):        # This method is not even considered due to 2 parameters/arguments
        print('2')
        return a + b

    def add(self, a, b, c = 10):
        print('3')
        return  a + b + c

A = Addition()
print(A.add(12, 13, 14))
print(A.add(15,16))

# method overriding
# same name and same parameters
# it occours within inheritance

class Father:
    def __init__(self):
        print('Father constructor')

    def teacher(self):
        print('teaching Maths')

class Son(Father):
    def __init__(self):
        super().__init__()
        print('Son constructor')

    def teacher(self):
        print('teaching python....')

B = Son()
print(B.teacher())

