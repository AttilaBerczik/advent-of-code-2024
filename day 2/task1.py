file1 = open("input", "r")

def is_safe(array):
    for j in range(len(array)):
        if j == 0:
            continue
        if 3 >= array[j-1] - array[j] >= 1:
            if j == len(array) - 1:
                return True
            continue
        else:
            for j in range(len(array)):
                if j == 0:
                    continue
                if -3 <= array[j-1] - array[j] <= -1:
                    if j == len(array) - 1:
                        return True
                else:
                    return False

safe = 0
for line in file1.readlines():
    line = line.replace("\n", "")
    array = line.split(" ")
    for i in range(len(array)):
        array[i] = int(array[i])
    if is_safe(array):
        safe += 1
    else:
        for i in range(len(array)):
            new_array = array[:i] + array[i + 1:]
            if is_safe(new_array):
                safe += 1
                break

print(safe)
