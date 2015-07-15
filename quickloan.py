#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
from array import *
import math
CalculTypeSavings = 0
CalculTypeLoan = 0	
Monthly = 0	

def HelpLoan():
    messagebox.showinfo("Help", "For Loan:\n1/In order to know the Monthly cost of an Loan\nEnter your Loan value, Loan rate and choose the duration in years\nSelect Monthly value calcul\nClick on action\n1/In order to know the amount of a Loan\nEnter your Monthly value, Loan rate and choose the duration in years\nThen select Amount value calcul checkbox\n And click on action")


def HelpSaving():
    messagebox.showinfo("Help", "For Savings:\n1/In order to know the amount of monthly Savings to achieve a specific value of Savings\nEnter your current Savings, then your Savings rate and choose the duration in years\nSelect Monthly value calcul\nClick on action\n1/In order to know the amount of Savings that you'll reach in a specific amount of time\nEnter your current Savings, then your Savings rate and choose the duration in years\nThen select Amount value calcul checkbox\n And click on action")
	
	
def CheckbuttonMonthlyLoan():
	global CalculTypeLoan
	global StateMonthlyLoan
	if StateMonthlyLoan.get() == 1:
		CalculTypeLoan=1
	else:
		CalculTypeLoan=0
	
	buttonAmountLoan.deselect()
	

def CheckbuttonAmountLoan():
	global CalculTypeLoan
	global StateAmountLoan
	if StateAmountLoan.get() == 1:
		CalculTypeLoan=2
	else:
		CalculTypeLoan=0
	buttonMonthlyLoan.deselect()
	
def CheckbuttonMonthlySavings():
	global CalculTypeSavings
	global StateMonthlySavings
	if StateMonthlySavings.get() == 1:
		CalculTypeSavings=1
	else :
		CalculTypeSavings=0
	buttonAmountSavings.deselect()

def CheckbuttonAmountSavings():
	global CalculTypeSavings
	global StateAmountSavings
	if StateAmountSavings.get() == 1:
		CalculTypeSavings=2
	else:
		CalculTypeSavings=0
	buttonMonthlySavings.deselect()
	
def AmountSavingsCalcul():
	if len(entryMonthlySavings.get()) == 0:
		    messagebox.showinfo("Error", "Please enter your monthly savings")
	else :
		if len((entryRateSavings.get().replace(',', '.'))) == 0:
			messagebox.showinfo("Error", "Please enter your savings rate")
		else :
			if len(entryYearsSavings.get()) == 0:
				messagebox.showinfo("Error", "Please enter a savings duration in years")
			else :			
				SavingsRate = float(entryRateSavings.get().replace(',', '.'))
				CapitalInitial = 0
				YearsOfSavings = int(float(entryYearsSavings.get().replace(',', '.')))
				valYearsSavings.set(str(YearsOfSavings))
				Savings = 0
				if len(entryCapitalSavings.get()) != 0 :
					CapitalInitial = float(entryCapitalSavings.get().replace(',', '.'))
					Savings = math.pow(1+SavingsRate/100,YearsOfSavings)
					Savings = CapitalInitial * Savings
				power = 12 * YearsOfSavings
				fact = math.pow((1+SavingsRate/(12*100)),power);
				fact = fact-1;
				fact  = (1+SavingsRate/(12*100))*fact;
				Savings = Savings + int(entryMonthlySavings.get()) * (12*100/SavingsRate) * fact
				GainInterest = Savings - power * int(entryMonthlySavings.get())  - CapitalInitial
				
				valAmountSavings.set(str(int(Savings)))
				valAmountInterestSavings.set(str(int(GainInterest)))

