noofstd=int(input("Enter the no. of student:- "))
list1=[]
for i in range(noofstd):
    marks=int(input("Enter marks of student no."+str(i+1)+" :- "))
    list1.append(marks)
print("\n -----------MENU----------")
print("1)Maximum no.of marks scored.")
print("2)Minimum no.of marks scored.")
print("3)Average marks scored by student.")
print("4)Sum of marks scored by student.")
print("5)exit")
b=1000
for i in range(b):
    option=int(input("Select the no. of option:-"))
    if option==2:
     Min=list1[0]
     for x in range(len(list1)):
        if Min>list1[x]:
            Min=list1[x]
     print("Minmum value scored is "+str(Min))
    if option==1:
     Max=list1[0]
     for x in range(len(list1)):
        if Max<list1[x]:
            Max=list1[x]
     print("Maximum value scored is "+str(Max))
    if option==3:
     Sum=0
     count=len(list1)
     for x in range(len(list1)):
        Sum=Sum+list1[x]
     avg=Sum/count
     print("Average marks scored by student:-"+str(avg))
    if option==4:
     Sum=0
     for x in range(len(list1)):
        Sum=Sum+list1[x]
     print("Sum of marks scored by student:-"+str(Sum))
    if option==5:
        break

