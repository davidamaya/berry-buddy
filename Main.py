
import tkinter as tk                
from tkinter import Button, font  as tkfont
from tkinter.constants import N, VERTICAL, BOTH, RIGHT, LEFT, Y, END
from PIL import ImageTk, Image
from tkinter import filedialog
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from tkinter import ttk
import sqlite3 as sl

class BerryApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, minsize=600, weight=1)
        container.grid_columnconfigure(0, minsize=1000, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, IdentifyPage, MapPage, CatalogPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#space in StartPage (label and logo)
def space(self):
    space_label = tk.Label(self, height=4, bg='#e2c7d8')
    space_label.pack()

#space in StartPage (logo and btn)
def btnspace(self):
    space_label = tk.Label(self, height=2, bg='#e2c7d8')
    space_label.pack()
    
    
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#e2c7d8')
        self.controller = controller
        self.controller.title("BerryBuddy.exe")
        
        space(self)
        
        disclamer_label = tk.Label(self, fg='#F2F2F2', bg="#0D0D0D", text="Disclamer: \n This application is not intended to supply toxicological advice to anyone. \n The creators of this application have referenced sources believed to be reliable in an effort to confirm the accuracy and completeness of the presented herein. \n However, none of the creators warrant that the information is in every respect accurate or complete, and \n they are nor responsible for errors or omissions or for any consequences from application of the information in this book. \n" \
                                             "Never eat any wild plant until you have positively identified the plant as edible. \n There is no substitute for the knowledge of a trained botanist or horticulturist for plant identification. \n In cases of accidental exposure or ingestion of toxic or poisonous berry varieties, contact a Poison Control Center (1-800-222-1222).")
        disclamer_label.pack()
        
        btnspace(self)
        
        logo_photo = tk.PhotoImage(file='berrylogo.gif')
        logo_photo_label = tk.Label(self,image=logo_photo, bg="#e2c7d8")
        logo_photo_label.pack()
        logo_photo_label.image = logo_photo
        
        btnspace(self)
        
        terms_label = tk.Label(self, text='Type "Agree" to get started', bg='#3d3d5c', fg='white')
        terms_label.pack(pady=10)


        my_term = tk.StringVar()
        term_entry_box = tk.Entry(self, textvariable=my_term, width=22)
        term_entry_box.focus_set()
        term_entry_box.pack(ipady=7)

        def check_password():
           if my_term.get() == 'Agree':
               my_term.set('')
               incorrect_term_label['text']=''
               controller.show_frame('PageOne')
           else:
               incorrect_term_label['text']='User has to Agree to move on.'
        
        btnspace(self)

        getStarted_button = Button(self, text="Get Started!", command=check_password, highlightbackground='#e2c7d8', foreground="black", height=3)
        getStarted_button.pack()

        incorrect_term_label = tk.Label(self, text='', fg='white', bg='#95658B', anchor='n')
        incorrect_term_label.pack(fill='both',expand=True)
        
      

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#e2c7d8')
        self.controller = controller

        button_frame = tk.Frame(self, bg="#e2c7d8")
        button_frame.pack(fill='both')
        
        
        def identify():
            controller.show_frame('IdentifyPage')
        identify_button = tk.Button(button_frame, text='Identify', width=8, command=identify, highlightbackground="#e2c7d8", foreground="black")

            
        def map():
            controller.show_frame('MapPage')    
        map_button = tk.Button(button_frame, text='Map', width=8, command=map, highlightbackground="#e2c7d8", foreground="black")
            
        def catalog():
            controller.show_frame('CatalogPage')    
        catalog_button = tk.Button(button_frame, text='Catalog', width=8, command=catalog, highlightbackground="#e2c7d8", foreground="black")
        
        
        logo_photo = tk.PhotoImage(file='berrylogo.gif')
        logo_photo_label = tk.Label(button_frame,image=logo_photo, bg="#e2c7d8")
        logo_photo_label.grid(row=4, column=4, sticky=tk.W, padx=20, rowspan=2)
        logo_photo_label.image = logo_photo

        identify_button.grid(row=4, column=6, sticky=tk.N)
        map_button.grid(row=4, column=6, rowspan=2)
        catalog_button.grid(row=5, column=6, sticky=tk.S)

        button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        

# David's Code Start
class IdentifyPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#e2c7d8")
        self.controller = controller
        
        
        label_frame = tk.Frame(self,bg="#95658B")
        label_frame.pack(fill='both',expand=True)
        
        #Put your code here with label_frame. Take test 1 out 
        def load_img(): 
            global img, image_data
            for img_display in label_frame.winfo_children():
                img_display.destroy()

            # Open file dialog box
            image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                       filetypes=(("all files", "*.*"), ("png files", "*.png")))
            basewidth = 150
            img = Image.open(image_data)
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            file_name = image_data.split('/')

            # Print file name onto page
            panel = tk.Label(label_frame, text= str(file_name[len(file_name)-1]).upper()).pack()

            # Print image onto page
            panel_image = tk.Label(label_frame, image=img).pack()

            classify()

        def classify():

            # Load neural net model
            model = load_model('keras_model.h5')

            # Place classs names into array from labels.txt
            with open('labels.txt', 'r') as f:
                class_names = f.read().split('\n')

            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            # Load berry image into variable
            berry_image = Image.open(image_data)

            # Normaliize the size of the photo into a 224x224 grid
            size = (224, 224)
            berry_image = ImageOps.fit(berry_image, size, Image.ANTIALIAS)

            image_array = np.asarray(berry_image)

            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

            data[0] = normalized_image_array

            # Run normalized image through trained model
            prediction = model.predict(data)

            index = np.argmax(prediction)
            class_name = class_names[index]

            # Print classification report onto page
            result = tk.Label(label_frame, text=class_name).pack()

            
        
        chose_image = tk.Button(self, text='Upload',
                        padx=35, pady=10,
                        fg="#0D0D0D", bg="#E2C7D8", command=load_img)
        chose_image.pack(side=tk.BOTTOM)    


        button_frame = tk.Frame(self, bg="#95658B")
        button_frame.pack(fill='both',expand=True)

        def back():
            controller.show_frame('PageOne')
        
        home_button = tk.Button(button_frame, text='Home', command=back, highlightbackground="#e2c7d8", foreground="black")
        
        button1 = Button(button_frame, text="Homepage", width=8,
                         highlightbackground="pink", foreground="black", command=back)
        home_button.grid(row=2, column=6, sticky=tk.S)
        button_frame.place(relx=1, rely=1, anchor=tk.SE)
        
