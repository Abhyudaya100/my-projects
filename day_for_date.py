'''
Write a python program to display day of the date.

input 0
8/7/2020

output 0
Wednesday

input 1
29/2/2019

output 1
Invalid

'''
d,m,y = input("Enter date :").split("/")
yy = int(y[2:])
year = int(y[:2])
d,m,y = int(d), int(m), int(y)
if y>2400 or y<1700 or m>12 or m<1 or d>31 or d<1:
    print("invalid date")

if y%4 not in [0] and m == 2 and d == 29:
    print("invalid")
    exit(0)
y_code = int((yy + (yy//4))%7)

if m in [1,10]:
    m_code = 0
elif m in [2,3,11]:
    m_code = 3
elif m in [4,7]:
    m_code = 6
elif m in [5]:
    m_code = 1
elif m in [6]:
    m_code = 4
elif m in [8]:
    m_code = 2
elif m in [9,12]:
    m_code = 5
else :
    print("invalid month")

if year == 17 or year == 21:
    c_code = 4
elif year == 18 or year ==22:
    c_code = 2
elif year == 19 or year == 23:
    c_code = 0
elif year == 20 or year == 24:
    c_code = 6
else:
    print("out of order")

if y % 4 ==0 and y%100 !=0:
    l_code = 0
else:
    l_code = 1
if m in [1,3,4,5,6,7,8,9,10,11,12]:
    x = (y_code + m_code + c_code + d - l_code)%7
else:
    x = (y_code + m_code + c_code + d - l_code) % 7 -1

if x == 0:
    print("day = sunday")
elif x ==1:
    print("day = monday")
elif x ==2:
    print("day = tuesday")
elif x ==3:
    print("day = wednesday")
elif x ==4:
    print("day = thursday")
elif x ==5:
    print("day = friday")
else:
    print("day = saturday")

