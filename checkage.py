def employee_info(**kwargs):
    for key,value in kwargs.items():
        if key == "age" and value < 18 :
            raise ValueError("Not Eligible")
        print(key,"=",value)
try:
    employee_info(name= "Abhyudaya", age = 21, salary = 100000)
    employee_info(name = "S",age = 16, salary = 200000)
except ValueError as error:
    print(error)

print("Thank you")