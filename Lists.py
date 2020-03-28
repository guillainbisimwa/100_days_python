friends = ["K", "G", "Jazmin"]
nbr = [1,3,5,8,2]
friends[0] = "Kevin"
friends.extend(nbr)
friends.append("Okay")
friends.insert(1,"Gustave")
friends.append(3)
friends.remove(1)
friends.pop()

print(friends)
print(friends.index(3))
print(friends.count("G"))
nbr.sort()
print(nbr)

