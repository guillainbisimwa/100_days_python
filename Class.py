from Student import Student
from Chef import Chef



student1 = Chef("Guillain", 28, "NTIC", 3.4, False)
student2 = Student("Eva", 25, "Business", 3.0, True)

print(student2.name)
student2.print_name("F")
student1.print_name("M")