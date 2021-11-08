import os
import platform
import datetime as dt
from prettytable import PrettyTable
import mysql.connector

passwrdddd=input("Enter your systems mysql password :- ")
mydb = mysql.connector.connect(user="root", password=passwrdddd,host="localhost",database="vaccinerecord")
cur=mydb.cursor()

well="Vaccine Record Management System Patient Panel"
welll="Vaccine Record Management System Medical Professional Panel"
we=well.center(89,"=")
wee=welll.center(89,"=")

#medical panel start

def clearscreen():
        print(os.system('cls'))
        
def details(b):
    t=PrettyTable(['Pateint_ID','Name','Age','Corona Status','Vaccine_ID','Vaccine_Name','Undercare of','First_Shot','Second Shot'])
    for i in range(len(b)):
        t.add_row([b[i][0],b[i][1],b[i][2],b[i][3],b[i][4],b[i][5],b[i][6],b[i][7],b[i][8]])
    print("Pateint Details :- ")
    print(t)

def lulu(ab):
    cur.execute("select pat_id from patdata")
    aa=cur.fetchall()
    aaa=(ab,)
    if aaa in aa:
        return True
    else:
        return False

def lalu(a):
    cur.execute("select prof_id from profdata;")
    checkk=cur.fetchall()
    check=(a,)
    if check in checkk:
        return True
    else:
        return False

def lalp(abc):
    cur.execute("select vacproid from vacpro;")
    u=cur.fetchall()
    check=(abc,)
    if check in u:
        return True
    else:
        return False

def plogr():
    print(wee)
    l=[]
    a=input("Enter username :- ")
    aa=input("Enter password :- ")
    aaa=input("Enter password to confirm :- ")
    if aa==aaa:
        l.append(a)
        l.append(aa)
    else:
        print("password entered to confirm does not match with password to set")
    log=(l)
    sql="insert into patlogi values(%s,%s);"
    cur.execute(sql,log)
    mydb.commit()
    print("Registration Successful")

def pplogr():
    print(we)
    l=[]
    a=input("Enter username :- ")
    aa=input("Enter password :- ")
    aaa=input("Enter password to confirm :- ")
    if aa==aaa:
        l.append(a)
        l.append(aa)
    else:
        print("password entered to confirm does not match with password to set")
    log=(l)
    sql="insert into proflogi values(%s,%s);"
    cur.execute(sql,log)
    mydb.commit()
    print("Registration Successful")

def plog():
    print(we)
    a=input("Enter your username :- ")
    aa=input("Enter password :- ")
    l=(a,aa)
    cur.execute("select * from patlogi")
    aaa=cur.fetchall() 
    if l in aaa:
        return True
    else :
        False

def pplog():
    print(wee)
    a=input("Enter your username :- ")
    aa=input("Enter password :- ")
    l=(a,aa)
    cur.execute("select * from proflogi")
    aaa=cur.fetchall() 
    if l in aaa:
        return True
    else :
        False

