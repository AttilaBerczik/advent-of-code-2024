import itertools
import random

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
wrongUpdates = []

for update in updates:
    if not isUpdateCorrect(update, rules):
        wrongUpdates.append(update)
print(wrongUpdates)
correctUpdates = []
for update in wrongUpdates:
    new = []
    for i in update:
        placed = False
        while not placed:
            position = random.randint(0, len(new))
            new.insert(position, i)
            if isUpdateCorrect(new, rules):
                placed = True
            else:
                new.pop(position)
    print(new)
    correctUpdates.append(new)

sum = 0

for update in correctUpdates:
    middle = update[len(update) // 2]
    sum += middle
print(sum)