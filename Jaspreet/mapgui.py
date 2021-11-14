import tkinter as tk
from tkinter.constants import N, S

#root window 
window = tk.Tk()
window.title("berrybuddy.exe")
window.geometry("500x300")
window.configure(bg='#E2C7D8')
icon = tk.PhotoImage(file='berrybuddylogo.png')
window.iconphoto(True, icon)

#Add marker button window
def AddmarkWindow():
    #save submitted marker info to a .txt
    def savemarker():
            Markername_info = Markername.get()
            latitude_info = latitude.get()
            longitude_info = longitude.get()
            
            file = open("berryname.txt","a+")  
            file.write(Markername_info + "\n")
            file.close()
            file = open("berrylat.txt","a+")  
            file.write(str(latitude_info) + "\n")
            file.close()
            file = open("berrylong.txt","a+")  
            file.write(str(longitude_info) + "\n")
            file.close()
            amwind.destroy()
            

    amwind = tk.Toplevel(window)
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
     

    dmwind = tk.Toplevel(window)
    dmwind.title("Delete Marker")
    dmwind.configure(bg='#E2C7D8')
    dmwind.geometry("250x230")
   
#map buttons
AddMarker = tk.Button(window, width=11, height=1, bg='#E2C7D8', text="Add Marker", command = AddmarkWindow)
AddMarker.grid(column=0, row=0, padx=10, pady=5) 

DelMarker = tk.Button(window, width=11, height=1, bg='#E2C7D8', text="Delete Marker", command = DelmarkWindow)
DelMarker.grid(column=0, row=1, padx=10, pady=5) 

List = tk.Button(window, width=11, height=1, bg='#E2C7D8' ,text="List")
List.grid(column=0, row=2, padx=10, pady=5) 


window.mainloop()
