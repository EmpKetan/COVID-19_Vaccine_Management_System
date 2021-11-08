from python_lal import *
from os import startfile
startfile(r'D:\vaccnie\mysqldig.png')
startfile(r'D:\vaccnie\COMPUTER SCIENCE PROJECT.docx')

def menu():
    wel="Welcome to Vaccine Record Management System"
    print(wel.center(89,"="))
    print("For Patient panel press 1")
    print("For Medical Professional panel press 2")
    ch=int(input("Enter your choice :- "))
    if ch==1:
        clearscreen()
        print(well.center(89,"="))
        print("To login press 1")
        print("To register press 2")
        chh=int(input("Enter your choice :- "))
        if chh==1:
            if plog():
                print("Operations you can perform :-")
                print("To see pateint details press 1")
                print("To view bill press 2")
                
                chhh=int(input("Enter your choice :- "))
                if chhh==1:
                    ponlydetails()
                elif chhh==2:
                    vacbill()
                else:
                    print("Enter vaild choice")
            else:
                print("User not resgistered please resgister below :-")
                plogr()
        elif chh==2:
            plogr()
        else:
            print("Enter proper/vaild choice")
    elif ch==2:
        clearscreen()
        print(wee)
        print("To login press 1")
        print("To register press 2")
        ah=int(input("Enter your choice :- "))
        if ah==1:
            if pplog():
                print("Operations you can perfrom :- ")
                print("To resgister a new pateint press 1")
                print("To resgister a vaccine press 2")
                print("To resgister a medical professional press 3")
                print("To search details based on IDs press 4")
                print("To display number of pateints under care of Medical Professionalc press 5")
                print("To display corona status of pateints press 6")
                print("To display all details stored in tables press 7")
                print("To display bill of pateint press 8")
                
                cho=int(input("Enter your choice :- "))
                if cho==1:
                    precnew()
                elif cho==2:
                    vacrec()
                elif cho==3:
                    pprecnew()
                elif cho==4:
                    pdetail()
                elif cho==5:
                    pateintscare()
                elif cho==6:
                    pstatus()
                elif cho==7:
                    alldata()
                elif cho==8:
                    vacbill()
                else:
                    print("Invaild choice")

            else:
                print("Print user not resgistered , resgister below :- ")
                pplogr()
        elif ah==2:
            pplogr()
    else:
        print("Please select proper/vaild choice")


lalal=1
while lalal==1:
    menu()
    lalal=int(input("Do you want to run the program again press 1 for yes press any other for no :- "))