def MonthSavingsCalcul():
	if len(entryAmountSavings.get()) == 0:
		    messagebox.showinfo("Error", "Please enter the amount of savings you want to reach")
	else :
		if len((entryRateSavings.get().replace(',', '.'))) == 0:
			messagebox.showinfo("Error", "Please enter your savings rate")
		else :
			if len(entryYearsSavings.get()) == 0:
				messagebox.showinfo("Error", "Please enter a savings duration in years")
			else :		
				SavingsRate = float(entryRateSavings.get().replace(',', '.'))
				CapitalInitial = 0
				YearsOfSavings = int(float(entryYearsSavings.get().replace(',', '.')))
				valYearsSavings.set(str(YearsOfSavings))
				SavingsValue = float(entryAmountSavings.get().replace(',', '.'))
				SavingsWithInitiCap = 0
				if len(entryCapitalSavings.get()) != 0 :
					CapitalInitial = float(entryCapitalSavings.get().replace(',', '.'))
					fact = math.pow(1+SavingsRate/100,YearsOfSavings)
					SavingsWithInitiCap = CapitalInitial * fact
				power = 12 * YearsOfSavings
				fact = math.pow((1+SavingsRate/(12*100)),power);
				fact = fact-1;
				fact  = (1+SavingsRate/(12*100))*fact;
				MonthlySavings = (SavingsValue - SavingsWithInitiCap ) * (SavingsRate /(12*100 * fact))
				GainInterest = SavingsValue - power * MonthlySavings  - CapitalInitial
				
				valMonthlySavings.set(str(int(MonthlySavings)))
				valAmountInterestSavings.set(str(int(GainInterest)))

	
def CalculSavings():
	global CalculTypeSavings
	if CalculTypeSavings == 1 :
		MonthSavingsCalcul()
	elif CalculTypeSavings == 2 :
		AmountSavingsCalcul()
	else :
		messagebox.showinfo("What do you want to do?", "Please select a calcul")
	
def LoanDumpToFile():
	global Monthly
	global Amount
	file = open(valOutputFileLoan.get()+'.csv','w')
	file.write("Monthly;;Rest to pay;;Cumulative refund;;Monthly cumulative refund;;Monthly refund interest\n");
	Indice = 0
	Indice = 1 + float(entryRateLoan.get() )/(100*12);
	CapitalRestant = array('f')
	CapitalParRemboursement = array('f')
	InteretParRemboursement = array('f')
	RemboursementCumule = array('f')
	MensualiteReel = array('f')
	
	for i in range(0,int(entryYearsLoan.get())*12):
		
		MensualiteReel.append(Monthly)
		
		if i == 0:
			CapitalRestant.append(Amount*Indice-MensualiteReel[i])
			RemboursementCumule.append(Amount-CapitalRestant[i])
			CapitalParRemboursement.append(RemboursementCumule[i])
		
		else:
			CapitalRestant.append(CapitalRestant[i-1]*Indice-MensualiteReel[i])
			RemboursementCumule.append(Amount-CapitalRestant[i])
			CapitalParRemboursement.append(RemboursementCumule[i]-RemboursementCumule[i-1])
		
		InteretParRemboursement.append(MensualiteReel[i]-CapitalParRemboursement[i])
		file.write(str(round(MensualiteReel[i]))+";;")
		file.write(str(round(CapitalRestant[i]))+";;")
		file.write(str(round(RemboursementCumule[i]))+";;")
		file.write(str(round(CapitalParRemboursement[i]))+";;")
		file.write(str(round(InteretParRemboursement[i]))+"\n")
		i = i +1
	file.close()
	
	
	
	
def LoanCalculMonthly():
	if len(entryAmountLoan.get()) == 0:
		    messagebox.showinfo("Error", "Please enter the amount value of your loan")
	else :
		if len((entryRateLoan.get().replace(',', '.'))) == 0:
			messagebox.showinfo("Error", "Please enter your loan rate")
		else :
			if len(entryYearsLoan.get()) == 0:
				messagebox.showinfo("Error", "Please enter the duration of your loan")
			else :	
				global Monthly
				global Amount
				Amount = float(entryAmountLoan.get())
				power  = -int(entryYearsLoan.get())*12
				Monthly = float(entryAmountLoan.get()) *float((entryRateLoan.get().replace(',', '.')))/(12*100)
				denom = 1+float((entryRateLoan.get().replace(',', '.')))/(12*100)
				denom = math.pow(denom,power)
				Monthly = Monthly/(1-denom)
				interet = Monthly*int(entryYearsLoan.get())*12-int(entryAmountLoan.get())
				valMonthlyLoan.set(str(int(Monthly)))
				valAmountInterestLoan.set(str(int(interet)))
				LoanDumpToFile()
				
