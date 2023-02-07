from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hola Mundo")

# imagen = Image.open('image1.jpg')
# imagen.show()

img = ImageTk.PhotoImage(Image.open("image5.jpg"))
l = Label(image=img)
l.pack()

root.mainloop()
