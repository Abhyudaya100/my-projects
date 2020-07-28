S = input()
T = []
sum = 0
for s in S:
    if s.isdigit():
        T.append(int(s))

for t in T:
    sum = sum + t

print(sum)