def LoanCalculValue():
	
	if len(entryMonthlyLoan.get()) == 0:
		    messagebox.showinfo("Error", "Please enter how much you want to pay each month")
	else :
		if len((entryRateLoan.get().replace(',', '.'))) == 0:
			messagebox.showinfo("Error", "Please enter your loan rate")
		else :
			if len(entryYearsLoan.get()) == 0:
				messagebox.showinfo("Error", "Please enter the duration of your loan")
			else :
				global Monthly
				global Amount
				Monthly = float(entryMonthlyLoan.get())
				Amount = (12 * 100) / float((entryRateLoan.get().replace(',', '.'))) * float(entryMonthlyLoan.get())
				power  = -int(entryYearsLoan.get())*12
				fact = 1+float((entryRateLoan.get().replace(',', '.')))/(12*100)
				fact = math.pow(fact,power)
				Amount = Amount * (1-fact)				
				interet = float(entryMonthlyLoan.get())*int(entryYearsLoan.get())*12-Amount
				valAmountLoan.set(str(int(Amount)))
				valAmountInterestLoan.set(str(int(interet)))
				LoanDumpToFile()
	

def CalculLoan():
	global CalculTypeLoan
	if CalculTypeLoan == 1 :
		LoanCalculMonthly()
	elif CalculTypeLoan == 2 :
		LoanCalculValue()
	else :
		messagebox.showinfo("What do you want to do?", "Please select a calcul")




wndMain = Tk()



LoanFields = LabelFrame(wndMain, text="Loan", padx=20, pady=20)
LoanFields.pack(side=LEFT,fill="both", expand="yes")

lbAmountLoan= Label(LoanFields, text="Amount")
lbAmountLoan.grid(row=1, column=1)
valAmountLoan = StringVar() 
valAmountLoan.set("150000")
entryAmountLoan = Entry(LoanFields, textvariable=valAmountLoan, width=30)
entryAmountLoan.grid(row=1, column=2)

lbRateLoan= Label(LoanFields, text="Rate")
lbRateLoan.grid(row=2, column=1)
valRateLoan = StringVar() 
valRateLoan.set("2")
entryRateLoan = Entry(LoanFields, textvariable=valRateLoan, width=30)
entryRateLoan.grid(row=2, column=2)

lbYearsLoan= Label(LoanFields, text="Years")
lbYearsLoan.grid(row=3, column=1)
valYearsLoan = StringVar() 
valYearsLoan.set("15")
entryYearsLoan = Entry(LoanFields, textvariable=valYearsLoan, width=30)
entryYearsLoan.grid(row=3, column=2)

lbMonthlyLoan= Label(LoanFields, text="Monthly")
lbMonthlyLoan.grid(row=4, column=1)
valMonthlyLoan = StringVar() 
valMonthlyLoan.set("")
entryMonthlyLoan = Entry(LoanFields, textvariable=valMonthlyLoan, width=30)
entryMonthlyLoan.grid(row=4, column=2)

lbAmountInterestLoan= Label(LoanFields, text="Amount of interest")
lbAmountInterestLoan.grid(row=5, column=1)
valAmountInterestLoan = StringVar() 
valAmountInterestLoan.set("")
entryAmountInterestLoan = Entry(LoanFields, textvariable=valAmountInterestLoan, width=30)
entryAmountInterestLoan.grid(row=5, column=2)

lbOutputFileLoan= Label(LoanFields, text="Output file")
lbOutputFileLoan.grid(row=6, column=1)
valOutputFileLoan = StringVar() 
valOutputFileLoan.set("output")
entryOutputFileLoan = Entry(LoanFields, textvariable=valOutputFileLoan, width=30)
entryOutputFileLoan.grid(row=6, column=2)


