import re

file1 = open("input", "r")

text = file1.read()

on = True
last7chars = "xxxxxxx"
newText = ""
for char in text:
    last7chars = last7chars[1:] + char
    if last7chars == "don't()":
        on = False
    elif last7chars[3:] == "do()":
        on = True
    if on:
        newText += char

x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", newText)
sum = 0
for entry in x:
    numbers = re.findall("[0-9]{1,3}", entry)
    sum += int(numbers[0]) * int(numbers[1])
print(sum)