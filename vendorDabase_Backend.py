import sqlite3



def vendorData():
    con=sqlite3.connect("C:\\Users\\lenovo\\PycharmProjects\\untitled\\Info.db")
    cur=con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS vinfo(Invoice_no TEXT NOT NULL,DocumentNumber INTEGER PRIMARY KEY  NOT NUll UNIQUE, Type text, Due_dt TEXT,Doc_dt TEXT,Posting_dt TEXT, Amt_loc INTEGER,Vendor_code INTEGER NOT NULL references vendor(vendor_name))")


    con.commit()
    con.close()

def addStdRec(Invoice_no,DocumentNumber,Type,Due_dt,Doc_dt,Posting_dt,Amt_loc,Vendor_code):
    con=sqlite3.connect("C:\\Users\\lenovo\\PycharmProjects\\untitled\\Info.db")
    cur=con.cursor()
    cur.execute("INSERT INTO vinfo (Invoice_no,DocumentNumber,Type,Due_dt,Doc_dt,Posting_dt,Amt_loc,Vendor_code)VALUES(?,?,?,?,?,?,?,?)",[Invoice_no,DocumentNumber,Type,Due_dt,Doc_dt,Posting_dt,Amt_loc,Vendor_code])
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("C:\\Users\\lenovo\\PycharmProjects\\untitled\\Info.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM vinfo")
    rows=cur.fetchall()
    con.close()
    return rows

def deleteRec(no,code):
    con = sqlite3.connect("C:\\Users\\lenovo\\PycharmProjects\\untitled\\Info.db")
    cur = con.cursor()
    cur.execute("DELETE FROM vinfo WHERE DocumentNumber = ? and Vendor_code=?",(no,code))
    con.commit()
    con.close()

def searchData(type="",code=""):
    con=sqlite3.connect("C:\\Users\\lenovo\\PycharmProjects\\untitled\\Info.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM vinfo WHERE Type=? or Vendor_code =?",(type,code))
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(inv="",dcn="",type="",dd="",dod="",postd="",amt="",code=""):
    con = sqlite3.connect("C:\\Users\\lenovo\\PycharmProjects\\untitled\\Info.db")
    cur = con.cursor()
    cur.execute("UPDATE vinfo SET Invoice_no=?,DocumentNumber=?,Type=?,Due_dt?,Doc_dt=?,Posting_dt=?,Amt_loc=?,Vendor_code=? WHERE DocumentNumber=?",
        (inv, dcn, type, dd, dod, postd, amt, code))
    con.commit()
    con.close()


vendorData()
