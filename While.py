# execute block of code multiple time
i = 1
while i<=4:
    print(i)
    i += 1
print("Finish")
count = 0
check = True
rep = "Guy"
ques = ""
while ques != rep and check:
    ques = input("Entrer la rep : ")
    count += 1
    if count == 3:
        check = False
        print("You loose")
