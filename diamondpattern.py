'''
1234512345
1234  1234
123    123
12      12
1        1
1        1
12      12
123    123
1234  1234
1234512345
'''
n = int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end = "")
    print(" " * 2* (n-i),end="")
    for j in range(1,i+1):
        print(j,end = "")
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end = "")
    print(" " * 2* (n-i),end="")
    for j in range(1,i+1):
        print(j,end = "")
    print()