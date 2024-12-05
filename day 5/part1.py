import itertools


def findsubsets(s, n):
    return list(itertools.combinations(s, n))

def isUpdateCorrect(update, rules):
    for pair1, pair2 in findsubsets(update, 2):
        for rule1, rule2 in rules:
            if pair2 == rule1 and pair1 == rule2:
                return False
    return True


file1 = open("input", "r")

rules = []
updates = []
for line in file1.readlines():
    line = line.strip()
    if len(line) == 5:
        line = line.split("|")
        rules.append([int(line[0]), int(line[1])])
    elif 1 < len(line):
        array = []
        line = line.split(",")
        for i in line:
            array.append(int(i))
        if len(array) > 0:
            updates.append(array)
correctUpdates = []
for update in updates:
    if isUpdateCorrect(update, rules):
        correctUpdates.append(update)

sum = 0

for update in correctUpdates:
    middle = update[len(update) // 2]
    sum += middle
print(sum)