from tkinter import *

# ----main----
window = Tk()
window.title("berrybuddy.exe")
window.configure(background="pink")
window.geometry("1000x600")

# ----Frame1 main----
def homepage():

    # ----Identify function begin----
    def identify():
        global identify
        for widgets in frame.winfo_children():
            widgets.destroy()

        # ----Frame2---Identify
        frame2 = Frame(window)
        frame2.configure(background="pink")

        # ---Back button to homepage---
        def back():
            for widgets in frame2.winfo_children():
                widgets.destroy()
                OptionMenu.destroy(frame4)
                frame3.destroy()
                homepage()

        # ---Identify page---
        test1 = Label(
            frame2, text="This is the identify page.This is the identify pageThis is the identify pageThis is the identify pageThis is the identify page")
        test1.grid(row=1, column=2, sticky=N)
        frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # ---Frame 3---
        frame3 = Frame(window)
        frame3.configure(background="pink")
        button1 = Button(frame3, text="Homepage", width=8,
                         highlightbackground="pink", foreground="black", command=back)
        button1.grid(row=2, column=6, sticky=S)
        frame3.place(relx=1, rely=1, anchor=SE)
    # ----Identify function ends----

    # ----Map function begin----

    def map():
        for widgets in frame.winfo_children():
            widgets.destroy()

        # ----Frame5---map----
        frame5 = Frame(window)
        frame5.configure(background="pink")

        # ---Back button to homepage---
        def back():
            for widgets in frame5.winfo_children():
                widgets.destroy()
                OptionMenu.destroy(frame4)
                frame6.destroy()
                homepage()

        # ---Maps page---
        test1 = Label(
            frame5, text="This is the Maps page.This is the Maps page.This is the Maps page.This is the Maps page.This is the Maps page.")
        test1.grid(row=1, column=2, sticky=N)
        frame5.place(relx=0.5, rely=0.5, anchor=CENTER)

        # ---Frame 6---
        frame6 = Frame(window)
        frame6.configure(background="pink")
        button1 = Button(frame6, text="Homepage", width=8,
                         highlightbackground="pink", foreground="black", command=back)
        button1.grid(row=2, column=6, sticky=S)
        frame6.place(relx=1, rely=1, anchor=SE)
    # ----Map function ends----

    # ----Catalog function begins----

    def catalog():
        for widgets in frame.winfo_children():
            widgets.destroy()

            # ----Frame7---catalog----
        frame7 = Frame(window)
        frame7.configure(background="pink")

        # ---Back button to homepage---
        def back():
            for widgets in frame7.winfo_children():
                widgets.destroy()
                OptionMenu.destroy(frame4)
                frame8.destroy()
                homepage()

        # ---Catalog page---
        test1 = Label(frame7, text="This is the Catalog page.")
        test1.grid(row=1, column=2, sticky=N)
        frame7.place(relx=0.5, rely=0.5, anchor=CENTER)

        # ---Frame 8---
        frame8 = Frame(window)
        frame8.configure(background="pink")
        button1 = Button(frame8, text="Homepage", width=8,
                         highlightbackground="pink", foreground="black", command=back)
        button1.grid(row=2, column=6, sticky=S)
        frame8.place(relx=1, rely=1, anchor=SE)
    # ----Catalog function ends----

    # ----About function begins----

    def about():
        for widgets in frame.winfo_children():
            widgets.destroy()

            # ----Frame9---catalog----
        frame9 = Frame(window)
        frame9.configure(background="pink")

        # ---Back button to homepage---
        def back():
            for widgets in frame9.winfo_children():
                widgets.destroy()
                OptionMenu.destroy(frame4)
                frame10.destroy()
                homepage()

        # ---About page---
        test1 = Label(
            frame9, text="This is the About page. Our names.... about")
        test1.grid(row=1, column=2, sticky=N)
        frame9.place(relx=0.5, rely=0.5, anchor=CENTER)

        # ---Frame 10---
        frame10 = Frame(window)
        frame10.configure(background="pink")
        button1 = Button(frame10, text="Homepage", width=8,
                         highlightbackground="pink", foreground="black", command=back)
        button1.grid(row=2, column=6, sticky=S)
        frame10.place(relx=1, rely=1, anchor=SE)
    # ----About function ends----

    # ---Frame 1---Homepage
    frame = Frame(window)
    frame.configure(background="pink")
    # logo
    global logo1
    logo1 = PhotoImage(file="berrylogo.gif")
    Label(frame, image=logo1, background="pink").grid(
        row=4, column=4, sticky=W, padx=20, rowspan=2)

    # button
    button1 = Button(frame, text="Identify", width=8,
                     highlightbackground="pink", foreground="black", command=identify)
    button2 = Button(frame, text="Map", width=8,
                     highlightbackground="pink", foreground="black", command=map)
    button3 = Button(frame, text="Catalog", width=8,
                     highlightbackground="pink", foreground="black", command=catalog)

    button1.grid(row=4, column=6, sticky=N)
    button2.grid(row=4, column=6, rowspan=2)
    button3.grid(row=5, column=6, sticky=S)

    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # ----Frame4----helper buttons----
    frame4 = Frame(window)
    frame4.configure(background="pink")
    # menu buttons
    aboutButton = Button(frame4, text="About", width=5, highlightbackground="pink",
                         foreground="black", command=about)

    # ---Help menu----
    helpOption = [
        "Help",
        "Help1",
        "Help2",
        "Help3"
    ]
    clicked = StringVar()
    clicked.set(helpOption[0])

    helpButton = OptionMenu(frame4, clicked, *helpOption)
    helpButton.configure(bg="pink", fg="black")

    # ----Help menu end----

    # ---Option menu----
    btnOption = [
        "Option",
        "Option1",
        "Option2",
        "Option3"
    ]
    clicked = StringVar()
    clicked.set(btnOption[0])

    optionsButton = OptionMenu(frame4, clicked, *btnOption)
    optionsButton.configure(bg="pink", fg="black")

    # ----Help menu end----

    aboutButton.grid(row=0, column=0)
    optionsButton.grid(row=0, column=1, sticky=S)
    helpButton.grid(row=0, column=2, padx=3, sticky=S)
    # anchor
    frame4.place(anchor=NW)


# ---Calls homepage to start the app----
homepage()

# run the main loop
window.mainloop()
