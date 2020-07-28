code = str(input("Enter the code:"))
x = int(input("if encode, enter 1 , if decode , enter 2:"))
if x ==1:
    n = 0
    for char in code:
        n = ord(char)
        if n == 88:
            n = 65
        elif n == 89:
            n = 66
        elif n == 90:
            n = 67
        elif n == 120:
            n = 97
        elif n == 121:
            n = 98
        elif n == 122:
            n = 99
        elif n == 32:
            n = 32
        else:
            n += 3
        n = chr(n)
        print(n,end="")
else:
    n = 0
    for char in code:
        n = ord(char)
        if n == 65:
            n = 88
        elif n == 66:
            n = 89
        elif n == 67:
            n = 90
        elif n == 97:
            n = 120
        elif n == 98:
            n = 121
        elif n == 99:
            n = 122
        elif n==32:
            n=32
        else:
            n -= 3
        n = chr(n)
        print(n, end="")