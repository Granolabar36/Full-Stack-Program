
from tkinter import *
from tkinter import messagebox as mb
from tkinter.messagebox import askyesno

import sqlite3

class gui:

    def connectDatabase(self):
        self.sqlConnection = sqlite3.connect("database.db (3).sqlite")
        self.cursor = self.sqlConnection.cursor()
        print("Connected")

    def disconnectDatabase(self):
        self.sqlConnection.close()
        print("Connection has been closed")

    def load(self):
        query = "SELECT * FROM patient"
        self.cursor.execute(query)
        everything = self.cursor.fetchall()
        self.recordsList = everything
        print(self.recordsList)
        
    def removePatient(self):
        ask = askyesno(title="Remove?", message="Do you really want to remove Patient?")

        if ask:
            patID = self.patientIDList
            self.cursor.execute("DELETE FROM patient WHERE patientId='"+patID+"'")
            self.sqlConnection.commit()

            self.name.delete("1.0", "end")
            self.age.delete("1.0", "end")
            self.sex.delete("1.0", "end")
            self.ethnicity.delete("1.0", "end")
            self.language.delete("1.0", "end")
            self.contactinfo.delete("1.0", "end")
            self.dob.delete("1.0", "end")
            self.cc.delete("1.0", "end")
            self.activeProblem.delete("1.0", "end")
            self.vaccination.delete("1.0", "end")
            self.hpi.delete("1.0", "end")
            self.plan.delete("1.0", "end")

    def addRemoveButton(self):
        self.removeButton = Button(self.root,text="Remove Patient Info", command =lambda:[self.removePatient()])#add function
        self.removeButton.grid(column=3, row=8)

    def addUpdateButton(self):
        self.updateButton = Button(self.root,text="Update Patient Info", command=lambda:[self.confirmUpdatePatient()])
        self.updateButton.grid(column=1, row=8)
        self.backButton = Button(self.root,text="Go Back", command=lambda:[self.removeMainButtons(), self.addStartButtons(), self.removeUpdateButton(), self.removeRemoveButton()])#add function
        self.backButton.grid(column=2, row=8)

    def addNewUpdateButton(self):
        mb.showinfo("Changes Made", "Patient information has been changed")
        self.newbackButton.grid_forget()
        self.updateButton = Button(self.root,text="Update Patient Info", command=lambda:[self.confirmUpdatePatient()])
        self.updateButton.grid(column=1, row=8)
        self.backButton = Button(self.root,text="Go Back", command=lambda:[self.removeMainButtons(),
                                                                           self.addStartButtons(), self.removeUpdateButton(), self.removeRemoveButton()
                                                                           , self.removeConfirmUpdateButton(), self.removeNewBackButton(), self.removeBackButtonAgain()])#add function
        self.backButton.grid(column=2, row=8)

    def removeBackButtonAgain(self):
        self.backButton.grid_forget()


    def removeConfirmUpdateButton(self):
        try:
            self.confirmUpdateButton.grid_forget()
        except:
            pass

    def removeNewBackButton(self):
        try:
            self.newbackButton.grid_forget()
        except:
            pass

    def confirmUpdatePatient(self):
        self.updateButton.grid_forget()

        self.confirmUpdateButton = Button(self.root,text="Make Changes", command =lambda:[self.updatePatient(),self.addNewUpdateButton(),self.removeNewBackButton()
                                                                                          ,self.removeConfirmUpdateButton()])#add function
        self.confirmUpdateButton.grid(column=1, row=8)
        self.newbackButton = Button(self.root,text="Go Back", command=lambda:[self.removeMainButtons(), self.addStartButtons(),
                                                                           self.removeUpdateButton(), self.removeRemoveButton(),
                                                                           self.removeConfirmUpdateButton(),
                                                                           self.removeNewBackButton()])#add function
        self.newbackButton.grid(column=2, row=8)

        mb.showinfo("Making Changes", "You may begin changing patient information")

        self.name.delete("1.0", "end")
        self.age.delete("1.0", "end")
        self.sex.delete("1.0", "end")
        self.ethnicity.delete("1.0", "end")
        self.language.delete("1.0", "end")
        self.contactinfo.delete("1.0", "end")
        self.dob.delete("1.0", "end")
        self.cc.delete("1.0", "end")
        self.activeProblem.delete("1.0", "end")
        self.vaccination.delete("1.0", "end")
        self.hpi.delete("1.0", "end")
        self.plan.delete("1.0", "end")

        patID = self.patientIDList
        query = "SELECT * FROM patient where patientId = '"+patID+"'"
        self.cursor.execute(query)
        everything = self.cursor.fetchall()
        self.recordsList = everything
        
        self.name.insert("end", self.recordsList[0][1])
        self.age.insert("end", self.recordsList[0][2])
        self.sex.insert("end", self.recordsList[0][3])
        self.ethnicity.insert("end", self.recordsList[0][4])
        self.language.insert("end", self.recordsList[0][5])
        self.contactinfo.insert("end", self.recordsList[0][6])
        self.dob.insert("end", self.recordsList[0][7])
        self.cc.insert("end", self.recordsList[0][8])
        self.activeProblem.insert("end", self.recordsList[0][9])
        self.vaccination.insert("end", self.recordsList[0][10])
        self.hpi.insert("end", self.recordsList[0][11])
        self.plan.insert("end", self.recordsList[0][12])

    def updatePatient(self):
        patID = self.patientIDList

        name = self.name.get(1.0, 'end-1c')
        age = self.age.get(1.0, 'end-1c')
        sex = self.sex.get(1.0, 'end-1c')
        ethnicity = self.ethnicity.get(1.0, 'end-1c')
        language = self.language.get(1.0, 'end-1c')
        contactinfo = self.contactinfo.get(1.0, 'end-1c')
        dob = self.dob.get(1.0, 'end-1c')
        cc = self.cc.get(1.0, 'end-1c')
        activeProblem = self.activeProblem.get(1.0, 'end-1c')
        vaccination = self.vaccination.get(1.0, 'end-1c')
        hpi = self.hpi.get(1.0, 'end-1c')
        plan = self.plan.get(1.0, 'end-1c')

        query = "UPDATE patient SET name = '"+name+"', age = '"+age+"', sex = '"+sex+"', ethnicity = '"+ethnicity+"', language = '"+language+"'"\
                ", contactinfo = '"+contactinfo+"', dob = '"+dob+"', cc='"+cc+"', activeProblem = '"+activeProblem+"', vaccination = '"+vaccination+"',"\
                "hpi = '"+hpi+"', plan = '"+plan+"' WHERE patientId = '"+patID+"'"
        
        self.cursor.execute(query)
        self.sqlConnection.commit()

    def removeRemoveButton(self):
        self.removeButton.grid_forget()

    def insertPatient(self):
        name = self.name.get(1.0, 'end-1c')
        age = self.age.get(1.0, 'end-1c')
        sex = self.sex.get(1.0, 'end-1c')
        ethnicity = self.ethnicity.get(1.0, 'end-1c')
        language = self.language.get(1.0, 'end-1c')
        contactinfo = self.contactinfo.get(1.0, 'end-1c')
        dob = self.dob.get(1.0, 'end-1c')
        cc = self.cc.get(1.0, 'end-1c')
        activeProblem = self.activeProblem.get(1.0, 'end-1c')
        vaccination = self.vaccination.get(1.0, 'end-1c')
        hpi = self.hpi.get(1.0, 'end-1c')
        plan = self.plan.get(1.0, 'end-1c')
        
        query = "INSERT INTO patient (name, age, sex, ethnicity, language, contactinfo, dob, cc, activeProblem, vaccination,hpi, plan) "\
                "VALUES ('"+name+"', '"+age+"','"+sex+"', '"+ethnicity+"','"+language+"',"\
                "'"+contactinfo+"','"+dob+"', '"+cc+"', '"+activeProblem+"','"+vaccination+"', '"+hpi+"', '"+plan+"' )"
        self.cursor.execute(query)
        self.sqlConnection.commit()

        newquery = "SELECT * FROM patient WHERE name = '"+name+"'"
        self.cursor.execute(newquery)
        everything = self.cursor.fetchall()
        self.recordsList = everything
        
        self.name.delete("1.0", "end")
        self.age.delete("1.0", "end")
        self.sex.delete("1.0", "end")
        self.ethnicity.delete("1.0", "end")
        self.language.delete("1.0", "end")
        self.contactinfo.delete("1.0", "end")
        self.dob.delete("1.0", "end")
        self.cc.delete("1.0", "end")
        self.activeProblem.delete("1.0", "end")
        self.vaccination.delete("1.0", "end")
        self.hpi.delete("1.0", "end")
        self.plan.delete("1.0", "end")

        idnumber = str(self.recordsList[0][0])
        patientname = str(self.recordsList[0][1])

        mb.showinfo(""+patientname+"'s ID",""+patientname+"'s ID is: "+idnumber+"")

    def addInsertButton(self):
        self.insertButton = Button(self.root,text="Insert Patient Info",
                                   command =lambda:[self.insertPatient(), self.removeMainButtons(),
                                                    self.addStartButtons(), self.removeInsertButton()])#add function
        self.insertButton.grid(column=3, row=8)

        self.backButton = Button(self.root,text="Go Back",
                                 command=lambda:[self.removeMainButtons(), self.addStartButtons(), self.removeInsertButton()])#add function
        self.backButton.grid(column=2, row=8)
        
    def addMainButtons(self):
        self.nameLabel = Label(self.root, text = "Name of Patient")
        self.name = Text(self.root, height = 3, width = 20, bg="black")
        self.nameLabel.grid(column=1, row=0)
        self.name.grid(column=1, row=1)

        self.ageLabel = Label(self.root, text = "Age of Patient")
        self.age = Text(self.root, height = 3, width = 10, bg="black")
        self.ageLabel.grid(column=2, row=0)
        self.age.grid(column=2, row=1)

        self.sexLabel = Label(self.root, text = "Sex")
        self.sex = Text(self.root, height = 3, width = 10, bg="black")
        self.sexLabel.grid(column=3, row=0)
        self.sex.grid(column=3, row=1)

        self.ethnicityLabel = Label(self.root, text = "Ethnicity")
        self.ethnicity = Text(self.root, height = 3, width = 14, bg="black")
        self.ethnicityLabel.grid(column=4, row=0)
        self.ethnicity.grid(column=4, row=1)

        self.languageLabel = Label(self.root, text = "Preferred Language")
        self.language = Text(self.root, height = 3, width = 15, bg="black")
        self.languageLabel.grid(column=1, row=2)
        self.language.grid(column=1, row=3)

        self.contactinfoLabel = Label(self.root, text = "Contact Information")
        self.contactinfo = Text(self.root, height = 5, width = 20, bg="black")
        self.contactinfoLabel.grid(column=3, row=2)
        self.contactinfo.grid(column=3, row=3)

        self.dobLabel = Label(self.root, text = "Date of Birth")
        self.dob = Text(self.root, height = 3, width = 17, bg="black")
        self.dobLabel.grid(column=2, row=2)
        self.dob.grid(column=2, row=3)

        self.ccLabel = Label(self.root, text = "Chief Complaint")
        self.cc = Text(self.root, height = 20, width = 30, bg="black")
        self.ccLabel.grid(column=1, row=4)
        self.cc.grid(column=1, row=5)

        self.activeProblemLabel = Label(self.root, text = "Active Problems/Diseases")
        self.activeProblem = Text(self.root, height = 20, width = 30, bg="black")
        self.activeProblemLabel.grid(column=2, row=4)
        self.activeProblem.grid(column=2, row=5)

        self.vaccinationLabel = Label(self.root, text = "Immunizations and Dates")
        self.vaccination = Text(self.root, height = 20, width = 30, bg="black")
        self.vaccinationLabel.grid(column=3, row=4)
        self.vaccination.grid(column=3, row=5)

        self.hpiLabel = Label(self.root, text = "History of Present Illness")
        self.hpi = Text(self.root, height = 20, width = 30, bg="black")
        self.hpiLabel.grid(column=1, row=6)
        self.hpi.grid(column=1, row=7)

        self.planLabel = Label(self.root, text = "Assessment and Plan")
        self.plan = Text(self.root, height = 20, width = 30, bg="black")
        self.planLabel.grid(column=2, row=6)
        self.plan.grid(column=2, row=7)

    def addStartButtons(self):

        self.backButton.grid_forget()
        
        self.findPatientButton = Button(self.root,text="Find Patient", command =lambda:[self.findPatient()])#add function
        self.findPatientButton.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.openPatientButton = Button(self.root,text="Open Patient Info",
                                        command =lambda:[self.removeStartButtons(), self.addRemoveButton(),self.addMainButtons(), self.showPatientInfo(), self.addUpdateButton()]
                                        , state = DISABLED)#add function
        self.openPatientButton.place(relx = 0.5, rely = 0.5, y = 30, anchor = CENTER)

        self.newPatientButton = Button(self.root,text="New Patient", command=lambda:[self.removeStartButtons(), self.addMainButtons(), self.addInsertButton()])#add function
        self.newPatientButton.place(relx = 0.5, rely = 0.5, y = 60, anchor = CENTER)

        self.idLabel = Label(text = "ID of Patient")
        self.id = Entry(self.root, bg="black")
        self.idLabel.place(relx = 0.5, rely = 0.5, y= -60, anchor = CENTER)
        self.id.place(relx = 0.5, rely = 0.5, y= -30,anchor = CENTER)

    def findPatient(self):
        patientID = self.id.get()
        self.patientIDList = patientID
        print(self.patientIDList)
        
        query = "SELECT * FROM patient where patientId= '"+self.patientIDList+"'"
        
        self.cursor.execute(query)
        everything = self.cursor.fetchall()
        self.recordsList = everything

        if bool(self.recordsList) == True:
            mb.showinfo("Patient Found", "Patient has been found. Please click the Open Patient Button")
            self.openPatientButton['state']=NORMAL

        elif bool(self.recordsList) == False:
            mb.showinfo("Error Message","Patient with ID of: "+self.patientIDList+" does not exist. Please Try Again")
            self.patientExists = False

    def showPatientInfo(self):
        patID = self.patientIDList
        
        query = "SELECT * FROM patient where patientId = '"+patID+"'"
        self.cursor.execute(query)
        everything = self.cursor.fetchall()
        self.recordsList = everything
        
        self.name.insert("end", self.recordsList[0][1])
        self.age.insert("end", self.recordsList[0][2])
        self.sex.insert("end", self.recordsList[0][3])
        self.ethnicity.insert("end", self.recordsList[0][4])
        self.language.insert("end", self.recordsList[0][5])
        self.contactinfo.insert("end", self.recordsList[0][6])
        self.dob.insert("end", self.recordsList[0][7])
        self.cc.insert("end", self.recordsList[0][8])
        self.activeProblem.insert("end", self.recordsList[0][9])
        self.vaccination.insert("end", self.recordsList[0][10])
        self.hpi.insert("end", self.recordsList[0][11])
        self.plan.insert("end", self.recordsList[0][12])
        
    def removeStartButtons(self):
        self.findPatientButton.place_forget()
        self.idLabel.place_forget()
        self.id.place_forget()
        self.newPatientButton.place_forget()
        self.openPatientButton.place_forget()

    def removeMainButtons(self):
        self.nameLabel.grid_forget()
        self.name.grid_forget()
        self.ageLabel.grid_forget()
        self.age.grid_forget()
        self.sexLabel.grid_forget()
        self.sex.grid_forget()
        self.ethnicityLabel.grid_forget()
        self.ethnicity.grid_forget()
        self.languageLabel.grid_forget()
        self.language.grid_forget()
        self.contactinfoLabel.grid_forget()
        self.contactinfo.grid_forget()
        self.dobLabel.grid_forget()
        self.dob.grid_forget()
        self.ccLabel.grid_forget()
        self.cc.grid_forget()
        self.activeProblemLabel.grid_forget()
        self.activeProblem.grid_forget()
        self.vaccinationLabel.grid_forget()
        self.vaccination.grid_forget()
        self.hpiLabel.grid_forget()
        self.hpi.grid_forget()
        self.planLabel.grid_forget()
        self.plan.grid_forget()
        self.backButton.grid_forget()
  

    def removeUpdateButton(self):
        self.updateButton.grid_forget()

    def removeInsertButton(self):
        self.insertButton.grid_forget()

    def about(self):
        mb.showinfo('About','This program is a rudimentary charting design for people in the medical field')

    def help(self):
        mb.showinfo('Help','Enter your ID \nClick find patient to see if patient with that ID exists \nIf a patient exists click Open Patient Info')

   
    
            
        
    def __init__(self):
        self.recordsList = []
        self.patientIDList = []
        
        self.root = Tk()

        #menu
        menu = Menu(self.root)
        self.root.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Exit")
        menu.add_cascade(label="File", menu=fileMenu)

        dbMenu = Menu(menu)
        dbMenu.add_command(label="Connect Database", command=self.connectDatabase)
        dbMenu.add_command(label="Disconnect Database", command=self.disconnectDatabase)
        dbMenu.add_command(label="Show All Items", command=self.load)
        menu.add_cascade(label="Database", menu=dbMenu)

        helpMenu = Menu(menu)
        helpMenu.add_command(label="Help", command=self.help)
        helpMenu.add_command(label="About", command=self.about)
        menu.add_cascade(label="Help", menu=helpMenu)
        
        #Buttons

        self.findPatientButton = Button(self.root,text="Find Patient", command =lambda:[self.findPatient()])#add function
        self.findPatientButton.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.openPatientButton = Button(self.root,text="Open Patient Info",
                                        command =lambda:[self.removeStartButtons(), self.addRemoveButton(),self.addMainButtons(), self.showPatientInfo(), self.addUpdateButton()]
                                        , state = DISABLED)#add function
        self.openPatientButton.place(relx = 0.5, rely = 0.5, y = 30, anchor = CENTER)

        self.newPatientButton = Button(self.root,text="New Patient", command=lambda:[self.removeStartButtons(), self.addMainButtons(), self.addInsertButton()])#add function
        self.newPatientButton.place(relx = 0.5, rely = 0.5, y = 60, anchor = CENTER)

        self.idLabel = Label(text = "ID of Patient")
        self.id = Entry(self.root, bg="black")
        self.idLabel.place(relx = 0.5, rely = 0.5, y= -60, anchor = CENTER)
        self.id.place(relx = 0.5, rely = 0.5, y= -30,anchor = CENTER)
 
        self.root.wm_title("Patient Database")
        self.root.geometry("1000x1000")
        self.root.mainloop()

def main():
    maingui = gui()

if(__name__=="__main__"):
    main()
