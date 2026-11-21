
def hra(basic):
    hra = basic * 20 / 100
    return hra


def da(basic):
    da = basic * 10 / 100
    return da


def calculate_gross(basic, hra, da):
    gross = basic + hra + da
    return gross


name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
basic = float(input("Enter basic salary: "))

hra = hra(basic)
da =  da(basic)
gross = calculate_gross(basic, hra, da)


print("\n------ SALARY DETAILS ------")
print("Employee:", name)
print("Employee ID:", emp_id)
print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross)