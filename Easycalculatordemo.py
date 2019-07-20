#Calculator- Simple

while(True):
    a = input("Input First Number : ")
    b = input("Input Second Number : ")
    operator = input("Input Operator : ")

    if(operator=="+"):
        c=float(a)+float(b)
    elif(operator=="-"):
        c=float(a)-float(b)
    elif(operator=="*"):
        c=float(a)*float(b)
    elif(operator=="/"):
        if(int(b)==0):
            print("Cannot Divide by Zero")
            c="ERROR"
        else:
            c=float(a)/float(b)
    else:
        print("INVALID OPERATOR")
        c="Error"
        
    print(c)

    answer=input("Continue? [Yes/No] : ")
    if(answer != 'yes' and answer !="Y" and answer !="Yes" and answer !="y"):
        break
