score = int(input("Enter your socres: "))



if score >=101: 
    print("Enter your score again -__-!")
    exit() #use exit() to terminate/exit the program



if score >= 90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else: print("F")