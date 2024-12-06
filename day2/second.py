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

def is_super_safe(report):
    l = len(report)

    if is_safe(report):
        print(f"{report} is already safe.")
        return True

    for i in range(l):
        print(f"Checking {report[:i] + report[i+1:]} in {report} by removing {report[i]}")
        if is_safe(report[:i] + report[i+1:]):
            print(f"{report[:i] + report[i+1:]} is safe {report} by removing {report[i]}")
            return True
    return False

with open("input.txt", "r") as file:
    for line in file.readlines():
        nums = line.split()
        nums = [int(n) for n in nums]
        reports.append(nums)
sum = 0
for report in reports:
    if is_super_safe(report):
        sum += 1
    else:
        print(f"{report} is not safe.")
print(sum)
