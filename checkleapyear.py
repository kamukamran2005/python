a=float(input("enter year:"))
if(a%4==0):
   
   if(a%100==0):
        
       if(a%400==0):
             print("year is leap year:")
       else:
             print("this is not leap year")
   else:
        print("this is a leap year")
else:
   print("this is a leap year")


