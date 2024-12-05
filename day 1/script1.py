file1 = open("input", "r")

text = file1.read()

list1 = []
list2 = []
for line in text.split("\n"):
    p = line.split(" ")
    if len(p) < 4:
        break
    list1.append(p[0])
    list2.append(p[3])

distance = 0
for i in range(len(list1)):
    smallest1 = min(list1)
    smallest2 = min(list2)
    distance += abs(int(smallest1) - int(smallest2))
    list1.remove(smallest1)
    list2.remove(smallest2)
print(distance)