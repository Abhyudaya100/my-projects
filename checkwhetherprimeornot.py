num = int(input("Enter a number:"))
factor = 0
if(num==1):
    print("neither prime nor composite")
    exit(0)
for factor in range(1,num+1):
    if num % factor == 0:
        factor+=1
if factor ==2:
    print("prime")
else:
    print("not prime")