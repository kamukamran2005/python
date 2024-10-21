#check prime no
a=int(input("enter no:"))
i=2
c=0
while(i<=a):
     if(a%i==0):
          c=c+1
     i=i+1
if(c>1):
     print("non prime")
else:
     print("Prime")

     




      
