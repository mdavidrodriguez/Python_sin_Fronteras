from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Hola Mundo")



# root.filename = filedialog.askopenfilename(title='Elige una Foto', filetypes=(("Archivos JPG", "*.jpg"),('Todos', "*")))
# l = Label(root, text=root.filename)
# l.pack()
# img = Image.open(root.filename)
# imgTk = ImageTk.PhotoImage(img)

# l2 = Label(root, image=imgTk)
# l2.pack()

def open():
    global imgTk 
    root.filename = filedialog.askopenfilename(title='Elige una Foto', filetypes=(("Archivos JPG", "*.jpg"),('Todos', "*")))
    l = Label(root, text=root.filename)
    l.pack()
    img = Image.open(root.filename)
    imgTk = ImageTk.PhotoImage(img)

    l2 = Label(root, image=imgTk)
    l2.pack()

btn = Button(root, text="Cargar Imagen", command=open)
btn.pack()


root.mainloop()