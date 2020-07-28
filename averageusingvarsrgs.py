#program to calculate average of list of values using function
def average(arg1, *values):
    total = arg1
    for value in values:
        total += value
    return total / (len(values) + 1)

def convert(value):
    return float(value) if value.find(".")!=-1 else int(value)

list1 = [convert(element) for element in input("Enter the values:").split()]
print("Average(",*list1, ")=", average(*list1))