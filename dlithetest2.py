N = int(input())
factors = []
for n in range(1,N + 1):
    if N % n == 0:
        factors.append(n)

print(*factors)