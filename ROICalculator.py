class Income():
    def __init__(self,rent,laundry,storage,misc):
        self.rent = rent
        self.laundry = laundry
        self.storage = storage
        self.misc = misc
    def total_income(self):
        return self.rent + self.laundry + self.storage + self.misc
    
class Expenses():
    def __init__(self,taxes,insurance,water,garbage,electric,HOA,lawn,vacancy,repairs,CapEx,property_Mgmt,mortgage):
        self.taxes = taxes
        self.insurance = insurance
        self.water = water
        self.garbage = garbage
        self.electric = electric
        self.HOA = HOA
        self.lawn = lawn
        self.vacancy = vacancy
        self.repairs = repairs
        self.CapEx = CapEx
        self.property_Mgmt = property_Mgmt
        self.mortgage = mortgage
    def total_expense(self):
        return (self.taxes + self.insurance + self.water + self.garbage 
               + self.electric + self.HOA + self.lawn + self.vacancy + self.repairs 
               + self.CapEx + self.property_Mgmt + self.mortgage)

class Cashflow():
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    def annual_cashflow(self):
        return (self.income.total_income() - self.expenses.total_expense()) * 12

class Cashreturn():
    def __init__(self, annual_cashflow, down_payment, closing_cost, rehab_budget, misc_other):
        self.annual_cashflow = annual_cashflow
        self.down_payment = down_payment
        self.closing_cost = closing_cost
        self.rehab_budget = rehab_budget
        self.misc_other = misc_other

    def cash_return(self):
        total_investment = self.down_payment + self.closing_cost + self.rehab_budget + self.misc_other
        return (self.annual_cashflow / total_investment) * 100

user_income = None
user_expense = None
annual_cashflow = None

print("Welcome to ROI Calculator! Please specify the income and expense first,  then you can calculate the cashflow and then cash return")
while True:
    user_action = input("Would you like to calculate: income / expenses / cashflow / cash return /exit: " )
    if user_action.lower() == "exit":
        break
    elif user_action.lower() == "income":
        monthly_rent = int(input("What is the monthly rental income per month? "))
        monthly_laundry = int(input("What is the monthly laundry income per month? "))
        monthly_storage = int(input("What is the monthly storage income per month? "))
        monthly_misc = int(input("What is the monthly other income per month? "))
        
        user_income = Income(monthly_rent,monthly_laundry,monthly_storage,monthly_misc)
        print(f"Total monthly income is: {user_income.total_income()}")
        
    elif user_action.lower() == "expenses":
        taxes = int(input("Please specify the taxes expense per month: "))
        insurance = int(input("Please specify the insurance expense per month: "))
        water = int(input("Please specify the water expense per month: "))
        garbage = int(input("Please specify the garbage expense per month: "))
        electric = int(input("Please specify the electric expense per month: "))
        HOA = int(input("Please specify the HOA expense per month per month: "))
        lawn = int(input("Please specify the lawn expense per month: "))
        vacancy = int(input("Please specify the vacancy expense: "))     
        repairs = int(input("Please specify the repairs expense: "))
        CapEx = int(input("Please specify the CapEx expense: "))
        property_Mgmt = int(input("Please specify the property managment expense: "))
        mortgage = int(input("Please specify the property mortgage expense: "))
        
        user_expense = Expenses(taxes,insurance,water,garbage,electric,HOA,lawn,
                                vacancy,repairs,CapEx,property_Mgmt,mortgage)
        print(f"Total monthly expenses is: {user_expense.total_expense()}")
        
    elif user_action.lower() == "cashflow":
        if user_income is not None and user_expense is not None:
            annual_cashflow = Cashflow(user_income, user_expense).annual_cashflow()
            print(f"Annual cashflow is {annual_cashflow}")
        else:
            print("Please specify your income and expenses first.")
    
    elif user_action.lower() == "cash return":
        if annual_cashflow is not None:
            down_payment = int(input("What is the down payment? "))
            closing_cost = int(input("What is the closing cost? "))
            rehab_budget = int(input("What is the rehab budget? "))
            misc_other = int(input("What is the other investment? "))
            
            cash_return_instance = Cashreturn(annual_cashflow, down_payment, closing_cost, rehab_budget, misc_other)
            print(f"Cash return rate = {cash_return_instance.cash_return()}%")
        else:
            print("Please calculate the annual cashflow first.")
    