# from fpdf import FPDF
# class Bill:
#
#     def __init__(self,amount,period):
#         self.amount = amount
#         self.period = period
#
#
#
#
#
# class Flatmate:
#
#     def __init__(self,name,flatmate_days,your_days):
#         self.name = name
#         self.flatmate_days = flatmate_days
#         self.your_days = your_days
#
#     def calculate(self,bill):
#         sum_of_both = self.your_days+self.flatmate_days
#         amount_your_flatmate_need_to_pay = bill.amount*(self.flatmate_days/sum_of_both)
#         amount_you_need_to_pay = bill.amount*(self.your_days/sum_of_both)
#         return amount_your_flatmate_need_to_pay,amount_you_need_to_pay
#
# class Generate_pdf(Flatmate):
#
#     def print_pdf(self,pdf):
#         pdf.add_page()
#         pdf.set_font(family="Times",size=24,style="B")
#         pdf.cell(w=0,h=80,txt="Bill",border=1,align="C",ln=1)
#         pdf.cell(w=0,h=40,txt="Period: ",border=1,ln=1)
#         #pdf.cell(w=150,h=40)
#         pdf.cell(w=150,h=80,txt="flatmate days:",border=1)
#         pdf.cell(w=170,h=80,txt=flatmate.flatmate_days,border=1)
#
#         pdf.output("bill.pdf")
#
#
#
#
#
# # pdf = FPDF(orientation="P",unit="pt",format="A4")
# # generate_pdf.print_pdf(pdf)
#
# bill_amount = float(input("Enter the bill amount: "))
# bill_period = int(input("Enter the bill period: "))
#
# your_name = input("Enter your name: ")
# flatmate_name = input("Enter your flatmate name:")
# flatmate_days = int(input("Enter the number of days your flatmate stayed in the house: "))
# your_days = int(input("Enter the number of days you stayed in the house: "))
#
# bill = Bill(bill_amount,bill_period)
#
# flatmate = Flatmate(flatmate_name,flatmate_days,your_days)
# flatmate_amount,your_amount = flatmate.calculate(bill)
# print("Your flatmate need to pay: ",flatmate_amount)
# pdf = FPDF(orientation="P",unit="pt",format="A4")
#
# generate_pdf = Generate_pdf(flatmate_name,flatmate_days,your_days)
# generate_pdf.print_pdf(pdf)
#
#
#
#
#
#
#


from fpdf import FPDF

class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    def __init__(self, name, flatmate_days, your_days):
        self.name = name
        self.flatmate_days = flatmate_days
        self.your_days = your_days

    def calculate(self, bill):
        sum_of_both = self.your_days + self.flatmate_days
        amount_your_flatmate_need_to_pay = bill.amount * (self.flatmate_days / sum_of_both)
        amount_you_need_to_pay = bill.amount * (self.your_days / sum_of_both)
        return amount_your_flatmate_need_to_pay, amount_you_need_to_pay

class GeneratePDF(Flatmate):
    def print_pdf(self, pdf):
        pdf.add_page()
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Monthly Bill", border=0, align="C", ln=1)
        pdf.cell(w=150, h=40, txt="Name ")
        pdf.cell(w=170, h=40, txt="Period: ")
        pdf.cell(w=190, h=40, txt="Amount",ln=1)
        pdf.cell(w=150, h=80, txt=self.name)
        pdf.cell(w=170, h=80, txt=str(self.flatmate_days)+" Days")
        pdf.cell(w=190 ,h=80, txt=str(flatmate_amount),ln=1)
        global your_name

        pdf.cell(w=150, h=80, txt=your_name)
        pdf.cell(w=170, h=80, txt=f"{self.your_days}  Days")
        pdf.cell(w=190, h=80, txt=str(your_amount),ln=1)

        global bill_amount
        pdf.cell(w=150,h=80, txt= "Total Bill")
        pdf.cell(w=170,h=80, txt = str(bill_amount))


        pdf.output("bill.pdf")

bill_amount = float(input("Enter the bill amount: "))
bill_period = int(input("Enter the bill period: "))

your_name = input("Enter your name: ")
flatmate_name = input("Enter your flatmate name:")
flatmate_days = int(input("Enter the number of days your flatmate stayed in the house: "))
your_days = int(input("Enter the number of days you stayed in the house: "))

bill = Bill(bill_amount, bill_period)
flatmate = Flatmate(flatmate_name, flatmate_days, your_days)
flatmate_amount, your_amount = flatmate.calculate(bill)

pdf = FPDF(orientation="P", unit="pt", format="A4")
pdf_generator = GeneratePDF(flatmate_name, flatmate_days, your_days)  # Create an instance
pdf_generator.print_pdf(pdf)  # Call the instance method

print("Your flatmate need to pay:", flatmate_amount)
