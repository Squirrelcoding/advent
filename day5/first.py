def get_minimal_element(rules):
    set2 = set([b for (_, b) in rules])
    
    for element in [a for (a, _) in rules]:
        if element not in set2:
            return element

def solution(rules):
    s = {}
    while rules:
        minimal_element = get_minimal_element(rules)
        i = 0
        while i < len(rules):
            if rules[i][0] == minimal_element:
                if minimal_element not in s:
                    s[minimal_element] = {rules[i][1]}
                s[minimal_element].add(rules[i][1])
                rules.pop(i)
            else:
                i += 1

    return [key for key in s.keys()]



with open("input.txt", "r") as file:
    lines = file.readlines()
    updates = lines[23:]

    rules = []

    # Determine which lines are already in the right order and remove them from the list
    for i in range(21):
        a, b = lines[i].split("|")
        a, b = int(a), int(b)
        rules.append((a,b))
    for update in updates:
        pass
