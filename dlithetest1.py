'''
num = int(input())
binary = bin(num)
print(binary[2:])
'''

num = int(input())
y = []
while num>0:
    x = num % 2
    y.append(x)
    num = num//2
z = y[::-1]
print(*z,sep='')