# David's Code End

# Jaspreet's Code Start
class MapPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#e2c7d8")
        self.controller = controller
        
        label_frame = tk.Frame(self,bg="#95658B")
        label_frame.pack(fill='both',expand=True)

        conn = sl.connect("berries.db")#connect to database
        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS amtable (
        Berry_Name text, 
        Latitude real, 
        longitude real
        )
        """)# creates a table if it doesn't already exist

        conn.commit() #commit 

        conn.close()
        
        #Add marker button window
        def AddmarkWindow():
           
         
            amwind = tk.Toplevel(self, bg='#E2C7D8')#creates window on top of existing window
            Markername_text = tk.Label(amwind, text="Marker Name :",bg='#E2C7D8')
            latitude_text = tk.Label(amwind, text="Latitude :",bg='#E2C7D8')
            longitude_text = tk.Label(amwind, text="Longitude :",bg='#E2C7D8')
            Markername_text.grid(column=1,row=0, padx=45, pady=5)
            latitude_text.grid(column=1,row=2, padx=45, pady=5)
            longitude_text.grid(column=1,row=4, padx=45, pady=5)
            global Markername, latitude, longitude, Markername_entry, latitude_entry, longitude_entry
            Markername = tk.StringVar()#decides datatype of variable
            latitude = tk.StringVar()
            longitude = tk.StringVar()
            Markername_entry = tk.Entry(amwind, textvariable=Markername,width="25")
            latitude_entry = tk.Entry(amwind, textvariable=latitude,width="25")
            longitude_entry = tk.Entry(amwind, textvariable=longitude,width="25")
            Markername_entry.grid(column=1, row=1, padx=45, pady=5)
            latitude_entry.grid(column=1,row=3, padx=45, pady=5)
            longitude_entry.grid(column=1,row=5, padx=45, pady=5)
            subbutton = tk.Button(amwind,text="Submit",command=savemarker, width="11",height="1",bg="#E2C7D8")
            subbutton.grid(column=1,row=6, padx=45, pady=5)
        def savemarker():
                 #save submitted marker info to the table in database
                
                    conn = sl.connect("berries.db")
                    cur = conn.cursor()
                    cur.execute("INSERT INTO amtable VALUES (:Markername, :latitude, :longitude)",
                                {
                                    'Markername': Markername.get(),
                                    'latitude': latitude.get(),
                                    'longitude': longitude.get()

                                    })#inserts variables into the database under respective columns

                    conn.commit()
                    conn.close()
                    
                    Markername_entry.delete(0, END)#clears entry box
                    latitude_entry.delete(0, END)
                    longitude_entry.delete(0, END)

        def DelmarkWindow():
            #delete marker button window

            dmwind = tk.Toplevel(self, bg='#E2C7D8')
        
            Numid_text = tk.Label(dmwind, text="Marker Number ID: ",bg='#E2C7D8')
            Numid_text.grid(column=1,row=0, padx=45, pady=5)
            global MarkerID_entry
            MarkerID_entry = tk.Entry(dmwind, width="25")
            MarkerID_entry.grid(column=1, row=1, padx=45, pady=5)
            delbutton = tk.Button(dmwind,text="Delete", command=delmark, width="11",height="1",bg="#E2C7D8")
            delbutton.grid(column=1,row=2, padx=45, pady=5)
            del_allbutton = tk.Button(dmwind,text="Delete All", command=delall, width="11",height="1",bg="#E2C7D8")
            del_allbutton.grid(column=1,row=3, padx=(45), pady=10)
            
        def delmark():
                conn = sl.connect("berries.db")
                cur = conn.cursor()
                cur.execute("DELETE FROM amtable WHERE oid = " + MarkerID_entry.get())#deletes marker depending on user inputted marker ID
                conn.commit()
                conn.close()
                MarkerID_entry.delete(0, END)
        def delall():
                conn = sl.connect("berries.db")
                cur = conn.cursor()
                cur.execute("DELETE FROM amtable;",);#deletes all entries in table
                conn.commit()
                conn.close()   

        def ListWindow():
       
            
            
            listmarker()   
            print_records
            lmwind = tk.Toplevel(self, bg='#E2C7D8')
        
            my_mainframe=tk.Frame(lmwind)
            my_mainframe.pack(fill=BOTH, expand=1)
            my_canvas = tk.Canvas(my_mainframe,bg='white', highlightbackground= "#95658B", highlightthickness= 4)
            my_canvas.pack(side=LEFT, fill= BOTH, expand=1 )
            my_scrollbar=ttk.Scrollbar(my_mainframe, orient=VERTICAL, command=my_canvas.yview)#this section makes up the scroll bar
            my_scrollbar.pack(side=RIGHT, fill=Y)
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
            
            Listframe=tk.Frame(my_canvas, bg='white')
            Listframe.pack()
            Markerlist_text = tk.Label(Listframe, text="Marker List",bg='white')
            Markerlist_text.pack()
            Markerlist = tk.Label(Listframe, text=print_records, bg="white")
            Markerlist.pack()
            my_canvas.create_window((0,0), window = Listframe, anchor="nw")
        
        def listmarker():
                conn = sl.connect("berries.db")
                cur = conn.cursor()
                cur.execute("SELECT *, oid FROM amtable")
            
                conn.commit()
            
                
                all_rec = cur.fetchall() #fetches all records in table
                global print_records
                print_records= ''
                for record in all_rec:#prints sepcified parts of records
                    print_records += str(record[3]) + "\t" + str(record[0])+ " " + " " + str(record[1]) + " " + " " + str(record[2]) +"\n"
                conn.close()
        #map buttons
        AddMarker = tk.Button(label_frame, width=11, height=1, bg='#E2C7D8', text="Add Marker", command = AddmarkWindow)
        AddMarker.grid(column=0, row=0, padx=10, pady=5) 

        DelMarker = tk.Button(label_frame, width=11, height=1, bg='#E2C7D8', text="Delete Marker", command = DelmarkWindow)
        DelMarker.grid(column=0, row=1, padx=10, pady=5) 

        List = tk.Button(label_frame, width=11, height=1, bg='#E2C7D8' ,text="List", command= ListWindow)
        List.grid(column=0, row=2, padx=10, pady=5) 
        

        button_frame = tk.Frame(self, bg="#95658B")
        button_frame.pack(fill='both',expand=True)
        def back():
            controller.show_frame('PageOne')
        
        home_button = tk.Button(button_frame, text='Home', command=back, highlightbackground="#e2c7d8", foreground="black")
        
        button1 = Button(button_frame, text="Homepage", width=8,
                         highlightbackground="pink", foreground="black", command=back)
        home_button.grid(row=2, column=6, sticky=tk.S)
        button_frame.place(relx=1, rely=1, anchor=tk.SE)

# Jaspreet's Code End

# Sunshine's Code Start
con = sl.connect("berries.db")

with con:
    data = con.execute("SELECT * FROM BERRY")
    for row in data:
        print(row)
        
class CatalogPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#e2c7d8")
        self.controller = controller
  
        label_frame = tk.Frame(self,bg="#95658B")
        label_frame.pack(fill='both',expand=True)
        
        #Put your code here with label_frame. Take test 1 out 
        label = ttk.Label(self, text="Berry Buddy Catalog")
        label2 = ttk.Label(self, text="")
        label3 = ttk.Label(self, text="")
        button2 = tk.Button(self, text="Close", command=lambda: resetLabelText())

        label.pack(pady=10)

        # # Created entry box
        myEntry = tk.Entry(self, font=('Helvetica', 20))
        myEntry.pack()
        #
        # # Create a list box
        myList = tk.Listbox(self, width=50)
        myList.pack()

        # Create a list of berries
        berryNames = ['Gooseberry', 'Coffeeberry', 'Elderberry', 'Wild Grape', 'Cherry', 'Currant', 'Ground Cherry', 'Huckleberry',
                      'Juniper', 'Nightshade', 'Raspberry', 'Serviceberry', 'Strawberry', 'Toyon']

        # # Update the listbox
        def update(data):
            # Clear the listbox so it can reset each time a new berry is entered
            myList.delete("0", "end")
            # Add berries top listbox
            # enumerate allows us to get the index
            # loop goes through the list of berries in the box
            for i, item in enumerate(data):
                # i is the index and item is the berry itself
                myList.insert(i, item)

        # Update entry box with listbox clicked
        def fillout(event):
            # Deletes anything in the entry box
            myEntry.delete(0, "end")

            # Add clicked list item to entry box
            myEntry.insert(0, myList.get("anchor"))
            global BERRY_NAME
            BERRY_NAME = myEntry.get()
            if BERRY_NAME in berryNames:
                with con:
                    data = con.execute(f"SELECT * FROM BERRY WHERE name == '{myEntry.get()}'")
                    result = data.fetchone()
                    if result:
                        label2.pack(pady=20)
                        label2.config(text=result[1])
                        label3.config(text=result[2])
                        label3.pack(pady=20)
                        # breaking... come back to fix because it is not destroying the labels, instead it is overlapping
                        button2.pack()

        # # Create function to check entry vs listbox
        def check(event):
            # Grab what was typed
            typed = myEntry.get()
            if typed == '':
                # The berryNames list will show up if there is nothing in the search bar
                data = berryNames
            else:
                data = []
                for item in berryNames:
                    if typed.lower() in item.lower():
                        data.append(item)

            # Updates our listbox with selected items
            update(data)

        #
        # # Add berryNames to list
        update(berryNames)
        #
        # # Create a binding on the listbox onclick... predicts entry based on what is in the listbox
        myList.bind('<<ListboxSelect>>', fillout)
        #
        # # Create a binding on the entry box
        myEntry.bind('<KeyRelease>', check)

        def resetLabelText():
            label2.config(text='')
            label3.config(text='')
            myEntry.delete("0", "end")

        button_frame = tk.Frame(self, bg="#95658B")
        button_frame.pack(fill='both',expand=True)
        def back():
            resetLabelText()
            controller.show_frame('PageOne')
        
        home_button = tk.Button(button_frame, text='Home', command=back, highlightbackground="#e2c7d8", foreground="black")
        
        button1 = Button(button_frame, text="Homepage", width=8,
                         highlightbackground="pink", foreground="black", command=back)
        home_button.grid(row=2, column=6, sticky=tk.S)
        button_frame.place(relx=1, rely=1, anchor=tk.SE)

# Sunshine's Code End

if __name__ == "__main__":
    app = BerryApp()
    app.mainloop()