StateMonthlyLoan = IntVar()
buttonMonthlyLoan = Checkbutton(LoanFields, text="Monthly value calcul?",command=CheckbuttonMonthlyLoan , variable=StateMonthlyLoan)
buttonMonthlyLoan.grid(row=7, column=1)

StateAmountLoan = IntVar()
buttonAmountLoan = Checkbutton(LoanFields, text="Amount value calcul?",command=CheckbuttonAmountLoan , variable=StateAmountLoan)
buttonAmountLoan.grid(row=7, column=2)

Button(LoanFields,text='Action', command=CalculLoan).grid(row=9, column=2)


SavingsFields = LabelFrame(wndMain, text="Savings", padx=20, pady=20)
SavingsFields.pack(side=RIGHT,fill="both", expand="yes")

lbCapitalSavings= Label(SavingsFields, text="Capital")
lbCapitalSavings.grid(row=1, column=1)
valCapitalSavings = StringVar() 
valCapitalSavings.set("500")
entryCapitalSavings = Entry(SavingsFields, textvariable=valCapitalSavings, width=30)
entryCapitalSavings.grid(row=1, column=2)

lbRateSavings= Label(SavingsFields, text="Rate")
lbRateSavings.grid(row=2, column=1)
valRateSavings = StringVar() 
valRateSavings.set("2,5")
entryRateSavings = Entry(SavingsFields, textvariable=valRateSavings, width=30)
entryRateSavings.grid(row=2, column=2)

lbMonthlySavings= Label(SavingsFields, text="Monthly")
lbMonthlySavings.grid(row=3, column=1)
valMonthlySavings = StringVar() 
valMonthlySavings.set("50")
entryMonthlySavings = Entry(SavingsFields, textvariable=valMonthlySavings, width=30)
entryMonthlySavings.grid(row=3, column=2)

lbYearsSavings= Label(SavingsFields, text="Years")
lbYearsSavings.grid(row=4, column=1)
valYearsSavings = StringVar() 
valYearsSavings.set("2")
entryYearsSavings = Entry(SavingsFields, textvariable=valYearsSavings, width=30)
entryYearsSavings.grid(row=4, column=2)


lbAmountInterestSavings= Label(SavingsFields, text="Amount of interest")
lbAmountInterestSavings.grid(row=5, column=1)
valAmountInterestSavings = StringVar() 
valAmountInterestSavings.set("")
entryAmountInterestSavings = Entry(SavingsFields, textvariable=valAmountInterestSavings, width=30)
entryAmountInterestSavings.grid(row=5, column=2)

lbAmountSavings= Label(SavingsFields, text="Savings")
lbAmountSavings.grid(row=6, column=1)
valAmountSavings = StringVar() 
valAmountSavings.set("")
entryAmountSavings = Entry(SavingsFields, textvariable=valAmountSavings, width=30)
entryAmountSavings.grid(row=6, column=2)


StateMonthlySavings = IntVar()
buttonMonthlySavings = Checkbutton(SavingsFields, text="Monthly value calcul?",command=CheckbuttonMonthlySavings, variable = StateMonthlySavings)
buttonMonthlySavings.grid(row=7, column=1)

StateAmountSavings = IntVar()
buttonAmountSavings = Checkbutton(SavingsFields, text="Amount value calcul?",command=CheckbuttonAmountSavings, variable =StateAmountSavings)
buttonAmountSavings.grid(row=7, column=2)

Button(SavingsFields,text='Action', command=CalculSavings).grid(row=9, column=2)

Menubar = Menu(wndMain)

MenuLoan = Menu(Menubar, tearoff=0)
MenuLoan.add_command(label="Help", command=HelpLoan)
MenuLoan.add_separator()
MenuLoan.add_command(label="Quit", command=wndMain.quit)
Menubar.add_cascade(label="Loan", menu=MenuLoan)

MenuSavings = Menu(Menubar, tearoff=0)
MenuSavings.add_command(label="Help", command=HelpSaving)
MenuSavings.add_separator()
MenuSavings.add_command(label="Quit", command=wndMain.quit)
Menubar.add_cascade(label="Savings", menu=MenuSavings)

wndMain.config(menu=Menubar)

wndMain.mainloop()
