#
# NAME: John Barbour
# SECTION: A2
# GT ID/EMAIL: jbarbour3@gatech.edu / 903038970
# COLLABORATION STATEMENT:
# I worked on this homework alone
# and referred to the following in addition to
# this semester's course materials for CS 2316.
#
#

from tkinter import *
import re
import urllib.request
import base64
import pymysql
from tkinter import messagebox

class Gateway:
    def __init__(self, root):


        self.root = root
        self.username = StringVar()
        self.password = StringVar()
        self.lastname = StringVar()
        self.confirmpassword = StringVar()
        self.currentuser = ''

        #Download and prep the IMAGE
        self.image = None
        response = urllib.request.urlopen("http://www.cc.gatech.edu/classes/AY2015/cs2316_fall/codesamples/techlogo.gif")
        data = response.read()
        response.close()
        img = base64.encodebytes(data)
        self.image = PhotoImage(data=img)

        #---------LOGIN PAGE---------#

        #TITLE
        self.root.title("Login")

        #image
        l = Label(self.root, image=self.image)
        l.pack()

        #USERNAME
        frame1 = Frame(self.root)
        frame1.pack()
        Label(frame1,text="Username:").pack(side=LEFT, anchor=E)
        self.loginusername = Entry(frame1, width=30, textvariable=self.username)
        self.loginusername.pack(side=LEFT)
        Label(frame1,text="          ").pack(side=LEFT, anchor=E)

        #PASSWORD
        frame2 = Frame(self.root)
        frame2.pack()
        Label(frame2,text="Password:").pack(side=LEFT, anchor=E)
        self.loginpassword = Entry(frame2, width=30, textvariable=self.password)
        self.loginpassword.pack(side=LEFT)
        Label(frame2,text="         ").pack(side=LEFT, anchor=E)

        #LOGIN BUTTONS
        frame3 = Frame(self.root)
        frame3.pack(fill=BOTH, expand=True)
        Button(frame3,text="Exit",     command=self.root.destroy).pack(side=RIGHT)
        Button(frame3,text="Login",    command=self.LoginCheck).pack(side=RIGHT)
        Button(frame3,text="Register", command=self.switch).pack(side=RIGHT)


        #----------REGISTER PAGE------------#
        self.root2 = Toplevel()

        #TITLE
        self.root2.title("Room Reservation New User Registration")

        # url = "http://www.or.gatech.edu/images/isye-icon.gif"
        #
        #
        #
        # response = urllib.request.urlopen(url)
        # data = response.read()
        # response.close()
        #
        # img = base64.encodebytes(data)
        # image = PhotoImage(data=img)

        #image
        L = Label(self.root2, image=self.image)
        L.pack()

        #LASTNAME
        framea = Frame(self.root2)
        framea.pack(fill=BOTH, expand=True)
        Label(framea,text="Last Name:           ").pack(side=LEFT)
        self.reglastname = Entry(framea, width=30, textvariable=self.lastname)
        self.reglastname.pack(side=LEFT)
        Label(framea,text="                  ").pack(side=LEFT, anchor=E)

        #USERNAME
        frameb = Frame(self.root2)
        frameb.pack(fill=BOTH, expand=True)
        Label(frameb,text="Username:            ").pack(side=LEFT)
        self.regusername = Entry(frameb, width=30, textvariable=self.username)
        self.regusername.pack(side=LEFT)

        #PASSWORD
        framec = Frame(self.root2)
        framec.pack(fill=BOTH, expand=True)
        Label(framec,text="Password:             ").pack(side=LEFT)
        self.regpassword = Entry(framec, width=30, textvariable=self.password)
        self.regpassword.pack(side=LEFT)

        #CONFIRMPASSWORD
        framed = Frame(self.root2)
        framed.pack(fill=BOTH, expand=True)
        Label(framed,text="Confirm Password:").pack(side=LEFT, anchor=E)
        self.regconfirmpassword = Entry(framed, width=30, textvariable=self.confirmpassword)
        self.regconfirmpassword.pack(side=LEFT)

        #BUTTONS
        framee = Frame(self.root2)
        framee.pack(fill=BOTH, expand=True)
        Button(framee,text="Register", command=self.RegisterNew).pack(side=RIGHT)
        Button(framee,text="Cancel", command=self.switch2).pack(side=RIGHT)

        self.root2.withdraw()

    def Homepage(self):
        self.menu = ('Search Books','Report 1', 'Report 2', 'Damaged Book', 'Frequent Users')
        self.switches = ('SBSwitch', 'R1Switch', 'R2Switch', 'Night')
        self.building = ('CULC','Klaus')
        # self.floor = (1, 2, 3, 4)
        # self.room = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        # self.currentreservation1=StringVar()
        # self.currentreservation1.set('')
        # self.currentreservation2=StringVar()
        # self.currentreservation2.set('')

        self.root3 = Toplevel()
        self.root3.title("GT Library Management System")


        #---top menu---#
        self.root3.topframe = Frame(self.root3)
        self.root3.topframe.pack()

        Button(self.root3.topframe, text='Search Book', command=self.SearchBook).pack(side=LEFT)
        Button(self.root3.topframe, text='Request Extension', command=self.RequestExtension).pack(side=LEFT)
        Button(self.root3.topframe, text='Future Hold Request', command=self.FutureHoldRequest).pack(side=LEFT)
        Button(self.root3.topframe, text='Track Book Location', command=self.TrackBookLocation).pack(side=LEFT)
        Button(self.root3.topframe, text='Checkout', command=self.Checkout).pack(side=LEFT)
        Button(self.root3.topframe, text='Return', command=self.Return).pack(side=LEFT)

        #---bottom menu---#
        self.root3.bottomframe = Frame(self.root3)
        self.root3.bottomframe.pack()

        Button(self.root3.bottomframe, text='Search Bookd', command=self.Logout).pack(side=LEFT)






        frameA=Frame(self.root3)
        frameA.pack(expand=True,fill=BOTH)
        self.root3.reservedisplay=Entry(frameA, width=50, textvariable=self.currentreservation1, state='readonly')
        self.root3.reservedisplay.pack(side=RIGHT)
        Label(frameA,text='Current Reservations:').pack(side=RIGHT)

        # #only do this if there are 2 reservations
        self.frameB=Frame(self.root3)
        self.frameB.pack(expand=True,fill=BOTH)
        # self.root3.reservedisplay2=Entry(frameB, width=50, textvariable=self.currentreservation2, state='readonly')
        # self.root3.reservedisplay2.pack(side=RIGHT)


        frameC=Frame(self.root3)
        frameC.pack(expand=True,fill=BOTH)
        Label(frameC,text='Make New Reservations:').pack(side=LEFT)


        ###----------START OF FRAMED BUTTONS--------####
        frameD=Frame(self.root3)
        frameD.pack(anchor=E)

        #the 5 days
        self.dayChoice=IntVar()
        frameDay=Frame(frameD, relief=SUNKEN, bd=2)
        frameDay.pack(side=LEFT,anchor=NE, padx=2)
        Label(frameDay,text='Day Choices:').pack()
        for item in self.day:
            Radiobutton(frameDay,text=item, variable=self.dayChoice, value=self.day.index(item)).pack(anchor=W)
        self.dayChoice.set(99)

        #the 4 times
        self.timeChoice=IntVar()
        frameTime=Frame(frameD, relief=SUNKEN, bd=2)
        frameTime.pack(side=LEFT,anchor=NE, padx=2)
        Label(frameTime,text='Time Choices:').pack()
        for item in self.time:
            Radiobutton(frameTime,text=item, variable=self.timeChoice, value=self.time.index(item)).pack(anchor=W)
        self.timeChoice.set(99)

        #the 2 buildings
        self.buildingChoice=IntVar()
        frameBuilding=Frame(frameD, relief=SUNKEN, bd=2)
        frameBuilding.pack(side=LEFT,anchor=NE, padx=2)
        Label(frameBuilding,text='Building Choices:').pack()
        for item in self.building:
            Radiobutton(frameBuilding,text=item, variable=self.buildingChoice, value=self.building.index(item)).pack()
        self.buildingChoice.set(99)

        #the 4 floors
        self.floorChoice=IntVar()
        frameFloor=Frame(frameD, relief=SUNKEN, bd=2)
        frameFloor.pack(side=LEFT,anchor=NE, padx=2)
        Label(frameFloor,text='Floor Choices:').pack()
        for i in range(1,5):
            Radiobutton(frameFloor,text=str(i), variable=self.floorChoice, value=i).pack()
        self.floorChoice.set(99)

        #the 10 rooms
        self.roomChoice=IntVar()
        frameRoom=Frame(frameD, relief=SUNKEN, bd=2)
        frameRoom.pack(side=LEFT,anchor=NE, padx=2)
        frameRoomTop=Frame(frameRoom)
        frameRoomTop.pack()
        frameRoomBottom=Frame(frameRoom)
        frameRoomBottom.pack()
        Label(frameRoomTop,text='Room Choices:').pack()
        for i in range(1,6):
            Radiobutton(frameRoomBottom,text=str(i), variable=self.roomChoice, value=i).grid(column=0, row=i)

        for i in range(6,11):
            Radiobutton(frameRoomBottom,text=str(i), variable=self.roomChoice, value=i).grid(column=1, row=(i-5))

        self.roomChoice.set(99)



        self.root3.bottom = Frame(self.root3)
        self.root3.bottom.pack(side=BOTTOM, expand=True, fill=BOTH)
        Button(self.root3.bottom, text='Logout', command=self.Logout).pack(side=RIGHT)
        Button(self.root3.bottom, text='Stats', command=self.stats).pack(side=RIGHT)
        Button(self.root3.bottom, text='Check Available Options', command=self.availableReservations).pack(side=RIGHT)
        Button(self.root3.bottom, text='Cancel All Reservations', command=self.cancelReservation).pack(side=RIGHT)

        self.displayReservations()

    def displayReservations(self):
        #get the number of reservations the user has already
        c=self.Connect()

        sql = 'SELECT * FROM RoomReservations WHERE ReservedBy =%s'
        c.execute(sql,self.currentuser)
        stuff = []
        for item in c:
            #print(item)
            stuff.append(item)
        self.reservations = len(stuff)
        i = self.reservations

        if i ==0:
            self.currentreservation1.set('No Reservations')
        elif i == 1:
            self.currentreservation1.set("Room {0} on {1} Floor {2} is reserved for {3} at {4} hours.".format(stuff[0][2],stuff[0][0],stuff[0][1],stuff[0][3],stuff[0][4]))
        else:
            self.currentreservation1.set("Room {0} on {1} Floor {2} is reserved for {3} at {4} hours.".format(stuff[1][2],stuff[1][0],stuff[1][1],stuff[1][3],stuff[1][4]))
            self.root3.reservedisplay2=Entry(self.frameB, width=50, textvariable=self.currentreservation2, state='readonly')
            self.root3.reservedisplay2.pack(side=RIGHT)
            self.currentreservation2.set("Room {0} on {1} Floor {2} is reserved for {3} at {4} hours.".format(stuff[0][2],stuff[0][0],stuff[0][1],stuff[0][3],stuff[0][4]))

    def Logout(self):
        #closes the Homepage window and returns the
        self.root3.destroy()

        self.root.deiconify()
        pass

    def stats(self):
        self.root3.withdraw()
        self.root5 = Toplevel()
        self.root5.title("Statistics")
        self.stat1=StringVar()
        self.stat2=StringVar()
        one = Frame(self.root5)
        one.pack(anchor=E)
        Entry(one,textvariable=self.stat1,state='readonly').pack(side=RIGHT)
        Label(one,text="The average number of reservations per person is:").pack(side=RIGHT)

        two = Frame(self.root5)
        two.pack(anchor=E)
        Entry(two,textvariable=self.stat2,state='readonly').pack(side=RIGHT)
        Label(two,text="The Busiest Building:").pack(side=RIGHT)

        Button(self.root5,text="          Back                    ", command=self.switch4).pack()

        c = self.Connect()
        sql = "SELECT AVG(NumberOfReservations) FROM ReservationUser"
        c.execute(sql)
        for item in c:
            avg = item[0]
            self.stat1.set(str(avg))

        a=c.execute("SELECT * FROM RoomReservations WHERE Building=%s",'CULC')
        b=c.execute("SELECT * FROM RoomReservations WHERE Building=%s",'Klaus')
        print(a,b)

        c.close()
        if a==b:
            self.stat2.set("Both are busy with " + str(a) + " reservations so far.")
        elif a>b:
            self.stat2.set("CULC is more busy with " + str(a) + " reservations so far.")
        else:
            self.stat2.set("Klaus is more busy with " + str(b) + " reservations so far.")

    def availableReservations(self):
        if self.reservations == 2:
            messagebox.showerror('Error', 'You can only make 2 reservations per week. Try again next week.')
        else:
            choices = (self.buildingChoice.get(),self.floorChoice.get(),self.roomChoice.get(),self.dayChoice.get(),self.timeChoice.get())
            if 99 in choices:
                messagebox.showwarning('Search Failure','Please choose a valid option from each category.')
            else:
                self.values = (self.building[self.buildingChoice.get()],self.floorChoice.get(),self.roomChoice.get(),self.day[self.dayChoice.get()])
                print(self.values)
                #query the room for the time frame...
                c = self.Connect()
                sql = "SELECT Time FROM RoomReservations WHERE Building=%s AND Floor=%s AND RoomNo=%s AND Day=%s"
                c.execute(sql,self.values)
                times = []
                for time in c:
                    times.append(time[0])
                c.close()
                print("these are the times from the sql ", times)
                if len(times)>=4:
                    messagebox.showwarning('Search Failure','This Room is unavailable for the selected day and time')
                else:
                    #make the reservation window
                    self.root3.withdraw()
                    self.root4 = Toplevel()
                    self.root4.title("Available Rooms")
                    wtf = Frame(self.root4)
                    wtf.pack(anchor=E)
                    Label(wtf,text='Building',bd=3,relief=RAISED).pack(side=LEFT,expand=True,fill=BOTH)
                    Label(wtf,text=' Floor ',bd=3,relief=RAISED).pack(side=LEFT,expand=True,fill=BOTH)
                    Label(wtf,text=' Room ',bd=3,relief=RAISED).pack(side=LEFT,expand=True,fill=BOTH)
                    Label(wtf,text='    Day    ',bd=3,relief=RAISED).pack(side=LEFT,expand=True,fill=BOTH)
                    Label(wtf,text='   Time   ',bd=3,relief=RAISED).pack(side=LEFT,expand=True,fill=BOTH)
                    Label(wtf,text='Select',bd=3,relief=RAISED).pack(side=LEFT,expand=True,fill=BOTH)
                    self.crapvariable = IntVar()
                    self.crapvariable.set(99)
                    x = self.timeChoice.get()
                    if x==0:
                        self.xvalue=['08:00','09:00','10:00','11:00']
                    elif x==1:
                        self.xvalue=['12:00','13:00','14:00','15:00']
                    elif x==2:
                        self.xvalue=['16:00','17:00','18:00','19:00']
                    else:
                        self.xvalue=['20:00','21:00','22:00','23:00']

                    wtf2 = Frame(self.root4)
                    wtf2.pack(expand=True,fill=BOTH,anchor=E)
                    z=1
                    for item in self.xvalue:
                        print(item)
                        if item not in times:
                            print(item)
                            Radiobutton(wtf2, variable=self.crapvariable, value=self.xvalue.index(item)).grid(row=z,column=5)
                            Label(wtf2,text="   "+ str(self.values[0])).grid(row=z,column=0)
                            Label(wtf2,text="      "+ str(self.values[1])).grid(row=z,column=1)
                            Label(wtf2,text="         "+ str(self.values[2])).grid(row=z,column=2)
                            Label(wtf2,text="      "+self.values[3]).grid(row=z,column=3)
                            Label(wtf2,text="  " + str(item) + "       ").grid(row=z,column=4)
                            z+=1
                    wtf3 = Frame(self.root4)
                    wtf3.pack(anchor=E)
                    Button(wtf3,text='Cancel',command=self.switch3).pack(side=RIGHT)
                    Button(wtf3,text='Submit Reservation',command=self.makeReservation).pack(side=RIGHT)

    def makeReservation(self):
        if self.crapvariable.get()==99:
            messagebox.showinfo('Reservation Incomplete','You must select a time for the reservation.')
        else:
            print((self.values[0],self.values[1],self.values[2],self.values[3],self.xvalue[self.crapvariable.get()],self.currentuser))
            c = self.Connect()
            sql = "INSERT INTO RoomReservations (Building, Floor, RoomNo, Day, Time, ReservedBy) Values (%s, %s, %s, %s, %s, %s)"
            c.execute(sql,(self.values[0],self.values[1],self.values[2],self.values[3],self.xvalue[self.crapvariable.get()],self.currentuser))


            sql = "Select NumberOfReservations From ReservationUser WHERE USERNAME=%s"
            c.execute(sql,(self.currentuser))

            for item in c:
                newvalue=int(item[0])
            newvalue+=1

            sql = "UPDATE ReservationUser SET NumberOfReservations=%s WHERE USERNAME=%s"
            c.execute(sql,(str(newvalue),self.currentuser))

            c.close()
            messagebox.showinfo('Reservation Complete','Congratulations, you have reserved your room. Click ok to go back to the homepage.')
            self.root4.destroy()
            self.root3.deiconify()

    def LoginCheck(self):
        usrname = self.username.get()#get credentials from the login entries
        passwrd = self.password.get()
        self.currentuser = self.username.get()

        #clear out credentials after retrieval
        self.clear()

        c=self.Connect()#create the database connection object
        sql = "SELECT username, password FROM User WHERE username= %s AND password= %s"
        a = c.execute(sql, (usrname, passwrd))

        contains = False
        if a != 0:
            for item in c:#check all the possible matches for
                if item[0]==usrname:
                    if item[1]==passwrd:
                        contains=True

        if contains:
            messagebox.showinfo("Login Successful", "Welcome to the Library Management System.")
            self.root.withdraw()
            self.Homepage()

        else:
            messagebox.showerror("Login Unsuccessful","Not found, please enter a different username/password")
        c.close()

    def cancelReservation(self):
        c=self.Connect()
        sql = "DELETE FROM RoomReservations WHERE ReservedBy = %s"
        c.execute(sql,self.currentuser)


        sql = "Select NumberOfReservations From ReservationUser WHERE USERNAME=%s"
        c.execute(sql,(self.currentuser))

        for item in c:
            newvalue=int(item[0])
        if newvalue != 0:
            sql = "UPDATE ReservationUser SET NumberOfReservations=%s WHERE USERNAME=%s"
            c.execute(sql,(0,self.currentuser))
            messagebox.showwarning("Succesful","Congratulations. You have deleted your reservations.")
            self.currentreservation1.set("No Reservations")
            try:
                self.currentreservation2.set("")
            except:
                pass
        else:
            messagebox.showerror("Error","There are currently no reservations to cancel.")

        c.close()

    def switch(self):
        self.clear()
        self.root.withdraw()
        self.root2.deiconify()

    def switch2(self):
        self.clear()
        self.root2.withdraw()
        self.root.deiconify()

    def switch3(self):
        self.root4.destroy()
        self.root3.deiconify()

    def switch4(self):
        self.root5.destroy()
        self.root3.deiconify()

    def clear(self):
        self.lastname.set("")
        self.username.set("")
        self.password.set("")
        self.confirmpassword.set("")

    def RegisterNew(self):
        valid = True
        #get register entries and put them into database
        lastname = self.lastname.get()
        username = self.username.get()
        password = self.password.get()
        confirmpassword = self.confirmpassword.get()

        #clear the form...
        self.clear()


        #make sure username/password entries have values
        if username=='' or password=='' or confirmpassword=='':
            valid = False
            messagebox.showerror("Missing items.", "You must specify a username, password, and confirm password. ")

        else:
            if len(username)>15:
                valid=False
                messagebox.showerror("Invalid Username","Username too long. Must be 15 characters or less.")
            else:
                #make sure password has one upper case letter and one number
                if re.search('[A-Z]',password) and re.search('[A-Z]',password):
                    #check to make sure passwords match
                    if password != confirmpassword:
                        valid = False
                        messagebox.showerror("Password error", "Password and confirm password must match.")
                    else:
                        #check for a duplicate username in the database
                        c=self.Connect()
                        sql = "SELECT * FROM ReservationUser WHERE Username= %s"
                        a= c.execute(sql,username)
                        print(a)
                        if a>0:
                            valid=False
                            messagebox.showerror("Username taken", "Please select another username...")
                            # for item in c:
                            #     print(username)
                            #     print(item)
                            #     if item[0]==username:
                            #         valid = False
                            #         messagebox.showerror("Username taken", "Please select another username...")
                            # c.close()
                else:
                    valid = False
                    messagebox.showerror("Password error", "Password must contain an uppercase letter and number")

        #Insert info into database, remember .commit()
        if valid:
            c = self.Connect()
            sql = "INSERT INTO ReservationUser (lastname, username, password) VALUES (%s, %s, %s)"
            c.execute(sql,(lastname, username, password))
            self.db.commit()
            c.close()

            #confirm registration, hide reg window and present login window
            messagebox.showinfo("Success","You have successfully registered you may now log in.")
            self.clear()
            self.root2.withdraw()
            self.root.deiconify()

    def Connect(self):
        #this points to the connection object, this way we can get a cursor from db.cursor()
        try:
            self.db = pymysql.connect(
                db='cs4400_Group_60',
                user='cs4400_Group_60',
                passwd='XoYOzC_l',
                host='academic-mysql.cc.gatech.edu'
            )
            c=self.db.cursor()
            return c
        except:
            messagebox.showerror("No connection!", "Can't connect to the database. Please check the internet connection.(If you're not on GTwifi, is your VPN running?)")
            return None

    

win = Tk()
app = Gateway(win)
win.mainloop()
