print("-*-*-*-*-*-Welcome To Star bank-*-*-*-*-*-")
name=input("Please Enter Your Name:- ")
print("Welcome Mr.\\Ms. ",name,"you can now intiate your transaction here....")
print("your initial balance is 0")
print("For your transaction to be registered you must use COMMAND like:- \n1) D amount in no.\n2) W amount in no. \n *space is compulsory between D/W & amount")
bal=0
com=""
n=1
noot=0;
while True:
    if n==1:
        com=input("Enter Command:- ")
    if n==2:
        com=input("Enter correct Command:- ")
    tran=com.split()
    if tran[0]=='E' or tran[0]=='e':
        print("Total No. of Transactions Are",noot)
        print("current balance",bal)
        break;
    if tran[0]=='D' or tran[0]=='d' or tran[0]=='W' or tran[0]=='w':
        if len(tran)==1:
            print("Please enter amount")
        else:
            inp=int(tran[1])
            if inp>bal: 
                if tran[0]=="w" or tran[0]=="W":
                    print("can't withdraw your account has insufficient balance")
                    n=1
                else :
                    if tran[0]=="w" or tran[0]=="W":
                       bal=bal-inp
                       print("current balance",bal)
                       noot=noot+1
                       n=1
                    else :
                       bal=bal+inp
                       print("current balance",bal)
                       noot=noot+1
                       n=1
            else:
                    if tran[0]=="w" or tran[0]=="W":
                       bal=bal-inp
                       print("current balance",bal)
                       noot=noot+1
                       n=1
                    else :
                       bal=bal+inp
                       print("current balance",bal)
                       noot=noot+1
                       n=1
    else:
        n=2
    
