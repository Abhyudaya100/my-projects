P = int(input("Enter the principal or loan amount:"))
T = input("Enter the total tenure in years:")
T = float(T)
for i in range(0,2):
    N = int(input())
    sum = 0
    for n in range(0,N):
        x, I = [float(n) for n in input().split()]
        EMI = P*I/(1-(1/((1+I)**(x*12))))
        sum = sum + EMI
        if i == 0:
            bank1 = sum
        else :
            bank2 = sum
if bank1<bank2:
    print("bank A")
else:
    print("bank B")