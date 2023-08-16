# object-oriented programming
# object -  instance of class
# classes - blueprint of object
class Python:
    def __init__(self, name, age, college):
        self.name = name
        self.age = age
        self.college = college
        print('I am a constructor')

    def nm(self):
        print(self.name)
        self.name = 'girish'
        print(self.name)

    def ag(self):
        print(self.age)
        self.age = 24
        print(self.age)

    def clg(self):
        print(self.college)
        self.college = 'KBP'
        print(self.college)



A = Python('vaibhav', 21, 'DIET')
A.nm()
A.ag()
A.clg()

# class educational details     name, age, DOB, address, mob, email
# another class for personam details   clg, 10, 12 , graduation

class PersonalDetails:
    def __init__(self,name,age,dob,address,mob,email):
        self.name = name
        self.age = age
        self.dob = dob
        self.address = address
        self.mob = mob
        self.email = email

    def pd(self):
        print(f'My name is {self.name} My age is {self.age} and My date of birthdate is {self.dob}')

    def cd(self):
        print(f'My mobile No is {self.mob} and my mail id is {self.email}')

class EduDetails:
    def __init__(self,clg,tenth,twelfth,grad):
        self.clg = clg
        self.tenth = tenth
        self.twelfth = twelfth
        self.grad = grad

    def grades(self):
        print(f'I study in {self.clg}')
        print(f'My grades in tenth are {self.tenth} in twelfth are {self.twelfth} and in graduation are {self.grad}')

PD = PersonalDetails('vaibhav' , 21, 20.01, 'jyoti heights guruwar peth, satara' , 8329424745 , 'vsjagtap03@gmail.com')
PD.pd(), PD.cd()
ED = EduDetails('DIET', 86.50, 69.80,92.25)
ED.grades()

