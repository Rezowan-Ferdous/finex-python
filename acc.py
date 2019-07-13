from tkinter import *
import datetime
from datetime import datetime, date, timedelta
import sqlite3
import tkinter.messagebox

date1 = datetime.today().date()
conn = sqlite3.connect("Finexdb.db")

c = conn.cursor()


result=c.execute("select max(account_id),sum(sa_collection),total(net_flow) from accounts")
for r in result:
    accountid=r[0]
    sacol=r[1]
    nfl = r[2]

resultnf=c.execute("SELECT date, net_flow FROM accounts ORDER BY account_id DESC LIMIT 1")
for n in resultnf:
    dt = n[0]
    nf=n[1]


class Accounts:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.datetime = datetime.date
        self.s = Label(master, text="Account ID has reached upto  " + str(accountid), font=('arial 10 bold'),
                       fg='steelblue')
        self.s.place(x=0, y=30)
        self.sa_l = Label(master, text="S/A Collection has reached upto  " + str(sacol), font=('arial 10 bold'),
                       fg='steelblue')
        self.sa_l.place(x=0, y=550)
        self.nf_l = Label(master, text="last date  "+str(dt)+"  Net Flow " + str(nfl), font=('arial 10 bold'),
                          fg='steelblue')
        self.nf_l.place(x=0, y=580)
        self.date_l = Label(master, text="today's Date: " + str(date1), font=('arial 10 bold '),
                            bg='lightblue', fg='white')
        self.date_l.place(x=0, y=0)
        self.ac_id_l = Label(master, text="Account ID", font=('arial 12 bold'))
        self.ac_id_l.place(x=0, y=500)
        self.date_le = Label(master, text="Enter Date", font=('arial 15 bold'))
        self.date_le.place(x=550, y=100)
        self.heading = Label(master, text="FINEX ACCOUNTS", font=('arial 40 bold'), fg='green')
        self.heading.place(x=450, y=0)

        self.cashinl = Label(master, text="Cash Inflow", font=('arial 25 bold'), fg='green')
        self.cashinl.place(x=20, y=60)

        self.sac_l = Label(master, text="S/A Collection ", font=('arial 15 bold'))
        self.sac_l.place(x=0, y=150)
        self.bo_l = Label(master, text="Book Opening", font=('arial 15 bold'))
        self.bo_l.place(x=0, y=200)
        self.loanrepay_l = Label(master, text="Loan Repay", font=('arial 15 bold'))
        self.loanrepay_l.place(x=0, y=250)
        self.owncap_l = Label(master, text="Owner Cap", font=('arial 15 bold'))
        self.owncap_l.place(x=0, y=300)
        self.return_l = Label(master, text="Return ", font=('arial 15 bold'))
        self.return_l.place(x=0, y=350)
        self.fine_l = Label(master, text="Fine ", font=('arial 15 bold'))
        self.fine_l.place(x=0, y=400)

        self.sac_e = Entry(master, width=8, font=('arial 15 bold'))
        self.sac_e.place(x=150, y=150)
        self.bo_e = Entry(master, width=8, font=('arial 15 bold'))
        self.bo_e.place(x=150, y=200)
        self.loanrepay_e = Entry(master, width=8, font=('arial 15 bold'))
        self.loanrepay_e.place(x=150, y=250)
        self.owncap_e = Entry(master, width=8, font=('arial 15 bold'))
        self.owncap_e.place(x=150, y=300)
        self.return_e = Entry(master, width=8, font=('arial 15 bold'))
        self.return_e.place(x=150, y=350)
        self.fine_e = Entry(master, width=8, font=('arial 15 bold'))
        self.fine_e.place(x=150, y=400)
        self.date_e = Entry(master, width=10, font=('arial 15 bold'))
        self.date_e.place(x=670, y=100)
        self.ac_id_e = Entry(master, width=10, font=('arial 15 bold'))
        self.ac_id_e.place(x=110, y=500)

        #######################################################
        self.cashout_l = Label(master, text="Cash Out flow", font=('arial 25 bold'), fg='green')
        self.cashout_l.place(x=300, y=60)
        self.loan_l = Label(master, text="LOAN ", font=('arial 15 bold'))
        self.loan_l.place(x=300, y=150)
        self.opex_l = Label(master, text="OP Expense", font=('arial 15 bold'))
        self.opex_l.place(x=300, y=200)
        self.withdrw_l = Label(master, text="Withdraw ", font=('arial 15 bold'))
        self.withdrw_l.place(x=300, y=250)
        self.politics_l = Label(master, text="POLitics", font=('arial 15 bold'))
        self.politics_l.place(x=300, y=300)
        self.bookcls_l = Label(master, text="BOOK Closing ", font=('arial 15 bold'))
        self.bookcls_l.place(x=300, y=350)
        self.salary_l = Label(master, text="Salary ", font=('arial 15 bold'))
        self.salary_l.place(x=300, y=400)

        self.loan_e = Entry(master, width=8, font=('arial 15 bold'))
        self.loan_e.place(x=450, y=150)
        self.opex_e = Entry(master, width=8, font=('arial 15 bold'))
        self.opex_e.place(x=450, y=200)
        self.withdraw_e = Entry(master, width=8, font=('arial 15 bold'))
        self.withdraw_e.place(x=450, y=250)
        self.politics_e = Entry(master, width=8, font=('arial 15 bold'))
        self.politics_e.place(x=450, y=300)
        self.bookcls_e = Entry(master, width=8, font=('arial 15 bold'))
        self.bookcls_e.place(x=450, y=350)
        self.salary_e = Entry(master, width=8, font=('arial 15 bold'))
        self.salary_e.place(x=450, y=400)

        self.btn_adds = Button(master, text="NET Flow", width=20, height=2, bg='steelblue', fg='white',
                               command=self.get_flow
                               )
        self.btn_adds.place(x=400, y=500)

        self.btn_clr = Button(master, text="CLEAR ALL FIELD", width=20, height=2, bg='green', fg='white',command=self.clear_all
                              )
        self.btn_clr.place(x=400, y=550)

        self.btn_srch = Button(master, text="SEARCH", width=10, height=2, bg='yellow', fg='black',
                               command=self.search)
        self.btn_srch.place(x=780, y=100)
        self.btn_upd = Button(master, text="UPDATE", width=10, height=2, bg='green', fg='white', command=self.update)
        self.btn_upd.place(x=865, y=100)
        self.btn_dlt = Button(master, text="Delete Accounts", width=12, height=2, bg='yellow', fg='black',
                              command=self.dlt)
        self.btn_dlt.place(x=950, y=100)

        self.tbox = Text(master, width=20, height=15)
        self.tbox.place(x=600, y=150)

    def get_flow(self, *args, **kwargs):
        # getfromentries
        self.acdat = self.date_e.get()
        self.acdate = datetime.strptime(self.acdat, "%d/%m/%Y").date()
        self.ac_id = self.ac_id_e.get()
        self.sac = self.sac_e.get()
        self.bo = self.bo_e.get()
        self.loanrepay = self.loanrepay_e.get()
        self.owncap = self.owncap_e.get()
        self.returns = self.return_e.get()
        self.fine = self.fine_e.get()
        self.inflow = int(self.sac) + int(self.bo) + int(self.loanrepay) + int(self.owncap) + int(self.returns) + int(
            self.fine)

        self.loan = self.loan_e.get()
        self.opex = self.opex_e.get()
        self.withdraw = self.withdraw_e.get()
        self.politics = self.politics_e.get()
        self.bookcls = self.bookcls_e.get()
        self.salary = self.salary_e.get()
        self.outflow = int( int(self.loan) + int(self.opex) + int(self.withdraw) + int(self.politics) + int(self.bookcls)+int(self.salary))

        self.netflow = int(int(self.inflow) - int(self.outflow))

        if self.acdate == '' or self.ac_id == '':  # or self.user_name=='' or self.grp=='' or self.joining_date==''or self.address =='' or self.nid==''or self.phone=='':
            tkinter.messagebox.showinfo("Error", "please fill required field.")
        else:
            # sql = 'insert into user(serial,user_id,user_name,group,joining_date,address,nid,phone,email) values(?,?,?,?,?,?,?,?,?)'
            c.execute("INSERT INTO accounts VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                      (self.acdate, self.ac_id, self.sac,
                       self.bo, self.loanrepay, self.owncap, self.returns, self.fine, self.inflow, self.loan,
                       self.opex, self.withdraw, self.politics, self.bookcls, self.salary, self.outflow, self.netflow))
            conn.commit()
            tkinter.messagebox.showinfo("success", " successfully added")
        self.tbox.insert(END, 'The net Cash IN Flow is ' + str(self.inflow))
        self.tbox.insert(END, '\nThe net Cash out Flow is ' + str(self.outflow))
        self.tbox.insert(END, '\nThe net Cash  Flow is ' + str(self.netflow))
        re

    def search(self, *args, **kwargs):
        self.acdat = self.date_e.get()
        self.acdate = datetime.strptime(self.acdat, "%d/%m/%Y").date()
        sql = "select account_id,sa_collection,b_opening, loan_repay,own_cap,return,fine,loan,salary,op_expense,withdraw,politics,b_closing from accounts where date=?"
        result = c.execute(sql, (self.acdate,))
        for r in result:
            self.n1 = r[0]  # ac id
            self.n2 = r[1]  # sa_col
            self.n3 = r[2]  # bo
            self.n4 = r[3]  # loan rep
            self.n5 = r[4]  # own cap
            self.n6 = r[5]  # return
            self.n7 = r[6]   #fine
            self.n8 = r[7]  # loan
            self.n9 = r[8]  # salary
            self.n10 = r[9]  # opex
            self.n11 = r[10]  # withdrw
            self.n12 = r[11]  # politi
            self.n13 = r[12]  # bc

        conn.commit()
        self.ac_id_e.delete(0, END)
        self.ac_id_e.insert(0, str(self.n1))
        self.sac_e.delete(0, END)
        self.sac_e.insert(0, str(self.n2))

        self.bo_e.delete(0, END)
        self.bo_e.insert(0, str(self.n3))
        self.loanrepay_e.delete(0, END)
        self.loanrepay_e.insert(0, str(self.n4))
        self.owncap_e.delete(0, END)
        self.owncap_e.insert(0, str(self.n5))
        self.return_e.delete(0, END)
        self.return_e.insert(0, str(self.n6))
        self.fine_e.delete(0, END)
        self.fine_e.insert(0, str(self.n7))
        self.loan_e.delete(0, END)
        self.loan_e.insert(0, str(self.n8))
        self.salary_e.delete(0,END)
        self.salary_e.insert(0,str(self.n9))
        self.opex_e.delete(0, END)
        self.opex_e.insert(0, str(self.n10))
        self.withdraw_e.delete(0, END)
        self.withdraw_e.insert(0, str(self.n11))
        self.politics_e.delete(0,END)
        self.politics_e.insert(0,str(self.n12))
        self.bookcls_e.delete(0,END)
        self.bookcls_e.insert(0,str(self.n13))
    def update(self,*args,**kwargs):
        self.acdat = self.date_e.get()
        self.acdate = datetime.strptime(self.acdat, "%d/%m/%Y").date()
        self.u1=self.ac_id_e.get()
        self.u2=self.sac_e.get()
        self.u3=self.bo_e.get()
        self.u4=self.loanrepay_e.get()
        self.u5=self.owncap_e.get()
        self.u6=self.return_e.get()
        self.u7=self.fine_e.get()
        self.u8=self.loan_e.get()
        self.u9=self.salary_e.get()
        self.u10 = self.opex_e.get()
        self.u11 = self.withdraw_e.get()
        self.u12 = self.politics_e.get()
        self.u13 = self.bookcls_e.get()
        self.inflow = int(self.u2) + int(self.u3) + int(self.u4) + int(self.u5) + int(self.u6) + int(
            self.u7)
        self.outflow = int(
            int(self.u8) + int(self.u9) + int(self.u10) + int(self.u11) + int(self.u12)+int(self.u13))

        self.netflow = int(int(self.inflow) - int(self.outflow))
        query = "UPDATE accounts SET account_id=?,sa_collection=?,b_opening=?,loan_repay=?,own_cap=?,return=?,fine=?,total_inflow=?,loan=?,salary=?,op_expense=?,\
        withdraw=?,politics=?,b_closing=?,total_outflow=?,net_flow=? WHERE date=?"
        c.execute(query, (
        self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7,self.inflow,self.u8,self.u9,self.u10,self.u11,self.u12,self.u13,\
        self.outflow,self.netflow,self.acdate))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Update the database")
    def dlt(self,*args,**kwargs):
        self.acdat = self.date_e.get()
        self.acdate = datetime.strptime(self.acdat, "%d/%m/%Y").date()
        sql = " delete from accounts where date=?"
        c.execute(sql, (self.acdate,))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted From database")
    def clear_all(self, *args, **kwargs):
        self.ac_id_e.delete(0, END)
        self.return_e.delete(0, END)
        self.sac_e.delete(0, END)
        self.bo_e.delete(0, END)
        self.loanrepay_e.delete(0, END)
        self.owncap_e.delete(0, END)
        self.fine_e.delete(0, END)
        self.loan_e.delete(0, END)
        self.opex_e.delete(0, END)
        self.withdraw_e.delete(0, END)
        self.politics_e.delete(0,END)
        self.bookcls_e.delete(0,END)
        self.salary_e.delete(0,END)
        self.date_e.delete(0,END)
root = Tk()
b = Accounts(root)

root.geometry("1280x1000+0+0")
root.title("Accounts ")
root.mainloop()
