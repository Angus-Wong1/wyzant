#Remaining principal of this month = Remaining principal of last month * (1 + Rate / 12) - Monthly payment. 

def total(principal, rate, monthly_payment, first12):
    """
    You should write your code for this program in this function. You could create other functions too if needed. Make sure to delete the 'pass' line before starting to write your own code. I recommend you first read main() function and make sure you understand how this function is called. You should also delete this docstring and replace it with a better, more descriptive one.
    """
    number_of_payments = 0
    totalpayment = 0
    while  principal > 0:

        if number_of_payments< 12:
            totalmonthlyPayment = (1 + rate/12)-monthly_payment-first12-1
            
            principal = principal * (1 + rate/12) - monthly_payment -first12
            print(principal,totalmonthlyPayment)
            totalpayment+=totalmonthlyPayment
            number_of_payments += 1

        else:
            totalmonthlyPayment = (1 + rate/12) - monthly_payment -1

            principal = principal * (1 + rate/12) - monthly_payment
            number_of_payments += 1
            totalpayment +=totalmonthlyPayment

    print(principal)
    print(number_of_payments,abs(totalpayment))
total(30000, 0.035, 545.75,200)