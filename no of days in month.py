a=str(input("enter the month:"))
if a=="january" or a=="march" or a=='may' or a=='july' or a=='august' or a=='october' or a=='december':
     print("no of days :31")
elif a=='april' or a=='june' or  a=='september' or  a=='november' :
     print("no of days:30")
elif a=="february":
    print("no of days:28")
else:
    print(" please enter valid month")
