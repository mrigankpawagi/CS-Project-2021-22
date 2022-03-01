import tool

signedInData = None

def display(data=None):
    global signedInData
    if data != None: 
        signedInData = data
    tool.menu("\n\nWelcome to the Patient Portal for {}!".format(signedInData[2]), [
        ("Search for Doctors", search),
        ("Appointments and Records", records),
        ("Forum", forum),
        ("Logout", tool.logout)
    ])

def search():
    pin, branch = tool.form([
        ('Your Pincode', '\d{6}'), 
        ('Medical Department', '')
    ])

def records():
    pass

def forum():
    pass

#display([8, "112233", "Mrig", "1234599999"])