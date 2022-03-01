import tool
import patient
import admin
import doctor

signedInData = None

def patientMenu():
    tool.menu('', [('Sign Up', patientSignUp), ('Sign In', patientSignIn), ('Return', main)])

def adminMenu():
    tool.menu('', [('Sign Up', adminSignUp), ('Sign In', adminSignIn), ('Return', main)])

def doctorMenu():
    tool.menu('', [('Sign In', doctorSignIn), ('Return', main)])

def exit():
    print("Thank you for using MediSmart!")

def patientSignUp():
    global signedInData
    name, phone, passw = tool.form([
        ('Name', ''), 
        ('Phone Number', '\D*\d\D*\d\D*\d\D*\d\D*\d\D*\d\D*\d\D*\d\D*\d\D*\d\D*'), 
        ('Password (at least 6 characters)', '.......*')
    ])
    id = tool.writeQuery("patient", "patients", "name, phone, password", "'" + "', '".join([name, phone, passw]) + "'")
    signedInData = (id, passw, name, phone)
    print("You were successfully registered. Here are your account details: \n")
    print("Patient ID: ", signedInData[0])
    print("Your password is: ", signedInData[1])

    patient.display()    

def patientSignIn():
        # print("-----Welcome to Patient Sign IN-----")
        # print()
        # pid=int(input("Enter Patient ID: "))
        # pa=input("Enter password: ")
        # myc.execute("use patients")
        # myc.execute("select * from profile where patient_id='"+str(pid)+"'")
        # result=myc.fetchone()
        # if result==None:
        #     print("Patient does not exist")
        # else:
        #     myc.execute("select ppass,pname from profile where patient_id='"+str(pid)+"'")
        #     pr=myc.fetchone()
        #     if pa==pr[0]:
        #         print("Logged in successfully")
        #         print()
        #         print("----- Welcome",pr[1],"-----")
        #         while True:
        #             print()
        #             print("1: Appointment Booking")
        #             print("2: Appointment Cancellation")
        #             print("3: View Lab Reports")
        #             print("4: View Medical History")
        #             print("5: Go to private forum")
        #             print("6: Search for a nearby hospital")
        #             print("7: Ask Queries")
        #             print("8: EXIT")
        #             ch1=input("Enter your choice: ")
        #             if ch1=="5":
        #                 forum()
        #             if ch1=="6":
        #                 search_hospital()
        #             if ch1=="7":
        #                 query()
        #             if ch1=="8":
        #                 break
        #     else:
        #         print("Invalid password")
        pass

def adminSignUp():
    global signedInData
    name, address, pincode, phone, description, passw = tool.form([
        ('Hospital Name', ''), 
        ('Address', ''), 
        ('Pincode (6-digit)', '\d{6}'),
        ('Phone Number', '\D*\d\D*\d\D*\d\D*\d\D*\d\D*\d\D*\d\D*\d\D*\d\D*\d\D*'), 
        ('Description', ''), 
        ('Password (at least 6 characters)', '.......*')
    ])
    id = tool.writeQuery("admin", "hospitals", "name, address, pincode, phone, description, password", "'" + "', '".join([name, address, pincode, phone, description, passw]) + "'")
    signedInData = (id, passw, name, address, pincode, phone, description)
    print("You were successfully registered. Here are your account details: \n")
    print("Hospital ID: ", signedInData[0])
    print("Your password is: ", signedInData[1])
    
    admin.display(signedInData)

def adminSignIn():
    global signedInData
    id, passw = tool.form([
        ('Hospital ID', ''), 
        ('Password', '')
    ])
    data = tool.getQuery("admin", "hospitals", "*", "WHERE id='{}'".format(id))
    if len(data) == 0:
        print("\nIncorrect Hospital ID. Please try again.")
        adminSignIn()
    else:
        if passw != data[0][1]:
            print("\nIncorrect Password. Please try again.")
            adminSignIn()
        else:
            print("\nLogged in successfully.")
            signedInData = data[0]
            admin.display(signedInData)

def doctorSignIn():
    pass

def main():
    tool.menu('Welcome to MediSmart!', [('Continue as Patient', patientMenu), ('Continue as Administrator', adminMenu), ('Continue as Doctor', doctorMenu), ('Exit', exit)])

tool.init()
main()