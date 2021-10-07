



def pay_for_the_week():
    hours_worked = float(input("How many hours did you work?: "))
    standard_work_week = 40
    pay_rate = 7.25
    overtime_pay_multiplier = 1.5
    sum = hours_worked * pay_rate
    overtime_pay_rate = pay_rate * overtime_pay_multiplier
    if hours_worked > standard_work_week:
        overtime_hours = hours_worked - standard_work_week
        pay = (overtime_hours * overtime_pay_rate) + sum
        print(pay)
    elif hours_worked <= standard_work_week:
        pay = sum
        print(pay)

# pay_for_the_week()



