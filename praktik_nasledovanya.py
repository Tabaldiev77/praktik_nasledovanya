
class Person:
    def __init__(self, last_name, firs_name, age, height):
        self.last_name = last_name
        self.firs_name = firs_name
        self.age = age
        self.height = height

    def get_class(self):
        return f'\nlast_name = {self.last_name}\nfirs_name = {self.firs_name}\nage = {self.age}\nheight = {self.height}'

class Children(Person):
    def __init__(self, last_name, firs_name, age, height, hair):
        super(Children, self).__init__(last_name, firs_name, age, height)
        self.hair = hair


    def get_class(self):
      return f'\nlast_name = {self.last_name}\nfirs_name = {self.firs_name}\nage = {self.age}\nheight = {self.height}\nhair = {self.hair}'

#

obj = Children('Ali','Alibekov','10','145',True)
print(obj.get_class())