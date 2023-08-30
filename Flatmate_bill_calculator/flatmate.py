class Bill:

    def __init__(self,amount,period):
        self.amount = amount
        self.period = period





class Flatmate:

    def __init__(self,name,flatmate_days,your_days):
        self.name = name
        self.flatmate_days = flatmate_days
        self.your_days = your_days

    def calculate(self,bill):
        sum_of_both = self.your_days+self.flatmate_days
        amount_your_flatmate_need_to_pay = bill.amount*(self.flatmate_days/sum_of_both)
        amount_you_need_to_pay = bill.amount*(self.your_days/sum_of_both)
        return amount_your_flatmate_need_to_pay,amount_you_need_to_pay



bill_amount = float(input("Enter the bill amount: "))
bill_period = int(input("Enter the bill period: "))

your_name = input("Enter your name: ")
flatmate_name = input("Enter your flatmate name:")
flatmate_days = int(input("Enter the number of days your flatmate stayed in the house: "))
your_days = int(input("Enter the number of days you stayed in the house: "))

bill = Bill(bill_amount,bill_period)

flatmate = Flatmate(flatmate_name,flatmate_days,your_days)
flatmate_amount,your_amount = flatmate.calculate(bill)
print("Your flatmate need to pay: ",flatmate_amount)