def precnew():
    ppopp=1
    while ppopp==1:
        clearscreen()
        print(wee)
        l=[]
        a=int(input("Enter pateint id :- "))
        cur.execute("select pat_id from patdata")
        aa=cur.fetchall()
        aaa=(a)
        if aaa==aa:
            print("Pateint already resgistered")
        else:
            l.append(a)
        b=input("Enter name of pateint :- ")
        l.append(b)
        c=int(input("Enter age of pateint :- "))
        l.append(c)
        print("Press 1 if pateint corona positive")
        print("Press 2 if pateint corona negitive")
        d=int(input("Enter your choice 1/2 :- "))
        if d==1 or 2:
            if d==1:
                dd="Positive"
                l.append(dd)
            else:
                dd="Negitive"
                l.append(dd)
        else:
            print("Enter vaild choice")
        clearscreen()
        print(wee)
        cur.execute("select * from vacpro")
        eee=cur.fetchall()
        pt=PrettyTable(['Vaccine_ID','Vaccine_Name','Vaccine_Cost'])
        for i in eee:
            pt.add_row([i[0],i[1],i[2]])
        print(pt)
        ee=int(input("Enter ID of vaccine to be used to vaccinate :- "))

        sqll="select * from vacpro"
        cur.execute(sqll)
        e=cur.fetchall()
        cur.execute("select vacproid from vacpro")
        checkk=cur.fetchall()
        if lalp(ee)==True:
            l.append(ee)
            if ee==len(e):
                l.append(e[ee-1][1])
            else:
                l.append(e[ee][1])
        else:
            print("Enter proper vaccine information")
        clearscreen()
        print(wee)
        f=int(input("Enter Medical Professional ID :- "))
        cur.execute("select prof_id from profdata")
        checkk=cur.fetchall()
        check=(f)
        if lalu(f)==True:
            l.append(f)
        else:
            print("Enter proper/vaild medical ID")
        
        g=int(input("Enter day no. of first vaccine shot :- "))
        gg=int(input("Enter month no. of first vaccine shot :- "))
        ggg=int(input("Enter year no. of first vaccine shot :- "))
        gggg=dt.date(ggg,gg,g)
        l.append(gggg)
        h=gggg+dt.timedelta(14)
        l.append(h)
        print("Date of second shot :- ",h)
        entry=(l)
        sql="insert into patdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cur.execute(sql,entry)
        mydb.commit()
        print("Pateint Resgistered Sucessfully")
        ppopp=int(input("Do you want to register another pateint press 1 for yes , press anything else for no :- "))

def pprecnew():
    print(wee)
    l=[]
    p=[]
    a=int(input("Enter medical professional ID:- "))
    if lalu(a)==False:
        l.append(a)
    else:
        print("Medical ID already registered")
    b=input("Enter Medical Professional's Name :- ")
    l.append(b)
    c=input("Enter Department of Medical Professional :- ")
    l.append(c)
    entry=(l)
    sql="insert into profdata values(%s,%s,%s);"
    cur.execute(sql,entry)
    mydb.commit()

def pateintscare():
    print(wee)
    print("Number of pateints under care of given Medical Professional")
    a=int(input("Enter Medical Professional ID :- "))
    if lalu(a)==True:
        cur.execute("select pat_id,pat_name from patdata where pat_profcareid=%s;",(a,))
        b=cur.fetchall()
        la=len(b)
        print("Total number of pateints under care of ",a,":- ",la)
        for i in range(la):
            print("Pateint_ID :- ",b[i][0])
            print("Pateint Name :- ",b[i][1])
            print()
    else:
        print("Enter proper/vaild Medical ID")

def vacrec():
    print(wee)
    l=[]
    a=int(input("Enter Vaccine ID of Vaccine to be registered :- "))
    if lalp(a)==False:
        l.append(a)
    else:
        print("Vaccine already registered")
    b=input("Enter name of Vaccine :- ")
    l.append(b)
    c=int(input("Enter Price of Vaccine :- "))
    l.append(c)
    entry=(l)
    sql="insert into vacpro values(%s,%s,%s)"
    cur.execute(sql,entry)
    mydb.commit()

def ponlydetails():
    clearscreen()
    print(wee)
    c=int(input("Enter pateint ID :- "))
    if lulu(c)==True:
        cc=(c,)
        cur.execute("select * from patdata where pat_id=%s",cc)
        b=cur.fetchall()
        details(b)
    else:
        print("Invaild details")

def pstatus():
    print(wee)
    print("To see corona postive pateints press 1")
    print("To see corona negitive pateints press 2")
    a=int(input("Enter your selection :- "))
    t = PrettyTable(['Pateint_ID', 'Pateint_Name','Pateint_Status'])
    c=[]
    d=[]
    e=[]
    if a==1:
        cur.execute("select pat_id,pat_name,pat_status from patdata where pat_status='Positive';")
        b=cur.fetchall()
        for i in range (len(b)):
            c.append(b[i][0])
            d.append(b[i][1])
            e.append(b[i][2])
        for o in range(len(c)):
            t.add_row([c[o],d[o],e[o]])
    if a==2:
        cur.execute("select pat_id,pat_name,pat_status from patdata where pat_status='Negitive';")
        b=cur.fetchall()
        for i in range (len(b)):
            c.append(b[i][0])
            d.append(b[i][1])
            e.append(b[i][2])
        for o in range(len(c)):
            t.add_row([c[o],d[o],e[o]])
    else:
        print("Select proper option")
    print(t)

