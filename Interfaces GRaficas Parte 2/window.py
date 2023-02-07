from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola Mundo')

# ===================
# Solución 1
# ===================
# def open():
#     img = ImageTk.PhotoImage(Image.open("image4.jpg"))
#     top = Toplevel()
#     top.title("Hola Mundo, Nueva ventana")
#     l = Label(top,text="Soy un textto en una segunda ventana")
#     l2 = Label(top,image=img)
#     l.pack()
#     l2.pack()
#     top.mainloop()


# ====================
# Solución 2 
#  ==================
# def open():
#     global img
#     img = ImageTk.PhotoImage(Image.open("image6.jpg"))
#     top = Toplevel()
#     top.title("Hola Mundo, Nueva ventana")
#     l = Label(top,text="Soy un textto en una segunda ventana")
#     l2 = Label(top,image=img)
#     l.pack()
#     l2.pack()



# ====================
# Solución 3
#  ==================
def open(img):
    top = Toplevel()
    top.title("Hola Mundo, Nueva ventana")
    l = Label(top,text="Soy un textto en una segunda ventana")
    l2 = Label(top,image=img)
    l.pack()
    l2.pack()

img = ImageTk.PhotoImage(Image.open("image6.jpg"))
btn = Button(root, text="Click", command= lambda:open(img)).pack()

root.mainloop()