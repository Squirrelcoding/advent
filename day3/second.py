def search(lines):
    sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            # Search in the up direction
            if i >= 3:
                chars = [lines[i][j], lines[i-1][j], lines[i-2][j], lines[i-3][j]]
                if chars == ["X", "M", "A", "S"] or chars == ["S", "A", "M", "X"]:
                    sum += 1
            # Search right
            if j < len(lines[i]) - 4:
                chars = [lines[i][j], lines[i][j+1], lines[i][j+2], lines[i][j+3]]
                if chars == ["X", "M", "A", "S"] or chars == ["S", "A", "M", "X"]:
                    sum += 1

            # Search diagonal right-down
            if 3 <= i and 3 <= j:
                chars = [lines[i][j], lines[i-1][j-1], lines[i-2][j-2], lines[i-3][j-3]]
                if chars == ["X", "M", "A", "S"] or chars == ["S", "A", "M", "X"]:
                    sum += 1

            # Search diagonal right-up
            if j < len(lines[i]) - 4 and 3 <= i:
                chars = [lines[i][j], lines[i-1][j+1], lines[i-2][j+2], lines[i-3][j+3]]
                if chars == ["X", "M", "A", "S"] or chars == ["S", "A", "M", "X"]:
                    sum += 1
    return sum

with open("input.txt", "r") as file:
    lines = file.readlines()
    print(search(lines))
