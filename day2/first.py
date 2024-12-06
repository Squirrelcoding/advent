import math

reports = []

def is_safe(report):
    l = len(report)

    # If decreasing
    if report[l-1] < report[0]:
        for i in range(l-1):
            if report[i + 1] >= report[i]:
                return False
    elif report[l-1] > report[0]:
        for i in range(l-1):
            if report[i + 1] <= report[i]:
                return False
    else:
        return False
    for i in range(l-1):
        if abs(report[i+1] - report[i]) > 3:
            return False
    return True

with open("input.txt", "r") as file:
    for line in file.readlines():
        nums = line.split()
        nums = [int(n) for n in nums]
        reports.append(nums)


sum = 0
for report in reports:
    if is_safe(report):
        print(f"{report} is safe.")
        sum += 1
    else:
        print(f"{report} is not safe.")
print(sum)
