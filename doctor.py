import tool
from commons import *

signedInData = None

def display(data=None):
    global signedInData
    if data != None: 
        signedInData = data
    tool.menu("\n\nWelcome to the Doctor Portal for {}!".format(signedInData[3]), [
        ("Appointments", appointments),
        ("Patient Search", patientSearch),
        ("Forum", forum),
        ("Logout", tool.logout)
    ])

def appointments():
    pass

def forum():
    pass

def closeslot():
    global slots
    id = tool.form([("Slot ID",'\d*')])
    if int(id) not in [S[0] for S in slots]:
        print("Incorrect ID. Please try again.")
        closeslot()
    else:
        if slots[[S[0] for S in slots].index(int(id))][15] == "Closed": 
            print("Closed slots cannot be closed again.")
        else:
            name = input("Enter prescription name: ")
            tool.updateQuery("admin", "slots", {"presfilename":name}, 'id = "{}"'.format(id))
            c = input("How do you want to upload the prescription?\n1. Text\n2. File\n")
            if c == "1":
                pres = input("Enter closing prescription: ")
                tool.updateQuery("admin", "slots", {"prestext":pres}, 'id = "{}"'.format(id)) 
            elif c == "2":
                pres = input("Enter file path: ")
                tool.insertblob(id, pres)

display([2, "q3m1M8", 3, "Ponty Sharma", "Peadiatrician"])