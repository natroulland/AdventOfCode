import textwrap
ans = 0

with open('Day 2/input.txt') as f:
    ranges = f.read().split(",")
    for r in ranges:
        n = r.split("-")
        for i in range(int(n[0]), int(n[1])):
            st = str(i)
            length = len(st)
            for x in range(1, len(st)):
                if(length%x ==0):
                    parts = textwrap.wrap(st, x)
                    if(parts.count(parts[0]) == len(parts)):
                        ans += i
                        break
    print(ans)