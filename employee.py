import sqlite3
from sqlite3.dbapi2 import Error
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
class employeeclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory management system | Developed by SUYASH KHANTWAL")
        self.root.config(bg="white")
        self.root.focus_force()

        #============
        #ALL VARIABLES===
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()





        self.var_emp_id=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()  #DATE OF JOINING
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_post=StringVar()



        #===========searchFrame============
        searchFrame=LabelFrame(self.root,text="search Employee",bg="white")
        searchFrame.place(x=250,y=20,width=600,height=70)

        #==========OPTIONS==========
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15,))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(searchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        ###=====title==
        title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
        

        #==========content====

        ###row1==========
        lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="WHITE").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="WHITE").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="WHITE").place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        #txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="WHITE").place(x=500,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("select","Male","Female","Others"),state='readonly',justify=CENTER,font=("goudy old style",15,))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
        
        #=====row2=====
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)

        #=====row3=====
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_password=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
        #txt_utype=Entry(self.root,textvariable=self.var_utype,font=("goudy old style",15),bg="lightyellow").place(x=850,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("select","Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15,))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)

        #=====row4============================================
        lbl_adress=Label(self.root,text="Adress",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_post=Label(self.root,text="Post",font=("goudy old style",15),bg="white").place(x=500,y=270)
    

        self.txt_adres=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_adres.place(x=150,y=270,width=300,height=60)
        txt_post=Entry(self.root,textvariable=self.var_post,font=("goudy old style",15),bg="lightyellow").place(x=600,y=270,width=180)


        #####======buttons=======

        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)



        #######Employee Details==========

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)


        self.employeetable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","adress","post"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.employeetable.xview)
        scrolly.config(command=self.employeetable.yview)

        self.employeetable.heading("eid",text="EMP ID")
        self.employeetable.heading("name",text="NAME")
        self.employeetable.heading("email",text="EMAIL")
        self.employeetable.heading("gender",text="GENDER")
        self.employeetable.heading("contact",text="CONTACT")
        self.employeetable.heading("dob",text="D.O.B")
        self.employeetable.heading("doj",text="D.O.J")
        self.employeetable.heading("pass",text="PASSWORD")
        self.employeetable.heading("utype",text="USER TYPE")
        self.employeetable.heading("adress",text="ADRESS")
        self.employeetable.heading("post",text="POST")
        
        self.employeetable["show"]="headings"
        
        //additional file//
        def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory management system | Developed by SUYASH KHANTWAL")
        self.root.config(bg="white")



        
        

       
        self.employeetable.column("eid",width=90)
        self.employeetable.column("name",width=100)
        self.employeetable.column("email",width=100)
        self.employeetable.column("gender",width=100)
        self.employeetable.column("contact",width=100)
        self.employeetable.column("dob",width=100)
        self.employeetable.column("doj",width=100)
        self.employeetable.column("pass",width=100)
        self.employeetable.column("utype",width=100)
        self.employeetable.column("adress",width=100)
        self.employeetable.column("post",width=100)
        self.employeetable.pack(fill=BOTH,expand=1)
        self.employeetable.bind("<ButtonRelease-1> ",self.get_data)

        self.show()


        
        
####################======================================================================================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="" :
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID already assinged,try different",parent=self.root)
                else:
                    cur.execute("Insert into Employee(eid,name,email,gender,contact,dob,doj,pass,utype,adress,post)values(?,?,?,?,?,?,?,?,?,?,?)",(
                                                self.var_emp_id.get(),
                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),
                                                self.var_dob.get(),
                                                self.var_doj.get(),  
                                                
                                                self.var_pass.get(),
                                                self.var_utype.get(),
                                                self.txt_adres.get('1.0',END),
                                                self.var_post.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


        
        


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.employeetable.delete(*self.employeetable.get_children())
            for row in rows:
                self.employeetable.insert('',END,values=row)

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def get_data(self,ev):

        f=self.employeetable.focus()
        content=(self.employeetable.item(f))
        row=content['values']
        #print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6]) 
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_adres.delete('1.0',END),
        self.txt_adres.insert(END,row[9]),
        self.var_post.set(row[10])


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="" :
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID ",parent=self.root)
                else:
                    cur.execute("Update Employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,adress=?,post=? where eid=?",(
                                                
                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),
                                                self.var_dob.get(),
                                                self.var_doj.get(),  
                                                
                                                self.var_pass.get(),
                                                self.var_utype.get(),
                                                self.txt_adres.get('1.0',END),
                                                self.var_post.get(),
                                                self.var_emp_id.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="" :
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID ",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from Employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                    messagebox.showinfo("Delete","Employee Deleted Succesfully",parent=self.root)
                    self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  

    def clear(self):
        
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("") 
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_adres.delete('1.0',END)
        self.var_post.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search By Option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("Select * from employee where " +self.var_searchby.get()+" LIKE '%"+ self.var_searchtxt.get() +"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.employeetable.delete(*self.employeetable.get_children())
                    for row in rows:
                        self.employeetable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=employeeclass(root)
    root.mainloop()
