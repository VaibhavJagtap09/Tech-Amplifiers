# abc.py
from abc import ABC, abstractmethod
class Father(ABC):          # Abstract base class
    def __init__(self):
        print('Father constructor')

    @abstractmethod
    def teacher(self):      # Abstract method
        pass

class Son(Father):
    def __init__(self):
        super().__init__()
        print('Son constructor')

    def teacher_python(self):
        print('teaching python....')


class Vaibhav(Son):
    def __init__(self):
        super().__init__()
        print('Vaibhav constructor')

    def teacher(self):
        print('teaching maths....')

class Mitali(Son):
    def __init__(self):
        super().__init__()
        print('Mitali constructor')

    def teacher(self):
        print('teaching english')

# B = Son()
# print(B.teacher_())
try:
    V = Vaibhav()
    print(V.teacher_python(), V.teacher())
except:
    print('Can not instantiate abstract class Vaibhav with abstract method teacher ')
else:
    M = Mitali()        # we can use abstracted method in different objects
    print(M.teacher())
finally:
    print('teaching....')

