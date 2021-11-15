import tkinter as tk
from tkinter.constants import END, N, S
import sqlite3

#root window
window = tk.Tk()
window.title("berrybuddy.exe")
window.geometry("500x300")
window.configure(bg='#E2C7D8')
icon = tk.PhotoImage(file="berrybuddylogo.png")
window.iconphoto(True, icon)
window.resizable(False, False)
conn = sqlite3.connect("Berrybase.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS amtable (
Berry_Name text, 
Latitude real, 
longitude real
 )
 """)

conn.commit

conn.close()


#Add marker button window
def AddmarkWindow():
    #save submitted marker info to a .txt
    def savemarker():
         
          
            conn = sqlite3.connect("Berrybase.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO amtable VALUES (:Markername, :latitude, :longitude)",
                        {
                            'Markername': Markername.get(),
                            'latitude': latitude.get(),
                            'longitude': longitude.get()

                            })

            conn.commit()
            conn.close()
            
            Markername_entry.delete(0, END)
            latitude_entry.delete(0, END)
            longitude_entry.delete(0, END)
           
           


    amwind = tk.Toplevel(window)
    amwind.resizable(False, False)
    amwind.title("Add Marker")
    amwind.configure(bg='#E2C7D8')
    amwind.geometry("250x230")
    Markername_text = tk.Label(amwind, text="Marker Name :",bg='#E2C7D8')
    latitude_text = tk.Label(amwind, text="Latitude :",bg='#E2C7D8')
    longitude_text = tk.Label(amwind, text="Longitude :",bg='#E2C7D8')
    Markername_text.grid(column=1,row=0, padx=45, pady=5)
    latitude_text.grid(column=1,row=2, padx=45, pady=5)
    longitude_text.grid(column=1,row=4, padx=45, pady=5)
    Markername = tk.StringVar()
    latitude = tk.DoubleVar()
    longitude = tk.DoubleVar()
    Markername_entry = tk.Entry(amwind, textvariable=Markername,width="25")
    latitude_entry = tk.Entry(amwind, textvariable=latitude,width="25")
    longitude_entry = tk.Entry(amwind, textvariable=longitude,width="25")
    Markername_entry.grid(column=1, row=1, padx=45, pady=5)
    latitude_entry.grid(column=1,row=3, padx=45, pady=5)
    longitude_entry.grid(column=1,row=5, padx=45, pady=5)
    subbutton = tk.Button(amwind,text="Submit",command=savemarker, width="11",height="1",bg="#E2C7D8")
    subbutton.grid(column=1,row=6, padx=45, pady=5)

def DelmarkWindow():
    def delmark():
        conn = sqlite3.connect("Berrybase.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM amtable WHERE oid = " + MarkerID_entry.get())
        conn.commit()
        conn.close()
        MarkerID_entry.delete(0, END)
    def delall():
        conn = sqlite3.connect("Berrybase.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM amtable;",);
        conn.commit()
        conn.close()

    dmwind = tk.Toplevel(window)
    dmwind.resizable(False, False)
    dmwind.title("Delete Marker")
    dmwind.configure(bg='#E2C7D8')
    dmwind.geometry("250x200")
   
    Numid_text = tk.Label(dmwind, text="Marker Number ID: ",bg='#E2C7D8')
    Numid_text.grid(column=1,row=0, padx=45, pady=5)
    MarkerID_entry = tk.Entry(dmwind, width="25")
    MarkerID_entry.grid(column=1, row=1, padx=45, pady=5)
    delbutton = tk.Button(dmwind,text="Delete", command=delmark, width="11",height="1",bg="#E2C7D8")
    delbutton.grid(column=1,row=2, padx=45, pady=5)
    del_allbutton = tk.Button(dmwind,text="Delete All", command=delall, width="11",height="1",bg="#E2C7D8")
    del_allbutton.grid(column=1,row=3, padx=(45), pady=10)
    
   

def ListWindow():
   
    def listmarker():
        conn = sqlite3.connect("Berrybase.db")
        cur = conn.cursor()
        cur.execute("SELECT *, oid FROM amtable")
    
        conn.commit
    
        conn.close
        all_rec = cur.fetchall() 
        global print_records
        print_records= ''
        for record in all_rec:
            print_records += str(record[3]) + "\t" + str(record[0])+ " " + " " + str(record[1]) + " " + " " + str(record[2]) +"\n"
    
    listmarker()   
    print_records
    lmwind = tk.Toplevel(window)
    lmwind.resizable(False, False)
    lmwind.title("List")
    lmwind.configure(bg='#E2C7D8')
    lmwind.geometry("210x230")
    Markerlist_text = tk.Label(lmwind, text="Marker List",bg='#E2C7D8')
    Markerlist_text.grid(column=1,row=0, padx=45, pady=5)
  
    Markerlist = tk.Label(lmwind, text=print_records,bg='white')
    Markerlist.grid(column=1,row=1, padx=45, pady=5)
  
#map buttons
AddMarker = tk.Button(window, width=11, height=1, bg='#E2C7D8', text="Add Marker", command = AddmarkWindow)
AddMarker.grid(column=0, row=0, padx=10, pady=5) 

DelMarker = tk.Button(window, width=11, height=1, bg='#E2C7D8', text="Delete Marker", command = DelmarkWindow)
DelMarker.grid(column=0, row=1, padx=10, pady=5) 

List = tk.Button(window, width=11, height=1, bg='#E2C7D8' ,text="List", command= ListWindow)
List.grid(column=0, row=2, padx=10, pady=5) 


window.mainloop()
