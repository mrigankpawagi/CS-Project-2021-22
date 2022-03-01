import tool

def display():
    tool.menu("\n\nWelcome to the Administrator Portal!", [("Manage Doctors", doclist)]) 

def doclist():
    #docs = tool.getQuery('admin', 'doctors', '*', 'WHERE hospitalid = {}'.format())
    print("Doclist!")