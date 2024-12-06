def search(lines):
    sum = 0
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            chars = []
            chars.append(lines[i][j])
            chars.append(lines[i+1][j+1])
            chars.append(lines[i+1][j-1])
            chars.append(lines[i-1][j+1])
            chars.append(lines[i-1][j-1])
            if chars[0] == "A": 
                if chars[1] == chars[2]:
                    if chars[1] == "M":
                        if (chars[3] == chars[4]) and (chars[3] == "S"):
                            sum += 1
                    if chars[1] == "S":
                        if (chars[3] == chars[4]) and (chars[3] == "M"):
                            sum += 1
                if chars[2] == chars[4]:
                    if chars[2] == "M":
                        if (chars[1] == chars[3]) and (chars[1] == "S"):
                            sum += 1
                    if chars[2] == "S":
                        if (chars[1] == chars[3]) and (chars[1] == "M"):
                            sum += 1
    return sum
with open("input.txt", "r") as file:
    lines = file.readlines()
    print(search(lines))
