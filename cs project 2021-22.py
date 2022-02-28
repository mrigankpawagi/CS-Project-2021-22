import mysql.connector
import random as r
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="jyoshi!@0987")
myc=mydb.cursor()
p=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x',
   'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V',
   'W', 'X', 'Y','Z','@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<','0', '1',
   '2', '3', '4', '5', '6', '7', '8', '9']

def passw():
    passw=""
    for i in range(5):
        pchoice=r.choice(p)
        passw=passw+pchoice
    pa=passw
    return pa

def forum():
    print()
    myc.execute("use admin")
    myc.execute("""create table if not exists query(
        qid int not null primary key auto_increment,
        pid int,
        ques varchar(150),
        ans varchar(150))""")
    print("-"*10,"Welcome to private forum","-"*10)
    print()
    pid=int(input("Enter your patient ID: "))
    q=input("Enter your query: ")
    print("Thankyou! Your query will be answered soon")
    myc.execute("insert into query(pid,ques) values('{}','{}')".format(pid,q))

def query():
    print()
    myc.execute("use admin")
    myc.execute("""create table if not exists adminquery(
        qid int not null primary key auto_increment,
        pid int,
        ques varchar(150),
        ans varchar(150))""")
    print("-"*10,"Welcome to private forum","-"*10)
    print()
    pid=int(input("Enter your patient ID: "))
    q=input("Enter your query for admin: ")
    print("Thankyou! Your query will be answered soon")
    myc.execute("insert into adminquery(pid,ques) values('{}','{}')".format(pid,q))

def search_hospital():
    myc.execute("use admin")
    print()
    pin=int(input("Enter desired area pincode: "))
    myc.execute("select hname,haddress,hcontact,hemail,htext from hospitals where hpin='"+str(pin)+"'")
    r=myc.fetchall()
    if r==[]:
        print("Sorry, no hospitals available in the region")
        print()
    else:
        for i in r:
            print()
            print("Hospital:",i[0])
            print("Address:",i[1])
            print("Contact:",i[2])
            print("Email:",i[3])
            print("Description:",i[4])
    
def patientsignup():
    print("-----Welcome to patient registration-----")
    myc.execute("create database if not exists patients")
    myc.execute("use patients")
    print()
    n=input("Enter patient name: ")
    a=int(input("Enter age: "))
    add=input("Enter residential address: ")
    pin=int(input("Enter pincode: "))
    while True:
        cn=int(input("Enter contact number: "))
        if len(str(cn))==10:
            break
        else:
            print("Invalid number")
    e=input("Enter email address: ")
    pid=r.randint(10000000,99999999)
    pa=passw()
    myc.execute("""create table if not exists profile(
                patient_id int primary key,
                ppass varchar(10),
                pname varchar(40),
                page int,
                paddress varchar(60),
                ppin int,
                pcontact bigint,
                pemail varchar(40))""")
    myc.execute("insert into profile values('{}','{}','{}','{}','{}','{}','{}','{}')".format(pid,pa,n,a,add,pin,cn,e))
    mydb.commit()
    print()
    print("Patient registered successfully")
    print("Your Patient ID is:",pid)
    print("Your password is:",pa)

def adminsignup():
    print("-----Welcome to Admin registration-----")
    myc.execute("create database if not exists admin")
    myc.execute("use admin")
    print()
    n=input("Enter Hospital name: ")
    add=input("Enter address: ")
    pin=int(input("Enter pincode: "))
    cn=int(input("Enter contact number: "))
    e=input("Enter email address: ")
    dt=input("Enter description: ")
    hid=r.randint(100000000,999999999)
    hpa=passw()
    myc.execute("""create table if not exists hospitals(
                hospital_id int primary key,
                hpass varchar(10),
                hname varchar(60),
                haddress varchar(60),
                hpin int,
                hcontact bigint,
                hemail varchar(60),
                htext varchar(80))""")
    myc.execute("insert into hospitals values('{}','{}','{}','{}','{}','{}','{}','{}')".format(hid,hpa,n,add,
                                                                                               pin,cn,e,dt))
    mydb.commit()
    print()
    print("Hospital registered successfully")
    print("Hospital ID:",hid)
    print("Password:",hpa)

def patientsignin():
        print("-----Welcome to Patient Sign IN-----")
        print()
        pid=int(input("Enter Patient ID: "))
        pa=input("Enter password: ")
        myc.execute("use patients")
        myc.execute("select * from profile where patient_id='"+str(pid)+"'")
        result=myc.fetchone()
        if result==None:
            print("Patient does not exist")
        else:
            myc.execute("select ppass,pname from profile where patient_id='"+str(pid)+"'")
            pr=myc.fetchone()
            if pa==pr[0]:
                print("Logged in successfully")
                print()
                print("----- Welcome",pr[1],"-----")
                while True:
                    print()
                    print("1: Appointment Booking")
                    print("2: Appointment Cancellation")
                    print("3: View Lab Reports")
                    print("4: View Medical History")
                    print("5: Go to private forum")
                    print("6: Search for a nearby hospital")
                    print("7: Ask Queries")
                    print("8: EXIT")
                    ch1=input("Enter your choice: ")
                    if ch1=="5":
                        forum()
                    if ch1=="6":
                        search_hospital()
                    if ch1=="7":
                        query()
                    if ch1=="8":
                        break
            else:
                print("Invalid password")

def adminsignin():
        print("-----Welcome to Admin Sign IN-----")
        hid=int(input("Enter Hospital ID: "))
        pa=input("Enter password: ")
        myc.execute("use admin")
        myc.execute("select * from hospitals where hospital_id='"+str(hid)+"'")
        result=myc.fetchone()
        if result==None:
            print("Hospital does not exist")
        else:
            myc.execute("select hpass,hname from hospitals where hospital_id='"+str(hid)+"'")
            pr=myc.fetchone()
            if pa==pr[0]:
                print("Logged in successfully")
                print()
                print("----- Welcome to the admin portal of",pr[1],"-----")
            else:
                print("Invalid password")
                                                  
print("\t\t\t\tWelcome to MediSmart")
while True:
    print("-"*110)
    print()
    print("1: Sign Up")
    print("2: Sign In")
    print("3: EXIT")
    c1=int(input("Enter your choice: "))
    print()
    if c1==1:
        print("Sign Up as")
        print("1: Patient")
        print("2: Admin")
        c2=int(input("Enter your choice: "))
        print()
        if c2==1:
            patientsignup()
        elif c2==2:
            adminsignup()
        else:
            print("INVALID!")
    elif c1==2:
        print("Sign In as:")
        print("1: Patient")
        print("2: Doctor")
        print("3: Admin")
        c3=int(input("Enter your choice: "))
        print()
        if c3==1:
            patientsignin()
        elif c3==3:
            adminsignin()
        else:
            print("INVALID!")
    elif c1==3:
        break
    else:
        print("INVALID!")
