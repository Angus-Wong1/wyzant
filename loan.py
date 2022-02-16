"""
Question 3
"""
#3.1
def total(principal, rate, monthly_payment):
    """
    This function finds the total cost of a loan
    In order to us this function all of the payment amounts have to be the same.
    First, this function calculates number of payments you need.
    Then multiplies monthly payment with number of payments to calculate the total amount you willpay back to the bank.
    Principal is the amount you borrow.
    Rate is the yearly interest rate of the month
    Monthly_payment is the fixed amount you pay everymonth
    """
    number_of_payments = 0
    while  principal > 0:
        principal = principal * (1 + rate/12) - monthly_payment
        number_of_payments += 1
    print("The total amount you need to pay is $", number_of_payments * monthly_payment, "and you will pay the loan for", number_of_payments, "months")
# total(30000, 0.035, 545.75)

#3.2
def total_2(principal, rate, monthly_payment, first_12_months_payments):
    """
    This function finds the total cost of the loan
    Principal is the amount you borrow.
    Rate is the yearly interest rate of the month
    Monthly_payment is the fixed amount you pay everymonth
    First_12_month_payments is the extra payment you mamke for the first 12 months
    """
    number_of_payments = 0 #Total number of payments
    totalpayment1 = 0 #Payments for the first 12 months
    totalpayment2 = 0 #Payments for the rest 
    number_of_payments_after12 = 0 #Number of months after first 12 months
    while  principal > 0:
        if number_of_payments < 12:
            principal = principal * (1 + rate/12) - monthly_payment - first_12_months_payments
            number_of_payments += 1
            totalpayment1 = number_of_payments * (monthly_payment + first_12_months_payments)
        else:
            principal = principal * (1 + rate/12) - monthly_payment
            number_of_payments += 1
            number_of_payments_after12 += 1
            totalpayment2 = number_of_payments_after12 * monthly_payment
    print("With the extra payment of $", first_12_months_payments, "for 12 months, the total amount you need to pay is $",totalpayment1 + totalpayment2, "and you will pay the loan for", number_of_payments, "months")
# total_2(30000, 0.035, 545.75, 200)

#3.3
def total_3(principal, rate, monthly_payment, extra_payment, extra_payment_start, extra_payment_end):
    """
    """
    number_of_payments = 1 #Total number of payments
    number_of_payments_include_extra = 0 #Total number of payments with extra payment
    number_of_payments_exclude_extra = 0 # Total number of payments without extra payment
    totalpayment1 = 0 #Payments for the first 12 months
    totalpayment2 = 0 #Payments for the rest 
    number_of_payments_after12 = 0 #Number of months after first 12 month
    while principal > 0:
        if extra_payment_start < number_of_payments <= extra_payment_end:

            principal = principal * (1 + rate/12) - monthly_payment - extra_payment

            number_of_payments_include_extra+= 1
            totalpayment1 = number_of_payments_include_extra * (monthly_payment + extra_payment)

            print(str(number_of_payments)+',$ '+str(round(totalpayment1,1)) +',$',round(principal,2))

            number_of_payments += 1
        else:
            principal = principal * (1 + rate/12) - monthly_payment
            number_of_payments_exclude_extra += 1

            totalpayment2 = number_of_payments_exclude_extra * monthly_payment
            print(str(number_of_payments)+',$ '+str(round(totalpayment2,1)) +',$',round(principal,2))
            number_of_payments += 1


total_3(30000, 0.035, 545.75, 200, 0, 12)
'''    1, $  745.75, $29341.75
       2, $ 1491.50, $28681.58
       3, $ 2237.25, $28019.48
       4, $ 2983.00, $27355.46
       5, $ 3728.75, $26689.49
      ...
      52, $30779.00, $ 1569.19
      53, $31324.75, $ 1028.02
      54, $31870.50, $  485.26
      55, $32416.25, $  -59.07
      ```
from Ziya Aydin to everyone:    10:42 AM
# total_3(30000, 0.035, 545.75, 200, 0, 12)
from Ziya Aydin to everyone:    10:43 AM
#3.3
def total_3(principal, rate, monthly_payment, extra_payment, extra_payment_start, extra_pay
# def main():
#     principal = 30000.0
#     rate = 0.035
#     payment = 545.75
#     first_12_months_payment = 200
#     total(principal, rate, payment)
#     total_2(principal, rate, payment, first_12_months_payment)
#     # You should add more code here


# if __name__ == "__main__":
#     main()
'''
