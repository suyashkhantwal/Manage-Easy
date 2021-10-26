import sqlite3
from sqlite3.dbapi2 import Error
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import os
class allotmentClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory management system | Developed by SUYASH KHANTWAL")
        self.root.config(bg="white")
        self.root.focus_force()

        self.bill_list=[]
        self.var_invoice=StringVar()

        
        ###########title######
        lbl_title=Label(self.root,text="View Allotments",font=("goudy old style ",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_invoice=Label(self.root,text="Invoice no.",font=("times new roman",15),bg="white").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="white").place(x=160,y=100,width=180,height=28)
        

        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=500,y=100,width=120,height=28)
        
##############ALLOTMENT LIST ################
        allotment_frame=Frame(self.root,bd=3,relief=RIDGE)
        allotment_frame.place(x=50,y=140,width=190,height=330)

        

        scrolly=Scrollbar(allotment_frame,orient=VERTICAL)
        self.allotment_List=Listbox(allotment_frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.allotment_List.yview)
        self.allotment_List.pack(fill=BOTH,expand=1)
        self.allotment_List.bind("<ButtonRelease-1>",self.get_data)
######################BILLING / RECORD AREA##############
        bill_frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=280,y=140,width=410,height=330)
        
        lbl_title=Label(bill_frame,text="Allotments Bill Area",font=("goudy old style ",20),bg="orange").pack(side=TOP,fill=X)
        

        
        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,font=("goudy old style",15),bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.allotment_List.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

       #####################Image############
        self.bill_photo=Image.open("images/cat2.jpg")
        self.bill_photo=self.bill_photo.resize((450,300),Image.ANTIALIAS)
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo) 


        lbl_image=Label(self.root,image=self.bill_photo,bd=0)
        lbl_image.place(x=700,y=110)

        self.show()
 ######################################      
    def show(self):
        del self.bill_list[:]
        self.allotment_List.delete(0,END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.allotment_List.insert(END,i)
                self.bill_list.append(i.split('.')[0])


    def get_data(self,ev):
        index_=self.allotment_List.curselection()
        file_name=self.allotment_List.get(index_)
        #print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error" , "Invoice no. shoud be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error" , " Invalid Invoice no.",parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)






if __name__=="__main__":
    root=Tk()
    obj=allotmentClass(root)
    root.mainloop()