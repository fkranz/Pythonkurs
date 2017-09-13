list = ['42', "What's the question", 1337, ["London", "England"], 3.1415, 3j-4]
print(list)
list.remove(3.1415)
print(list)
list.append(["Madrid", "Spain"])
list.extend(["Berlin", "Germany"])
print(list)
tup = tuple(list)
print(int(tup[0]) + tup[2])
