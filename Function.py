def say_h(name = "no one"):
    print("HELLO "+ name)

say_h("Guy")

female = False
male = True
if male and female:
    print("Impossible")
elif not female and male:
    print("Male")

nb1 = float(input("1st number please: "))
op = input("Operator: ")
nb2 = float(input("2nd number please: "))

if op == "+":
    print("Somme  = "+ str(nb1 + nb2))
else:
    print("Invalid op")


