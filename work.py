print("Welcome To Salary calculator")
a=input("Name of the Employee ")
b=int(input("Month for which salary is being counted(use no. instead of full name) "))
k=0
if b<1 or b>12:
    while k<1:
        b=int(input("Enter No. B/W 1-12"))
        if b>1 or b<12:
            k=1
c=0
if b==1:
    c=31
if b==2:
    c=29
if b==3:
    c=31
if b==4:
    c=30
if b==5:
    c=31
if b==6:
    c=30
if b==7:
    c=31
if b==8:
    c=31
if b==9:
    c=30
if b==10:
    c=31
if b==11:
    c=30
if b==12:
    c=31
i=0
d=int(input("No. of days Employee was present"))
if d>c :
     while i<1:
          d=int(input("No. of days work exceed no. of days in month Enter correct No."))
          if d<c or d==c:
              break
j=0
e=input("Designation(M for Manager,TL for Team Leader, TM for Team Member)")          
if e=='M' or e=='TL' or e=='TM':
    j=0
else: 
    while j<1:
        e=input("Enter correct designation")
        if e=='M' or e=='TL' or e=='TM':
            j=1;
salary=0
if e=='M':
    salary=2000
if e=='TL':
    salary=1800
if e=='TM':
    salary=1500
f=int(input("Overtime(if done or put 0)"))
f=f/2
d=d+f
salary=salary*d
print("Salary of an employee is ",salary)
