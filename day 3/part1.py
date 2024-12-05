import re

file1 = open("input", "r")

text = file1.read()

x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", text)
sum = 0
for entry in x:
    numbers = re.findall("[0-9]{1,3}", entry)
    sum += int(numbers[0]) * int(numbers[1])
print(sum)