first_column = []
second_column = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        words = line.strip().split()
        first_column.append(words[0])
        second_column.append(words[1])

sum = 0
first_column = [int(n) for n in first_column]
second_column = [int(n) for n in second_column]

for i in range(1000):
    first_min = min(first_column)
    first_index = first_column.index(first_min)
    first_column.pop(first_index)
    second_min = min(second_column)
    second_index = second_column.index(second_min)
    second_column.pop(second_index)
    sum += abs(first_min - second_min) 
print(sum)
