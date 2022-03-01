import tool

signedInData = None
docs = None

def display(data=None):
    global signedInData
    if data != None: 
        signedInData = data
    tool.menu("\n\nWelcome to the Administrator Portal for {}!".format(signedInData[2]), [
        ("Manage Doctors", doclist),
        ("Manage Account", account),
        ("Patient Search", patientSearch),
        ("Messages", messages),
        ("Logout", logout)
    ]) 

def doclist():
    global docs
    docs = tool.getQuery('admin', 'doctors', '*', 'WHERE hospitalid = "{}"'.format(signedInData[0]))
    tool.printTable(docs, {0: "Doctor ID", 3: "Name", 4: "Speciality", 1: "Password"})
    tool.menu('', [
        ("Add Doctor", addDoc),
        ("Edit Doctor Details", editDoc),
        ("Delete Doctor", delDoc),
        ("Manage Slots", slots),
        ("Return", display)
    ]) 


def account():
    pass

def patientSearch():
    pass

def messages():
    pass

def logout():
    pass

def addDoc():
    name, branch = tool.form([
        ('Name of Doctor', ''), 
        ('Speciality', '')
    ])
    passw = tool.randstr(6)
    id = tool.writeQuery("admin", "doctors", "name, branch, hospitalid, password", "'" + "', '".join([name, branch, str(signedInData[0]), passw]) + "'")
    print("Doctor added.\n")
    print("Doctor ID: ", id)
    print("Password is: ", passw)

    doclist()

def editDoc():
    id, = tool.form([("Doctor ID", '\d*')])
    if int(id) not in [d[0] for d in docs]:
        print("Incorrect ID. Please try again.")
        editDoc()
    else:
        name, branch, passw = tool.form([
            ('New Name', ''), 
            ('New Speciality', ''),
            ('New Password (at least 6 characters)', '.......*')
        ])
        tool.updateQuery("admin", "doctors", {'name': name, 'branch': branch, 'password': passw}, 'id = "{}"'.format(id))
        print("Details updated successfully.")

        doclist()

def delDoc():
    pass

def slots():
    pass

display([3, '123456', 'Yatharth Hospital', 'Sec-82, Noida',	201304, '9268121866', 'Best hospital in NCR'])