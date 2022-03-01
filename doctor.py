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

display([2, "q3m1M8", 3, "Ponty Sharma", "Peadiatrician"])