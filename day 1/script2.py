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

similarity = 0
for i in range(len(list1)):
    current = list1[i]
    count = 0
    for j in list2:
        print(i, j)
        if int(current) == int(j):
            count += 1
    similarity += int(current) * count
print(similarity)