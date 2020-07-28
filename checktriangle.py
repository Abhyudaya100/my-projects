'''
Write a Python program to check a triangle is equilateral, isosceles or scalene.
Note : An equilateral triangle is a triangle in which all three sides are equal. A scalene triangle is a triangle that has three unequal sides. An isosceles triangle is a triangle with (at least) two equal sides.

Input:
x: 3
y: 3
z: 3

Output:
Equilateral triangle
'''
x = input("x:")
y = input("y:")
z = input("z:")
x,y,z = int(x), int(y), int(z)

if x==y==z:
    print("Equilateral triangle")
elif x==y or y==z or x==z:
    print("Isosceles triangle")
else:
    print("Scalene triangle")