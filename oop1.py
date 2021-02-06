import random
#super classes and inheritances

class School:
    def __init__(self, name, enrolled=True, **kwargs):
       self.name = name
       self.enrolled = enrolled

       for key, value in kwargs.items():
           setattr(self, key, value)
    
    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.name)


class Student(School):

    def __init__(self, name, enrolled=True, **kwargs):
      super().__init__(name, **kwargs)
      self.enrolled = enrolled

    def praise(self):
       print("Great job, {}!".format(self.name))

    def quiz(self, score):
       return self.enrolled and score >50

    def study(self):
       return self.enrolled and bool(random.randint(0,1))


#magic methods

# __str__ - Control how your instances turn into strings
# __int__ - Control int() conversion
# __init__ - Customize the initialization of your instances


class Grades:
    def __init__(self, value):
        self.value = str(value)
        
    def __str__(self):
        return self.value
    
    def __int__(self):
        return int(self.value)
    
    def __float__(self):
        return float(self.value)
    
    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        self.value = self + other
        return self.value
    
    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other

    def __rmul__(self, other):
        return self * other
    
    def __imul__(self, other):
        self.value = self * other
        return self.value




    



