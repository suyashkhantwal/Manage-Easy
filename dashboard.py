from tkinter import*
from PIL import Image,ImageTk
from employee import employeeclass
from supplier import supplierclass
from category import categoryclass
from product import productClass
from allotment import allotmentClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory management system | Developed by SUYASH KHANTWAL")
        self.root.config(bg="white")

        #----------TITLE-----------------
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inverntory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor='w',padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #------btn_logout--------
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)
        
        #========clock========
        self.lbl_clock=Label(self.root,text="Welcome to Inverntory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #==========left Menu===========
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="blue")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        lbl_menulogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        #=======LEFT mENU BUTTONS===========
        self.icon_side=PhotoImage(file="images/side.png")

        lbl_menu=Button(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688",cursor="hand2").pack(side=TOP,fill=X)


        btn_employe=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_departement=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_allotments=Button(LeftMenu,text="Allotment",command=self.allotment,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       
       
        #######==========content========
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE, bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE, bg="#ff5772",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=650,y=120,height=150,width=300)

        self.lbl_departement=Label(self.root,text="Total Departments\n[0]",bd=5,relief=RIDGE, bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_departement.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Products\n[0]",bd=5,relief=RIDGE, bg="#607db8",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_allotment=Label(self.root,text="Total Allotments\n[0]",bd=5,relief=RIDGE, bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_allotment.place(x=650,y=300,height=150,width=300)
         #######======footer=======
        self.lbl_clock=Label(self.root,text="IMS-Inventory Management System | Developed by Suyash Khantwal \n For Technical Issue Contact 931xxxxx6 ",font=("times new roman",15,),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

###########=====================================================================
    def employee(self):
        self.__new__win=Toplevel(self.root)
        self.__new__obj=employeeclass(self.__new__win)

    def supplier(self):
        self.__new__win=Toplevel(self.root)
        self.__new__obj=supplierclass(self.__new__win)

    def category(self):
        self.__new__win=Toplevel(self.root)
        self.__new__obj=categoryclass(self.__new__win)

    def product(self):
        self.__new__win=Toplevel(self.root)
        self.__new__obj=productClass(self.__new__win)

    def allotment(self):
        self.__new__win=Toplevel(self.root)
        self.__new__obj=allotmentClass(self.__new__win)

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()