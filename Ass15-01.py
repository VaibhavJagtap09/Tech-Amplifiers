# abc.py
from abc import ABC, abstractmethod
class Principal(ABC):
    def __init__(self):
        print('Principal Constructor')

    def teaching_maths(self):
        pass

    def teaching_arts(self):
        pass

    def teaching_science(self):
        pass

    def teaching_eng(self):
        pass

    def administration(self):
        print("I am Principal and I have administrative authority")
