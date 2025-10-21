class glass:
    def __init__(self, contents, size):
        self.contents = contents
        self.size = size
    def __str__(self):
        return str(int(self.contents))
    def __repr__(self):
        return str(self.contents)

glass_1 = glass(8, 8)
glass_2 = glass(0, 5)
glass_3 = glass(0, 3)

tree = [[[glass_1.contents, glass_2.contents, glass_3.contents]]]
combinations = [[glass_1.contents, glass_2.contents, glass_3.contents]]

def pour(from_glass, to_glass):
    total_contents = from_glass.contents + to_glass.contents
    if total_contents > to_glass.size:
        to_glass.contents = to_glass.size
        from_glass.contents = total_contents - to_glass.size
    else:
        to_glass.contents = total_contents
        from_glass.contents = 0
    
def record_state(inp):
    branch = []
    for x in inp:
        if x not in combinations:
            combinations.append(x)
            branch.append(x)
    tree.append(branch)

def mix(tree):
    com = []
    branch = tree[-1]
    try:
        for x in branch:
            glass_1 = glass(x[0], 8)
            glass_2 = glass(x[1], 5)
            glass_3 = glass(x[2], 3)
    except:
        glass_1 = glass(branch[0], 8)
        glass_2 = glass(branch[1], 5)
        glass_3 = glass(branch[2], 3)
        actions = [(glass_1, glass_2), (glass_1, glass_3), (glass_2, glass_1), (glass_2, glass_3), (glass_3, glass_1), (glass_3, glass_2)]
        for from_glass, to_glass in actions:
            pour(from_glass, to_glass)
            com.append([glass_1.contents, glass_2.contents, glass_3.contents])
        print(com)
    record_state(com)
mix(combinations)
print(combinations)
print(tree)