from tkinter import *
from tkinter import ttk

import tkinter.messagebox
import vendorDabase_Backend


class College:
    def  __init__(self,root):
        self.root=root
        self.root.title("Vendor API")
        self.root.geometry('2050x750+0+0')
        self.root.config(background="Maroon")
#=======================================FRAME BACKGROUND================================================
        MainFrame=Frame(self.root)
        MainFrame.grid()

        TopFrame=Frame(MainFrame,bd=14,width=1350,height=550,padx=20,relief=RIDGE,bg="brown")
        TopFrame.pack(side=TOP)

        LeftFrame = Frame(TopFrame, bd=10, width=450, height=550, padx=20, relief=RIDGE, bg="MistyRose")
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(TopFrame, bd=10, width=820, height=550, padx=2, relief=RIDGE, bg="Pink")
        RightFrame.pack(side=RIGHT)

        BottomFrame = Frame(MainFrame, bd=14, width=1480, height=150, padx=20, relief=RIDGE, bg="brown")
        BottomFrame.pack(side=BOTTOM)
        # =======================================FUNCTIONS==========================================================
        #----------------------------------------Exit dilog box on exit button click------------------------
        def iExit():
            iExit=tkinter.messagebox.askyesno("College management System","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
            return
        #--------------------------------------clearing data on clear button click-----------------------------
        def clearData():
            self.txtInv.delete(0,END)
            self.txtDocn.delete(0, END)
            self.txtType.delete(0, END)
            self.txtDd.delete(0, END)
            self.txtdocd.delete(0, END)
            self.txtpd.delete(0, END)
            self.txtMobile.delete(0, END)

        #------------------------------------adding data on add button click----------------------------------------
        def addData():
            if(len(Doc_no.get())!=0):
                vendorDabase_Backend.addStdRec(Invoice_no.get(), Doc_no.get(), Type.get(), Due_dt.get(), Doc_dt.get(), Posting_dt.get(), Amt_loc.get(), Vendor_code.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(Invoice_no.get(),Doc_no.get(),Type.get(),Due_dt.get(),Doc_dt.get(),Posting_dt.get(),Amt_loc.get(),Vendor_code.get()))

        # ------------------------------------displaying data on add display click----------------------------------------
        def DisplayData():
            studentlist.delete(0,END)
            for  i in vendorDabase_Backend.viewData():
                studentlist.insert(END,i,str(""))

        # ------------------------------------sd as global variable----------------------------------------
        def StudentRec(event):
            global sd
            searchStd=studentlist.curselection()[0]
            sd=studentlist.get(searchStd)

            self.txtInv.delete(0, END)
            self.txtInv.insert(END,sd[1])
            self.txtDocn.delete(0, END)
            self.txtDocn.insert(END, sd[2])
            self.txtType.delete(0, END)
            self.txtType.insert(END, sd[3])
            self.txtDd.delete(0, END)
            self.txtDd.insert(END, sd[4])
            self.txtdocd.delete(0, END)
            self.txtdocd.insert(END, sd[5])
            self.txtpd.delete(0, END)
            self.txtpd.insert(END, sd[6])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, sd[7])


        # ------------------------------------deleting data on delete  button click----------------------------------------
        def DeleteData():
            if (len(Doc_no.get()) != 0):
                vendorDabase_Backend.deleteRec(sd[0], sd[0])
            clearData()
            DisplayData()

        # ------------------------------------searching data on search button click----------------------------------------
        def searchDatabase():

            studentlist.delete(0,END)
            for row in vendorDabase_Backend.searchData(Type.get(), Vendor_code.get()):
                studentlist.insert(END,row,str(""))

        # ------------------------------------updating data on update button click----------------------------------------
        def update():
            if(len(Doc_no.get())!=0):
                vendorDabase_Backend.deleteRec(0, 0)
            if(len(Doc_no.get())!=0):
                vendorDabase_Backend.addStdRec(Invoice_no.get(), Doc_no.get(), Type.get(), Due_dt.get(), Doc_dt.get(), Posting_dt.get(), Amt_loc.get(), Vendor_code.get())
                studentlist.delete(0,END)

                studentlist.insert(END,(Invoice_no.get(),Doc_no.get(),Type.get(),Due_dt.get(),Doc_dt.get(),Posting_dt.get(),Amt_loc.get(),Vendor_code.get()))




        #===========================INNER LEFT FRAME============================================================
        Invoice_no = IntVar()
        Doc_no = StringVar()
        Type = StringVar()
        Due_dt = IntVar()
        Doc_dt = IntVar()
        Posting_dt = IntVar()
        Amt_loc = IntVar()
        Vendor_code = StringVar()

        #------------Invoice--------------------
        self.lblInv=Label(LeftFrame,font=('Chauser',20,'bold'),text="Invoice Number",padx=2,bg="LightGoldenrodYellow")
        self.lblInv.grid(row=0,column=0,sticky=W)
        self.txtInv=Entry(LeftFrame,font=('Chauser',20,'bold'),textvariable=Invoice_no,width=20)
        self.txtInv.grid(row=0,column=1,pady=3,padx=20)
        #--------------Document Number--------------
        self.lblDocn=Label(LeftFrame, font=('Chauser', 20, 'bold'), text="Document Number", padx=2,pady=2,bg="LightGoldenrodYellow")
        self.lblDocn.grid(row=1, column=0, sticky=W)
        self.txtDocn=Entry(LeftFrame, font=('Chauser', 20, 'bold'), textvariable=Doc_no, width=20)
        self.txtDocn.grid(row=1, column=1, pady=3, padx=20)
        #------------Type---------------------
        self.lblType = Label(LeftFrame, font=('Chauser', 20, 'bold'), text="Type", padx=2,
                                     bg="LightGoldenrodYellow")
        self.lblType.grid(row=2, column=0, sticky=W)
        self.txtType = Entry(LeftFrame, font=('Chauser', 20, 'bold'), textvariable=Type, width=20)
        self.txtType.grid(row=2, column=1, pady=3, padx=20)
        #----------Due Date----------------
        self.lblDd = Label(LeftFrame, font=('Chauser', 20, 'bold'), text="Due Date", padx=2,
                                     bg="LightGoldenrodYellow")
        self.lblDd.grid(row=3, column=0, sticky=W)
        self.txtDd = Entry(LeftFrame, font=('Chauser', 20, 'bold'), textvariable=Due_dt, width=20)
        self.txtDd.grid(row=3, column=1, pady=3, padx=20)
        #--------------Doc date------------
        self.lbldocd = Label(LeftFrame, font=('Chauser', 20, 'bold'), text="Document Date", padx=2,
                                     bg="LightGoldenrodYellow")
        self.lbldocd.grid(row=4, column=0, sticky=W)
        self.txtdocd = Entry(LeftFrame, font=('Chauser', 20, 'bold'), textvariable=Doc_dt, width=20)
        self.txtdocd.grid(row=4, column=1, pady=3, padx=20)
        #------------Posting Date------------
        self.lblpd = Label(LeftFrame, font=('Chauser', 20, 'bold'), text="Posting Date", padx=2,
                                     bg="LightGoldenrodYellow")
        self.lblpd.grid(row=5, column=0, sticky=W)
        self.txtpd = Entry(LeftFrame, font=('Chauser', 20, 'bold'), textvariable=Posting_dt, width=20)
        self.txtpd.grid(row=5, column=1, sticky=W)
        #-----------Amount--------------
        self.lblAddress = Label(LeftFrame, font=('Chauser', 20, 'bold'), text="Amount", padx=2,
                                     bg="LightGoldenrodYellow")
        self.lblAddress.grid(row=6, column=0, sticky=W)
        self.txtAddress = Entry(LeftFrame, font=('Chauser', 20, 'bold'), textvariable=Amt_loc, width=20)
        self.txtAddress.grid(row=6, column=1, pady=3, padx=20)
        #------------Vendor Code-------------
        self.lblMobile = Label(LeftFrame, font=('Chauser', 20, 'bold'), text="Vendor Code", padx=2,
                                     bg="LightGoldenrodYellow")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(LeftFrame, font=('Chauser', 20, 'bold'), textvariable=Vendor_code, width=20)
        self.txtMobile.grid(row=7, column=1, pady=3, padx=20)

        # ===========================SCROLL BAR AND LIST BOX============================================================

        scrollbar=Scrollbar(RightFrame)
        scrollbar.grid(row=0,column=1,sticky='ns')

        studentlist= Listbox(RightFrame,width=41,height=16,font=('Chauser', 20, 'bold'),yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=studentlist.yview)
        scrollbar.config(command=studentlist.xview)
        # ===========================BUTTONS AT BOTTOM=================================================================
        self.btnAddData=Button(BottomFrame,text="Add new",font=('Chauser', 10, 'bold'),height=1,width=10,bd=4,command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(BottomFrame, text="Display", font=('Chauser', 10, 'bold'), height=1, width=10, bd=4,command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(BottomFrame, text="Clear", font=('Chauser', 10, 'bold'), height=1, width=10, bd=4,command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(BottomFrame, text="Delete", font=('Chauser', 10, 'bold'), height=1, width=10, bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(BottomFrame, text="Search", font=('Chauser', 10, 'bold'), height=1, width=10, bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(BottomFrame, text="Update", font=('Chauser', 10, 'bold'), height=1, width=10, bd=4,command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(BottomFrame, text="Exit", font=('Chauser', 10, 'bold'), height=1, width=10, bd=4,command=iExit)
        self.btnExit.grid(row=0, column=6)

#============================================MAIN FUNCTION CALLING=====================================================
if __name__=='__main__':
    root=Tk()
    application=College(root)
    root.mainloop()