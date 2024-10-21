S1=float(input("enter value of side 1:"))
S2=float(input("enter value of side 2:"))
S3=float(input("enter value of side 3:"))
if(S1==S2 and S1==S3):
    print("traingle is equilateral")
elif(S1==S2 or S1==S3 or S3==S2):
    print("traingle is isosceles")
else:
        print("traingle is scalene ")
