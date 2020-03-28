class Student:
    def __init__(self, name, age, major, gpa, is_on_prabation):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.is_on_prabation = is_on_prabation

    def print_name(self, sex):
        print("Hello: "+sex+" -> ",self.name)