from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
from datetime import datetime,date,timedelta
from datetime import datetime
#date=datetime.datetime.date()

conn= sqlite3.connect("Finexdb.db")
c= conn.cursor()
result=c.execute("select max(serial) from user")
for r in result:
    serial=r[0]

# c.execute("CREATE TABLE user(userid INTEGER PRIMARY KEY, username TEXT, group TEXT")
# conn.commit()
class Userinfo:
    def __init__(self,master,*args,**kwargs):


        self.master=master
        self.heading = Label(master,text="Add Users",font=('arial 40 bold'),fg='steelblue')
        self.heading.place(x=450,y=0)

        self.s=Label(master,text="Serial has reached upto "+str(serial),font=('arial 10 bold'),fg='steelblue')
        self.s.place(x=0,y=30)
        #labels and entries
        self.serial_l=Label(master,text="Enter Serial",font=('arial 18 bold') )
        self.serial_l.place(x=0,y=50)

        self.user_id_l = Label(master, text="User ID", font=('arial 18 bold'))
        self.user_id_l.place(x=0, y=100)

        self.user_name_l = Label(master, text="User Name", font=('arial 18 bold'))
        self.user_name_l.place(x=0, y=150)

        self.group_l = Label(master, text="Enter Group", font=('arial 18 bold'))
        self.group_l.place(x=0, y=200)

        self.joining_date_l = Label(master, text="Joining Date", font=('arial 18 bold'))
        self.joining_date_l.place(x=0, y=250)

        self.address_l = Label(master, text="Address", font=('arial 18 bold'))
        self.address_l.place(x=0, y=300)

        self.nid_l = Label(master, text="Enter NID", font=('arial 18 bold'))
        self.nid_l.place(x=0, y=350)

        self.phone_l = Label(master, text="Phone Number", font=('arial 18 bold'))
        self.phone_l.place(x=0, y=400)

        self.email_l = Label(master, text="Enter Email", font=('arial 18 bold'))
        self.email_l.place(x=0, y=450)
        self.spd_l = Label(master, text="Saving per Day", font=('arial 10 bold'))
        self.spd_l.place(x=0, y=490)
        self.suid_l = Label(master, text="Search user id", font=('arial 10 bold'))
        self.suid_l.place(x=0, y=530)
        #entry
        self.serial_e = Entry(master,width=15, font=('arial 18 bold'))
        self.serial_e.place(x=250, y=50)

        self.user_id_e = Entry(master, width=25, font=('arial 18 bold'))
        self.user_id_e.place(x=250, y=100)
        self.user_name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.user_name_e.place(x=250, y=150)
        self.group_e = Entry(master, width=25, font=('arial 18 bold'))
        self.group_e.place(x=250, y=200)
        self.joining_date_e = Entry(master, width=25, font=('arial 18 bold'))
        self.joining_date_e.place(x=250, y=250)
        self.address_e = Entry(master, width=25, font=('arial 18 bold'))
        self.address_e.place(x=250, y=300)
        self.nid_e = Entry(master, width=25, font=('arial 18 bold'))
        self.nid_e.place(x=250, y=350)
        self.phone_e = Entry(master, width=25, font=('arial 18 bold'))
        self.phone_e.place(x=250, y=400)
        self.email_e = Entry(master, width=25, font=('arial 18 bold'))
        self.email_e.place(x=250, y=450)
        self.spd_e = Entry(master, width=15, font=('arial 12 bold'))
        self.spd_e.place(x=250, y=490)

        self.user_sid_e = Entry(master, width=10, font=('arial 18 bold'))
        self.user_sid_e.place(x=100, y=530)


        #btn
        self.btn_add= Button(master,text="ADD USER",width=18,height=2,bg='steelblue',fg='white',command=self.get_user)
        self.btn_add.place(x=450,y=500)

        self.btn_clr = Button(master, text="CLEAR ALL FIELD", width=15, height=2, bg='green', fg='white',
                              command=self.clear_all)
        self.btn_clr.place(x=600, y=500)
        self.btn_upd = Button(master, text="UPDATE USER", width=15, height=2, bg='steelblue', fg='white',
                              command=self.update)
        self.btn_upd.place(x=250, y=600)
        self.btn_search = Button(master, text="SEARCH", width=10, height=2, bg='yellow', fg='black',
                                 command=self.search)
        self.btn_search.place(x=250, y=530)
        self.btn_dlt = Button(master, text="Delete User", width=10, height=2, bg='yellow', fg='black',
                                 command=self.dlt)
        self.btn_dlt.place(x=350, y=530)
        #textbox
        self.tbox=Text(master,width=70,height=25)
        self.tbox.place(x=600,y=70)
        #self.tbox.insert(END,"Serial has reached upto"+str(serial))

        # self.master.bind('<Return>',self.get_user)
        # self.master.bind('<up>',self.clear_all)

    def get_user(self,*args,**kwargs):

        #getfromentries
        self.serial=self.serial_e.get()
        self.user_id=self.user_id_e.get()
        self.user_name=self.user_name_e.get()
        self.grp=self.group_e.get()
        self.joining_dat=self.joining_date_e.get()
        self.joining_date=datetime.strptime(self.joining_dat, "%d/%m/%Y").date()

        self.address=self.address_e.get()
        self.nid=self.nid_e.get()
        self.phone=self.phone_e.get()
        self.email=self.email_e.get()
        self.spd=self.spd_e.get()

        if self.serial =='' or self.user_id=='' :#or self.user_name=='' or self.grp=='' or self.joining_date==''or self.address =='' or self.nid==''or self.phone=='':
            tkinter.messagebox.showinfo("Error","please fill required field.")
        else:
            #sql = 'insert into user(serial,user_id,user_name,group,joining_date,address,nid,phone,email) values(?,?,?,?,?,?,?,?,?)'
            c.execute("INSERT INTO user VALUES(?,?,?,?,?,?,?,?,?,?)",(self.serial, self.user_id, self.user_name, self.grp,self.joining_date,self.address,self.nid,self.phone,self.email,self.spd))
            conn.commit()
            tkinter.messagebox.showinfo("success"," successfully added")
            self.tbox.insert(END,"\n\nUser Name " + str(self.user_name)+" User ID " +str(self.user_id) + " is added into Database.")
            self.tbox.insert(END, '\n Serial          ' + str(self.serial))
            self.tbox.insert(END, '\n Group           ' + str(self.grp))
            self.tbox.insert(END, '\n Joining Date    ' + str(self.joining_date))
            self.tbox.insert(END, '\n Address         ' + str(self.address))
            self.tbox.insert(END, '\n NID             ' + str(self.nid))
            self.tbox.insert(END, '\n Phone           ' + str(self.phone))
            self.tbox.insert(END, '\n Email           ' + str(self.email))



    def clear_all(self,*args,**kwargs):
        self.serial_e.delete(0,END)
        self.user_id_e.delete(0,END)
        self.user_name_e.delete(0,END)
        self.group_e.delete(0,END)
        self.joining_date_e.delete(0,END)
        self.address_e.delete(0,END)
        self.nid_e.delete(0,END)
        self.phone_e.delete(0,END)
        self.email_e.delete(0,END)
        self.spd_e.delete(0,END)

    def search(self,*args,**kwargs):
        sql="select * from user where user_id=?"
        result=c.execute(sql,(self.user_sid_e.get(), ))
        for r in result:
            self.n1=r[0]#serial
            self.n2 = r[2]  # name
            self.n3 = r[3]  # group
            self.n4 = r[4]  # joiningdate
            self.n5 = r[5]  # serial
            self.n6 = r[6]  # serial
            self.n7=r[7]
            self.n8 = r[8]  # serial
            self.n9 = r[9]  # serial
        conn.commit()
        self.serial_e.delete(0, END)
        self.serial_e.insert(0, str(self.n1))
        self.user_name_e.delete(0,END)
        self.user_name_e.insert(0,str(self.n2))

        self.group_e.delete(0, END)
        self.group_e.insert(0, str(self.n3))
        self.joining_date_e.delete(0, END)
        self.joining_date_e.insert(0, str(self.n4))
        self.address_e.delete(0, END)
        self.address_e.insert(0, str(self.n5))
        self.nid_e.delete(0, END)
        self.nid_e.insert(0, str(self.n6))
        self.phone_e.delete(0, END)
        self.phone_e.insert(0, str(self.n7))
        self.email_e.delete(0, END)
        self.email_e.insert(0, str(self.n8))
        self.spd_e.delete(0,END)
        self.spd_e.insert(0,str(self.n9))

    def update(self,*args,**kwargs):
        self.u1=self.serial_e.get()
        self.u2=self.user_name_e.get()
        self.u3=self.group_e.get()
        self.uu=self.joining_date_e.get()
        self.u4=datetime.strptime(self.uu, "%d/%m/%Y").date()
        self.u5=self.address_e.get()
        self.u6=self.nid_e.get()
        self.u7=self.phone_e.get()
        self.u8=self.email_e.get()
        self.u9=self.spd_e.get()


        query="UPDATE user SET serial=?,user_name=?,grp=?,joining_date=?,address=?,nid=?,phone=?,email=?,saving_pd=? WHERE user_id=?"
        c.execute(query,(self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.u7,self.u8,self.u9,self.user_sid_e.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success" , "Update the database")
    def dlt(self,*args,**kwargs):
        sql = " delete from user where user_id=?"
        c.execute(sql, (self.user_sid_e.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted From database")


root=Tk()
b= Userinfo(root)

root.geometry("1280x720+0+0")
root.title("Add user ")
root.mainloop()
