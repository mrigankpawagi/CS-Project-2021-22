from datetime import datetime
import sqlite3 as sql
import tool

signedInData = None
slots = None

def display(data=None):
    global signedInData
    if data != None: 
        signedInData = data
    tool.menu("\n\nWelcome to the Patient Portal for {}!".format(signedInData[2]), [
        ("Search for Doctors", search),
        ("Appointments and Records", records),
        ("Forum", forum),
        ("Inquiries", inquirylist),
        ("Logout", tool.logout)
    ])
    
def search():
    global slots
    pin, branch = tool.form([
        ('Your Pincode', '\d{6}'), 
        ('Medical Department', '')
    ])
    slots = tool.getQuery('admin', '(slots JOIN doctors ON slots.docid = doctors.id) JOIN hospitals on slots.hospitalid = hospitals.id', '*', 'WHERE hospitals.pincode = "{}" AND doctors.branch LIKE "%{}%" AND slots.patientid IS NULL'.format(pin, branch))
    
    k = 0
    print("\nHere are your search results.\n")
    for S in slots:
        slotTime = datetime.strptime(S[4] + " " + S[5], "%d-%m-%Y %H:%M").timestamp()
        currentTime = datetime.now().timestamp()
        if currentTime < slotTime:     
            k += 1
            tool.printItem("[Slot ID: " + str(S[0]) + "] Dr. " + S[13] + ", " + S[17], {
                'Date': S[4],
                'Time': S[5] + " to " + S[6],
                'Hospital Address': S[18],
                'Hospital Phone': S[20],
                'About Hospital': S[21]            
            })
    if k == 0:
        print("No doctors are available at the moment.")
        display()
    tool.menu('', [
        ("Book an appointment", bookSlot),
        ("Send inquiry to a hospital", inquire),
        ("Return", display)
    ])     

def records():
    pass

def forum():
    res = tool.getQuery('admin', 'forum', 'question, answer, docid', 'WHERE patientid = "{}"'.format(signedInData[0]))
    
    for r in res:
        tool.printItem('Unanswered' if r[2] == None else 'Answered', {
            ('Question: ' + r[0]): ('Answer: ' + str(r[1]))
        })
    tool.menu('', [
        ("Ask a question", forumAsk),
        ("Return", display)
    ])

def forumAsk(): 
    query, = tool.form([("Ask your question", '')])
    tool.writeQuery("admin", "forum", "patientid, question", "'" + "', '".join([str(signedInData[0]), query]) + "'")
    print("Question posted successfully.")
    forum()

def bookSlot():
    id, = tool.form([("Slot ID", '\d*')])
    if int(id) not in [S[0] for S in slots]:
        print("Incorrect ID. Please try again.")
        bookSlot()
    else:
        tool.updateQuery("admin", "slots", {'patientid': signedInData[0]}, "id = '{}'".format(id))
        print("Appointment booked successfully.")
        display()

def inquire():
    id, = tool.form([("Slot ID", '\d*')])
    if int(id) not in [S[0] for S in slots]:
        print("Incorrect ID. Please try again.")
        bookSlot()
    else:
        query, = tool.form([("Your query", '')])
        tool.writeQuery("admin", "queries", "patientid, hospitalid, slotid, question", "'" + "', '".join([str(signedInData[0]), str(slots[[S[0] for S in slots].index(int(id))][15]), id, query]) + "'")
        print("Inquiry sent successfully.")
        display()
    
def inquirylist():
    pass

def updateaccount():
    con = sql.connect("patient.db")
    cur = con.cursor()
    print("Please provide the following details:\n")
    pid = int(input("Enter your ID: "))
    passw = input("Enter your password: ")
    cur.execute("select password from patients where id = " + str(pid))
    res = cur.fetchone()
    if len(res) == 0:
        print("Invalid ID. Please try again.")
        updateaccount()
    elif passw != res[1]:
        print("Invalid password. Please try again.")
    else:
        c = input("What do you want to change?\n1. Password\n2. Name\n3. Contact number\n")
        if c == 1:
            npass = input("Enter new password: ")
            cur.execute("update patients set password = (?) where id = " + str(pid), (npass,))
        elif c == 2:
            nname = input("Enter new profile name: ")
            cur.execute("update patients set name = (?) where id = " + str(pid), (nname,))
        elif c == 3:
            nphone = input("Enter new contact: ")
            cur.execute("update patients set phone = (?) where id = " + str(pid), (nphone,))
        else:
            print("Invalid choice. Try again.")
            updateaccount()
        
#display([8, "112233", "Mrig", "1234599999"])