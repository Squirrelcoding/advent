import re

with open("input.txt", "r") as file:
    s = file.read().rstrip()
    #matches = regex.findall(r"mul\([0-9]+,[0-9]+\)", s)  
    mul_matches = [(match.start(), match.end()) for match in re.finditer(r"mul\([0-9]+,[0-9]+\)", s)]
    d_matches = [(match.start(), match.end()) for match in re.finditer(r"\b(?:do|don't)\b", s)]
    sum = 0
    
    for match in mul_matches:
        # Find the most recent ending index of the d_matches
        most_recent_d = d_matches[0]
        i = 0

        # While the end of the most recent D word is before our MUL word 
        while most_recent_d[1] < match[0] and i < len(d_matches):
            # If the start of the latest D word appears after our word, end
            if d_matches[i][0] >= match[0]:
                break
            most_recent_d = d_matches[i]
            i += 1

        most_recent_mul = mul_matches[0]
        j = 0
        while most_recent_mul[1] < match[0] and j < len(mul_matches):
            if mul_matches[j][0] >= match[0]:
                break
            most_recent_mul = mul_matches[j]
            j += 1

        # If there are no MUL's between the most recent DO/DON and match
        print(f"We have {s[most_recent_d[0]:most_recent_mul[1]]}")
        if s[most_recent_d[0]:most_recent_d[1]] == "do":
            print("It's a do!")
            string_nums = s[match[0]+4:match[1]-1].split(",")
            nums = [int(x) for x in string_nums]
            sum += nums[0] * nums[1]
        else:
            print("It's a don't :(")


    print(sum)

        # If there's no word:
            # If it's a do:
                # Add
            # Else:
                # Don't add