def pdetail():
    clearscreen()
    print(wee)
    print("To Display Details :- ")
    print("Based on Pateint ID press 1")
    print("Based on Medical Professional ID press 2")
    print("Based on Vaccine ID press 3")
    a=int(input("Enter selection :- "))
    if a==1:
        ponlydetails()
    elif a==2:
        clearscreen()
        print(wee)
        d=int(input("Enter Medical Professional ID :- "))
        if lalu(d)==True:
            cur.execute("select * from patdata where pat_profcareid=%s",(d,))
            e=cur.fetchall()
            details(e)
        else:
            print("Invaild medical ID")
    elif a==3:
        clearscreen()
        print(wee)
        g=int(input("Enter vaccine ID :- "))
        if lalp(g)==True:
            cur.execute("select * from patdata where pat_vacproid=%s;",(g,))
            h=cur.fetchall()
            details(h)
        else:
            print("invaild vaccine ID")
    else:
        print("Enter vaild choice")

def alldata():
    clearscreen()
    print(wee)
    print("Display all Details of all")
    print("Pateints press 1")
    print("Medical Professionals press 2")
    print("Vaccines press 3")
    a=int(input("Enter your choice :- "))
    if a==1:
        clearscreen()
        print(wee)
        cur.execute("select * from patdata")
        b=cur.fetchall()
        t = PrettyTable(['Pateint_ID', 'Name','Age','Status','Vaccine_ID_Given','Vaccine_Given','Undercare of','First Shot','Second Shot'])
        for i in range(len(b)):
            t.add_row([b[i][0],b[i][1],b[i][2],b[i][3],b[i][4],b[i][5],b[i][6],b[i][7],b[i][8]])
        clearscreen()
        print(wee)
        print("Details of pateints :- ")
        print(t)
        print("Total number of entries :- ",len(b))
    elif a==2:
        clearscreen()
        print(wee)
        cur.execute("select * from profdata")
        c=cur.fetchall()
        y=PrettyTable(['Medical_Professional_ID', 'Name','Department'])
        for e in range(len(c)):
            y.add_row([c[e][0],c[e][1],c[e][2]])
        clearscreen()
        print(wee)
        print("Details of Medicla Professionals :- ")
        print(y)
        print("Total number of entries :- ",len(c))
    elif a==3:
        clearscreen()
        print(wee)
        cur.execute("select * from vacpro")
        d=cur.fetchall()
        u=PrettyTable(['Vaccine_ID', 'Vaccine_Name','Vaccine_Price'])
        for q in range(len(d)):
            q.add_row([d[q][0],d[q][1],d[q][2]])
        print(u)
    else:
        print("Invaild selection")

#medical panel over

def vacbill():
    clearscreen()
    print(we)
    a=int(input("Enter Pateint ID :- "))
    if lulu(a)==True:
        cur.execute("select pat_vacproid from patdata where pat_id=%s;",(a,))
        b=cur.fetchall()
        print(b)
        bb=b[0][0]
        cur.execute("select vacprocost from vacpro where vacproid=%s;",(bb,))
        c=cur.fetchall()
        print(c)
        cc=c[0][0]
        cur.execute("select * from patdata where pat_id=%s",(a,))
        d=cur.fetchall()
        print(d)
        clearscreen()
        print(we)
        print("Bill :- ")
        print("Cost :- ",cc,"rupees")
        print("Details of Pateint :- ")
        details(d)
    else:
        print("Enter proper/vaild Pateint ID")


