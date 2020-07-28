basic_salary = float(input())
DA = 0.25 * basic_salary
HRA = 0.15 * basic_salary
gross_salary = basic_salary +DA + HRA
provident_fund = 0.1 * gross_salary
Net_salary = gross_salary - provident_fund
print(round(Net_salary,2))