from tkinter import *

class Berry:
    def __init__(self, name, description):
        self.name = name
        self.description = description


list = []

list.append(Berry('Coffeeberry', """
    Currants and gooseberries are both members of the Ribes genus, and do look very
    similar, though there are some important distinctions. They are both perennial
    bushes with somewhat vining stalks that arise from the roots. When cut back or
    burned back, the plant will send up many very straight stalks.
    The stalks of the gooseberries are covered in spines. The fruits of goose-berry are
    also covered in little spines. Currants, on the other hand, have no spines on the stalk
    or fruit. But both plants have the very same growth patterns, and leaves that look
    like a three-lobed mitten. I prefer the currants because they are easier to collect and have no spines. But
    both are useful, and both have their adherents.
    The fruits are small, but you can get a fair amount if you find a good patch and
    carefully pick away. You never seem to be able to gather as much as you want. For
    one thing, the fruits dont usually all ripen at the same time. """))

# ***** main window *****
main = Tk()
main.title("BerryBuddy Catalog")
main.configure(background="pink")
main.geometry("1000x600")

BERRY_DATA = ['Coffeeberry', 'Gooseberry', 'Elderberry', 'Wild Grape', 'Ground Cherry',
              'Huckleberry']


# ***** mainPage -- frame1
def mainPage():
    # ***** go function starts -- navigates to berry info page
    def go(berry):
        foundBerry = None
        for item in list:
            if item.name == berry:
                foundBerry = Berry(item.name, item.description)
        global go
        for widgets in frame.winfo_children():
            widgets.destroy()

        # ***** Go -- frame2
        frame2 = Frame(main)
        frame2.configure(background="pink")

        # ***** back to mainPage
        def back():
            for widgets in frame2.winfo_children():
                widgets.destroy()
                frame3.destroy()
                mainPage()

        # ***** berry info page
        if bool(foundBerry):
            test1 = Label(
                frame2, text="This is the " + berry + " page.")
            test2 = Label(
                frame2, text=foundBerry.description)
            test1.grid(row=1, column=2, sticky=N)
            test2.grid(row=2, column=2, sticky=S)
            frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

            #
            frame3 = Frame(main)
            frame3.configure(background="pink")
            button1 = Button(frame3, text="Catalog", width=8,
                             highlightbackground="pink", foreground="black", command=back)
            button1.grid(row=2, column=6, sticky=S)
            frame3.place(relx=1, rely=1, anchor=SE)
        else:
            test1 = Label(frame2, text="Berry not found...")
            test1.grid(row=1, column=2, stick=N)
            frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

            #
            frame3 = Frame(main)
            frame3.configure(background="pink")
            button1 = Button(frame3, text="Catalog", width=8,
                             highlightbackground="pink", foreground="black", command=back)
            button1.grid(row=2, column=6, sticky=S)
            frame3.place(relx=1, rely=1, anchor=SE)

        # ***** end of Go function

        # ---Back button to homepage---
        def back():
            for widgets in frame2.winfo_children():
                widgets.destroy()
                frame4.destroy()
                mainPage()

        frame4 = Frame(main)
        frame4.configure(background="pink")
        button1 = Button(frame4, text="Catalog", width=8,
                         highlightbackground="pink", foreground="black", command=back)
        button1.grid(row=2, column=6, sticky=S)
        frame4.place(relx=1, rely=1, anchor=SE)

    frame = Frame(main)
    frame.configure(background="pink")

    # Update the listbox
    def update(data):
        # Clear the listbox so it can reset each time a new berry is entered
        myList.delete(0, END)
        # Add berried top listbox
        for item in data:
            myList.insert(END, item)

    def fillout(event):
        # Deletes anything in the entry box
        myEntry.delete(0, END)
        # Add clicked list item to entry box
        myEntry.insert(0, myList.get(ANCHOR))
        if len(myEntry.get()) != 0:
            button1 = Button(frame, text="Go",
                             width=8, highlightbackground="pink", foreground="black",
                             command=lambda: back(myEntry.get()))
            button1.grid(row=4, column=6, sticky=N)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Create function to check entry vs listbox

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
        # Add berryNames to list
        update(data)

    # logo
    global logo1
    logo1 = PhotoImage(file="berrylogo.gif")
    Label(frame, image=logo1, background="pink").grid(
        row=4, column=4, sticky=W, padx=20, rowspan=2)

    # Create a list of berries
    berryNames = ['Coffeeberry', 'Gooseberry', 'Elderberry', 'Wild Grape', 'Ground Cherry',
                  'Huckleberry']

    # Created entry box
    myEntry = Entry(main, font=('Helvetica', 20))
    myEntry.pack(padx=50, pady=20)

    # Create a list box
    myList = Listbox(main, width=20)
    myList.pack(pady=20)

    # Create a binding on the listbox onclick... predicts entry based on what is in the listbox
    myList.bind('<<ListboxSelect>>', fillout)

    # Create a binding on the entry box
    myEntry.bind('<KeyRelease>', check)

    update(berryNames)

    # ---Back button to homepage---
    def back(entry):
        myEntry.pack_forget()
        myList.pack_forget()
        for widgets in frame.winfo_children():
            widgets.destroy()
            go(entry)

    frame.place(relx=0.5, rely=0.5, anchor=CENTER)


# calls mainPage
mainPage()

# run the main loop
main.mainloop()
