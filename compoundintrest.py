#compound intrest

p=float(input("enter principle amount:"))
r=float(input("enter annual interest rate:"))
n=float(input("enter no of times interst is compounded per year:"))
t=float(input("enter time in year:"))
A=p*(1+(r/n))**(n*t)
print("compound intrust=",A,"rupees")
