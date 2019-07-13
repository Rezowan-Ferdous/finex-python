from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
from datetime import datetime,date,timedelta
from tkinter import Frame

date=datetime.today().date()
conn= sqlite3.connect("Finexdb.db")

c= conn.cursor()

# c.execute("CREATE TABLE sales(userid INTEGER PRIMARY KEY, username TEXT, group TEXT")
# conn.commit()

slb=[]
result=c.execute("select max(serial) from sales")
for r in result:
    serial=r[0]

class Salesinfo:


    def __init__(self,master,*args,**kwargs):
        self.datetime=datetime.date


        self.master=master
        self.heading = Label(master,text="Druto Loan ",font=('arial 40 bold'),fg='green')
        self.heading.place(x=450,y=0)

        self.s=Label(master,text="Serial has reached upto "+str(serial),font=('arial 10 bold'),fg='steelblue')
        self.s.place(x=0,y=30)
        #labels and entries
        self.user_id_l = Label(master, text="User ID", font=('arial 12 bold'))
        self.user_id_l.place(x=0, y=50)

        self.serial_l=Label(master,text="Enter Serial",font=('arial 12 bold') )
        self.serial_l.place(x=0,y=100)




        self.lending_date_l = Label(master, text="Lending Date y/m/d", font=('arial 15 bold'))
        self.lending_date_l.place(x=0, y=150)

        self.slab_l = Label(master, text="Slab No", font=('arial 15 bold'))
        self.slab_l.place(x=0, y=200)

        self.amount_l = Label(master, text="Amount", font=('arial 15 bold'))
        self.amount_l.place(x=0, y=250)

        self.repay_date_l = Label(master, text="Repay Date", font=('arial 15 bold'))
        self.repay_date_l.place(x=0, y=300)

        self.lending_period_l = Label(master, text="Landing week", font=('arial 15 bold'))
        self.lending_period_l.place(x=0, y=350)

        # self.weekly_fee_l = Label(master, text="Weekly Fee", font=('arial 15 bold'))
        # self.weekly_fee_l.place(x=0, y=400)

        self.status_l = Label(master, text="Status Fee", font=('arial 15 bold'))
        self.status_l.place(x=0, y=400)
        self.status_dl = Label(master, text="Status DL", font=('arial 15 bold'))
        self.status_dl.place(x=0, y=450)
        #frame
        self.right=Frame(master,width=520,height=750,bg='lightblue')
        self.right.pack(side=RIGHT)

        self.id_l = Label(self.right, text="user ID", font=('arial 15 bold'),bg='lightblue', fg='black')
        self.id_l.place(x=40, y=50)

        self.date_l=Label(self.right,text="today's Date: "+str(date),font=('arial 10 bold '),bg='lightblue',fg='white')
        self.date_l.place(x=0,y=0)
        self.sl_ll = Label(self.right, text="SL", font=('arial 10 bold '), bg='lightblue', fg='black')
        self.sl_ll.place(x=0, y=100)
        self.name_ll = Label(self.right, text="name", font=('arial 10 bold '), bg='lightblue',fg='black')
        self.name_ll.place(x=20, y=100)
        self.slabs_ll = Label(self.right, text="slabs", font=('arial 10 bold '), bg='lightblue', fg='black')
        self.slabs_ll.place(x=80, y=100)
        self.rep_dt_ll = Label(self.right, text="Repay Date", font=('arial 10 bold '), bg='lightblue', fg='black')
        self.rep_dt_ll.place(x=150, y=100)
        self.fee_ll = Label(self.right, text="subscr. Fee", font=('arial 10 bold '), bg='lightblue', fg='black')
        self.fee_ll.place(x=250, y=100)
        self.stts_ll = Label(self.right, text="Status_FEE ", font=('arial 10 bold '), bg='lightblue', fg='black')
        self.stts_ll.place(x=350, y=100)
        self.stts_dl = Label(self.right, text="Status_DL ", font=('arial 10 bold '), bg='lightblue', fg='black')
        self.stts_dl.place(x=450, y=100)


        # self.name_l = Label(self.right, text="", font=('arial 10 bold '), bg='lightblue', fg='green')
        # self.name_l.place(x=20, y=200)
        # self.slabs_l = Label(self.right, text="", font=('arial 10 bold '), bg='lightblue', fg='green')
        # self.slabs_l.place(x=80, y=200)
        # self.rep_dt_l = Label(self.right, text="", font=('arial 10 bold '), bg='lightblue', fg='green')
        # self.rep_dt_l.place(x=150, y=200)
        # self.fee_l = Label(self.right, text="", font=('arial 10 bold '), bg='lightblue', fg='green')
        # self.fee_l.place(x=250, y=200)
        self.stts_l = Label(master, text="serial", font=('arial 10 bold '))
        self.stts_l.place(x=0, y=500)
        #entry
        self.serial_id_e = Entry(master, width=8, font=('arial 15 bold'))
        self.serial_id_e.place(x=80, y=500)
        self.user_id_e = Entry(master, width=15, font=('arial 15 bold'))
        self.user_id_e.place(x=250, y=50)
        self.user_id_e.focus()
        self.serial_e = Entry(master,width=15, font=('arial 15 bold'))
        self.serial_e.place(x=250, y=100)
        self.id_e = Entry(self.right, width=15, font=('arial 15 bold'))
        self.id_e.place(x=120, y=50)



        self.lending_date_e = Entry(master, width=25, font=('arial 15 bold'))
        self.lending_date_e.place(x=250, y=150)


        self.slab_e = Entry(master, width=25, font=('arial 15 bold'))
        self.slab_e.place(x=250, y=200)
        self.amount_e = Entry(master, width=25, font=('arial 15 bold'))
        self.amount_e.place(x=250, y=250)
        self.repay_date_e = Entry(master, width=25, font=('arial 15 bold'))
        self.repay_date_e.place(x=250, y=300)
        self.lending_period_e = Entry(master, width=25, font=('arial 15 bold'))
        self.lending_period_e.place(x=250, y=350)
        # self.weekly_fee_e = Entry(master, width=25, font=('arial 15 bold'))
        # self.weekly_fee_e.place(x=250, y=400)
        self.status_e = Entry(master, width=25, font=('arial 15 bold'))
        self.status_e.place(x=250, y=400)
        self.status_dle = Entry(master, width=25, font=('arial 15 bold'))
        self.status_dle.place(x=250, y=450)

        #btn
        self.btn_adds= Button(master,text="ADD sales",width=20,height=2,bg='steelblue',fg='white',command=self.get_sales)
        self.btn_adds.place(x=400,y=500)

        self.btn_clr = Button(master, text="CLEAR ALL FIELD", width=20, height=2, bg='green', fg='white',
                              command=self.clear_all)
        self.btn_clr.place(x=400, y=550)
        self.btn_search = Button(master, text="SEARCH", width=15, height=2, bg='yellow', fg='black',
                                 command=self.ajax)
        self.btn_search.place(x=1100, y=50)
        self.btn_srch = Button(master, text="SEARCH", width=15, height=2, bg='yellow', fg='black',
                                 command=self.search)
        self.btn_srch.place(x=180, y=500)
        self.btn_upd = Button(master, text="UPDATE", width=10, height=2, bg='green', fg='black',command=self.update)
        self.btn_upd.place(x=100, y=550)
        self.btn_dlt = Button(master, text="Delete Sales", width=10, height=2, bg='yellow', fg='black',
                              command=self.dlt)
        self.btn_dlt.place(x=250, y=550)
        #text bix
        self.tbox = Text(self.right, width=70, height=25)
        self.tbox.place(x=0, y=150)

    def get_sales(self, *args, **kwargs):

        # getfromentries
        self.id=self.id_e.get()
        self.serial = self.serial_e.get()
        self.user_id = self.user_id_e.get()

        self.lending_dat = self.lending_date_e.get()
        self.lending_date=datetime.strptime(self.lending_dat, "%d/%m/%Y").date()
        # self.year, self.month, self.day = map(int, self.lending_date.split('/'))
        # self.date1= self.datetime.date(year=self.year, month=self.month, day=self.day)


        self.slab = self.slab_e.get()
        #self.slab=[{'1':30,'2':70,'3':115,'4':145,'5':195}]
        weekfee = c.execute("SELECT weekly_fee from dl where slab = ? ", (self.slab,))
        for self.w in weekfee:
            self.getweekfee = self.w[0]


        self.repay_dat = self.repay_date_e.get()
        self.repay_date = datetime.strptime(self.repay_dat, "%d/%m/%Y").date()
        self.lending_period = self.lending_period_e.get()
        self.status = self.status_e.get()
        self.amount = self.amount_e.get()
        self.statusdl=self.status_dle.get()
        self.weekly_fee =self.getweekfee

        #dynamic field
        self.subs_fee=int(self.weekly_fee)*int(self.lending_period)



        if self.serial == '' or self.user_id == '':  # or self.user_name=='' or self.grp=='' or self.joining_date==''or self.address =='' or self.nid==''or self.phone=='':
            tkinter.messagebox.showinfo("Error", "please fill required field.")
        else:
            # sql = 'insert into user(serial,user_id,user_name,group,joining_date,address,nid,phone,email) values(?,?,?,?,?,?,?,?,)'
            c.execute("INSERT INTO sales VALUES(?,?,?,?,?,?,?,?,?,?,?)",( self.serial,self.user_id, self.lending_date, self.slab, self.amount, self.repay_date, self.lending_period,self.weekly_fee,self.subs_fee,
            self.status,self.statusdl))
            conn.commit()
            tkinter.messagebox.showinfo("success", " successfully added")

    def clear_all(self, *args, **kwargs):
        self.serial_e.delete(0, END)
        self.user_id_e.delete(0, END)
        self.lending_period_e.delete(0, END)
        self.lending_date_e.delete(0, END)
        self.slab_e.delete(0, END)
        self.amount_e.delete(0, END)
        self.repay_date_e.delete(0, END)
        self.lending_period_e.delete(0, END)
        self.status_e.delete(0, END)
        self.status_dle.delete(0, END)

    # def search(self, *args, **kwargs):
    #     sql = "select * from user where user_id=?"
    #     reult = c.execute(sql, (self.id_e.get(),))

    def ajax(self,*args,**kwargs):

        self.get_id=self.id_e.get()

        query="SELECT sales.serial,user.user_name,sales.slab,sales.subs_fee,sales.repay_date,sales.status_fee , sales.status_dl FROM sales INNER JOIN user ON sales.user_id =user.user_id  AND user.user_id=?"

        rsale=c.execute(query, (self.get_id, ))
        for self.r in rsale.fetchall():
            self.get_sl=self.r[0]
            self.get_username=self.r[1]
            self.get_slab=self.r[2]
            self.get_fee = self.r[3]
            self.get_status=self.r[5]
            self.get_repdt=self.r[4]
            self.get_sttsdl=self.r[6]

            self.tbox.insert(END, '' + str(self.get_sl))

            self.tbox.insert(END, ' ' + str(self.get_username))

            self.tbox.insert(END,'     ' + str(self.get_slab))

            self.tbox.insert(END, '     ' + str(self.get_repdt))
            self.tbox.insert(END, '     ' + str(self.get_fee))
            self.tbox.insert(END, '         ' + str(self.get_status))
            self.tbox.insert(END, '     ' + str(self.get_sttsdl)+'\n')

    def search(self, *args, **kwargs):
        sql = "select user_id ,lending_date,slab,amount,repay_date, lending_period,status_fee,status_dl from sales where serial=?"
        result = c.execute(sql, (self.serial_id_e.get(),))
        for r in result:
            self.n1 = r[0]  # id
            self.n2 = r[1]  # lend date
            self.n3 = r[2]  # slab
            self.n4 = r[3]  # amount
            self.n5 = r[4]  # rep dat
            self.n6 = r[5]  # len per
            self.n7 = r[6]   #stts fee
            self.n8 = r[7]  # stts dl

        conn.commit()
        self.user_id_e.delete(0, END)
        self.user_id_e.insert(0, str(self.n1))
        self.lending_date_e.delete(0, END)
        self.lending_date_e.insert(0, str(self.n2))

        self.slab_e.delete(0, END)
        self.slab_e.insert(0, str(self.n3))
        self.amount_e.delete(0, END)
        self.amount_e.insert(0, str(self.n4))
        self.repay_date_e.delete(0, END)
        self.repay_date_e.insert(0, str(self.n5))
        self.lending_period_e.delete(0, END)
        self.lending_period_e.insert(0, str(self.n6))
        self.status_e.delete(0, END)
        self.status_e.insert(0, str(self.n7))
        self.status_dle.delete(0, END)
        self.status_dle.insert(0, str(self.n8))
    def update(self,*args,**kwargs):
        self.u1=self.user_id_e.get()
        self.u2=self.lending_date_e.get()
        self.u3=self.slab_e.get()
        self.u4=self.amount_e.get()
        self.u5=self.repay_date_e.get()
        self.u6=self.lending_period_e.get()
        self.u7=self.status_e.get()
        self.u8=self.status_dle.get()
        weekfee = c.execute("SELECT weekly_fee from dl where slab = ? ", (self.u3,))
        for self.w in weekfee:
            self.getweekfee = self.w[0]
        self.subs_fee = int(self.getweekfee) * int(self.u6)
        query = "UPDATE sales SET user_id=?,lending_date=?,slab=?,amount=?,repay_date=?,lending_period=?,weekly_fee=?,subs_fee=?,status_fee=?,status_dl=? WHERE serial=?"
        c.execute(query, (
        self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.getweekfee,self.subs_fee,self.u7,self.u8, self.serial_id_e.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Update the database")
    def dlt(self,*args,**kwargs):

        sql = " delete from sales where serial=?"
        c.execute(sql, (self.serial_id_e.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted From database")


root=Tk()
b= Salesinfo(root)

root.geometry("1280x1000+0+0")
root.title("Add user ")
root.mainloop()
