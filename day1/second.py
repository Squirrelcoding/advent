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

for num in first_column:
    sum += num * second_column.count(num)

#for num in second_column:
#    sum += num * first_column.count(num)

print(sum)
