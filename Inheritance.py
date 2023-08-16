class Father:
    def __int__(self):
        self.name = 'Father'
        self.a = 10
        print('Father constructor')

    def teacher_maths(self):
        school_name = 2*self.a
        return school_name

class Son(Father):
    def __init__(self):
        super().__init__()
        self.name = 'Son'
        print('son constructor')

    def teacher_python(self):
        institute_name = 'Tech amplifiers'
        return institute_name


s = Son()
s.teacher_python()
print(s.teacher_python())