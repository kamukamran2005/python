a=int(input("enter no:"))
c=0

if a >=100:
   c+=a//100
   a=a%100
print("total 100:",c)   
if a >=50:
    c+=a//50
    a=a%50
print("total 50:",c)    
if a >20:
   c+=a//20
   a=a%20
print(c)   
if a >=5:
   c+=a//5
   a=a%5
print(c)   
if a >=1:
   c+=a//1
   a=a%1
print(c)   

   





