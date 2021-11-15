import tkinter as tk
from typing_extensions import _AnnotatedAlias
from PIL import ImageTk, Image
from tkinter import filedialog
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np


def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()

    image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                       filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth = 150
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    file_name = image_data.split('/')
    panel = tk.Label(frame, text= str(file_name[len(file_name)-1]).upper()).pack()
    panel_image = tk.Label(frame, image=img).pack()

    classify()

def classify():

    np.set_printoptions(suppress=True)

    model = load_model('keras_model.h5')

    with open('labels.txt', 'r') as f:
       class_names = f.read().split('\n')

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    berry_image = Image.open(image_data)

    size = (224, 224)
    berry_image = ImageOps.fit(berry_image, size, Image.ANTIALIAS)

    image_array = np.asarray(berry_image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)

    index = np.argmax(prediction)
    class_name = class_names[index]
    result = tk.Label(frame, text=class_name).pack()

    print("The class is ", class_name)


root = tk.Tk()
root.resizable(False, False)
root.title("berrybuddy.exe")
root.configure(background="#E2C7D8")
root.geometry("1000x600")

tit = tk.Label(root, text="Berry Buddy", padx=25, pady=6, font=("", 12)).pack()


frame = tk.Frame(root, highlightbackground="#95658B", highlightthickness=4, bg="#F2F2F2")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

chose_image = tk.Button(root, text='Upload',
                        padx=35, pady=10,
                        fg="#0D0D0D", bg="#E2C7D8", command=load_img)
chose_image.pack(side=tk.BOTTOM)



root.mainloop()