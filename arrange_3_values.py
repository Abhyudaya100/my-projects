x,y,z = input("Enter 3 values :").split()
x,y,z = int(x), int(y), int(z)
if x>y:
    if y>z:
        print("Output\nmax>mid>min\n",x,">",y,">",z,)
        exit(0)
    else :
        if x>z:
            print("Output\nmax>mid>min\n",x,">",z,">",y)
            exit(0)
        else :
            print("Output\nmax>mid>min\n", z,">", x,">", y)
            exit(0)
else :
    if x > z:
        print("Output\nmax>mid>min\n", y,">", x,">", z)
        exit(0)
    else:
        if y > z:
            print("Output\nmax>mid>min\n", y,">", z,">", x)
            exit(0)
        else:
            print("Output\nmax>mid>min\n", z,">", y,">", x)
            exit(0)