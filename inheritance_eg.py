class Animal:
    def __init__(self):
        self.name = 'Animal'
        print('I am an Animal')

    def characteristics(self):
        legs = 4
        tail = 1
        return legs, tail
class Petanimal(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Pet Animal'
        print('I am a pet')

    def char(self):
        living = 'Pet by Humans'
        food = 'depends on humans'
class Wildanimals(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Wild Animal'
        print('I am Wild animal')

    def char(self):
        living = 'Lives independent of humans'
        food = 'depends on Nature'
class echosystem(Petanimal, Wildanimals, Animal):
    def __init__(self):
        super().__init__()
        self.n = 'Echo-System'
        print('This is an Echosystem')

    def elements(self):
        print('This echosystem consists of', Petanimal, Wildanimals, 'and plants also.')

# Method Overriding
class Humans(Animal):
    def __init__(self):
        super().__init__()
        print('I am a Human')

    def characteristics(self):
        legs = 2
        hands = 2
        tail = 'None'
        return legs, hands, tail

C = Humans()
print(C.characteristics())
