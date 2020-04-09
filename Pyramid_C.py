empty = " "
stars = "*"

x = 11
es = 1
div2 = (x-1) /2
div = (x-1) /2
while div >= 0:
    #for x in range(1, int(div)):
   
    print(stars*int(es) + empty *(int(div)))
    es +=1
    div -= 1