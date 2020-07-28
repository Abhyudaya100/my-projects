#ascii
#A-Z : 64-90
#a-z : 97
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end = "")
    print()