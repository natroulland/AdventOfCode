pos = 50
ans1 = 0
ans2 = 0
with open("Day 1/input.txt") as f:
    for line in f:
        line = line.removesuffix("\n")
        way = line[0]
        number = int(line[1:])
        for i in range(number):
            if way == 'L':
                pos = (pos-1)%100
            else:
                pos = (pos+1)%100
            if pos == 0:
                ans2 += 1
        if pos == 0:
            ans1 += 1
print(ans1, ans2)