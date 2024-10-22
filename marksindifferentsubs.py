english=float(input("enter marks in english:"))
science=float(input("enter marks in science:"))
math=float(input("eneter marks in math:"))
urdu=float(input("enter marks in urdu:"))
sst=float(input("enter marks in sst:"))
totalmarks=english+math+science+urdu+sst
percentage=totalmarks/500*100
if(percentage>75):
            print(percentage,"%"," congrats u have a distinction")
elif(percentage>=60):
       print(percentage,"%","congrats u have A grade")
elif(percentage> 55):
       print(percentage,"%","congrats u have b grade")
elif(percentage>=33):
       print(percentage,"%","congrats u have c grade","need hard work")
else:
            print(percentage,"%","fail")
