num = int(input("Enter a number:"))
if num == 1:
    print("neither composite nor prime")
else:
    for factor in range(2,num):
        if num%factor == 0:
            print("not prime")
            exit(0)
    print("prime")