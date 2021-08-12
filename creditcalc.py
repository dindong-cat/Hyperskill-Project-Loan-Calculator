import argparse
import math
cal = argparse.ArgumentParser(description = "You can use it to calculate a convenient interest rate and your payment needed.")
cal.add_argument("--type", help = 'Select your type of payment. "Diff" means "differentiated".')
cal.add_argument("--payment", help = "It is the monthly payment amount. Only --type annuity will need to enter this. Since For diff, the payment is different each month, so we can't calculate months or principal.")
cal.add_argument("--principal", help = "It is used for calculations of both types of payment. You can get its value if you know the interest, annuity payment, and number of months.")
cal.add_argument("--periods", help = "denotes the number of months needed to repay the loan. It's calculated based on the interest, annuity payment, and principal.")
cal.add_argument("--interest", help = "It is specified without a percent sign. Note that it can accept a floating-point value. Our loan calculator can't calculate the interest, so it must always be provided.")

factors = cal.parse_args()
detail = [factors.type, factors.payment, factors.principal, factors.periods, factors.interest]

def loan_calculator(detail):
    detail = [factors.type, factors.payment, factors.principal, factors.periods, factors.interest]
    detail = [float(i) if str(i).isdecimal() == True else i for i in detail]
    detail = [float(i) if (i != None and i != ("diff") and i != "annuity") else i for i in detail]
    if detail[0] != ("diff") and detail[0] != ("annuity") or detail[0] is None:
        print("Incorrect parameters")
    elif detail[0] == "diff" and detail[1] is not None:
        print("Incorrect parameters")
    elif detail[4] == None:
        print("Incorrect parameters")
    elif sum(i == None for i in detail) > 1:
        print("Incorrect parameters")
    elif detail[2] != None and detail[3] != None and (detail[2] < 0 or detail[3] < 0 or detail[4] < 0):
        print("Incorrect parameters")
    else:
        if detail[0] == "diff":
            calc_one(detail)
        elif detail[0] == "annuity" and factors.payment == None:
            calc_two(detail)
        elif detail[0] == "annuity" and factors.principal == None:
            calc_three(detail)
        elif factors.type == "annuity" and factors.periods == None:
            calc_four(detail)

def calc_one(detail):
    total_payment = 0
    interest = float(factors.interest) / 12 / 100
    for i in range(1, int(detail[3]) + 1):
        payment = math.ceil((int(detail[2]) / int(detail[3])) + interest * (int(detail[2]) - (int(detail[2]) * (i - 1)) / int(detail[3])))
        total_payment += payment
        print(f"Month {i}: payment is {payment}")
    print()
    print(f"Overpayment = {total_payment - int(detail[2])}")


def calc_two(detail):
    # detail = [factors.type, factors.payment, factors.principal, factors.periods, factors.interest]
    interest = float(factors.interest) / 12 / 100
    payment = math.ceil(int(factors.principal) * ((interest * math.pow(1 + interest, int(factors.periods))) / (math.pow(1 + interest, int(factors.periods)) - 1)))
    overpayment = payment * int(factors.periods) - int(factors.principal)
    print(f"Your annuity payment = {payment}!")
    print(f"Overpayment = {overpayment}")


def calc_three(detail):
    # detail = [factors.type, factors.payment, factors.principal, factors.periods, factors.interest]
    payment = detail[1]
    interest = detail[-1] / 12 / 100
    period = detail[3]
    principal = math.ceil(payment / ((interest * math.pow(1 + interest, period)) / (math.pow(1 + interest, period) - 1)))
    overpayment = abs(payment / ((interest * math.pow(1 + interest, period)) / (math.pow(1 + interest, period) - 1)) - (payment * period))
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {math.ceil(overpayment)}")
    return [overpayment, principal]


def calc_four(detail):
    # detail = [factors.type, factors.payment, factors.principal, factors.periods, factors.interest]
    factors.interest = float(factors.interest) / 12 / 100
    number_of_months = math.ceil(math.log(float(factors.payment) / (float(factors.payment) - float(factors.interest) * float(factors.principal)), float(factors.interest) + 1))
    if divmod(number_of_months, 12)[1] == 0:
        print(f"It will take {divmod(number_of_months, 12)[0]} years to repay this loan!")
    else:
        print(f"It will take {divmod(number_of_months, 12)[0]} years and {divmod(number_of_months, 12)[1]} months to repay this loan!")
    overpayment = number_of_months * float(factors.payment) - float(factors.principal)
    print(f"Overpayment = {math.ceil(overpayment)}")

loan_calculator(detail)
