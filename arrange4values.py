w,x,y,z = input("Enter 4 values :").split()
w,x,y,z = int(w), int(x), int(y), int(z)
largest = max(w,x,y,z)
smallest = min(w,x,y,z)
mid1 = min(max(w,x),max(y,z))
mid2 = max(min(w,x),min(y,z))

if mid1>mid2:
    print(largest,">",mid1,">",mid2,">",smallest)
else:
    print(largest, ">", mid2, ">", mid1, ">", smallest)
