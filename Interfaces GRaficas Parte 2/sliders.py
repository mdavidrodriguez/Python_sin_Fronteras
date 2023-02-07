from tkinter import *

root = Tk()
root.title("Hola Mundo: Sliders")
vertical = Scale(root, from_=0, to=200, command=lambda x: enviar())
vertical.pack()

Horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
Horizontal.pack()

def enviar():
    hor = Horizontal.get()
    ver = vertical.get()
    print(str(hor) + ' ' + str(ver))

btn = Button(root, text="Enviar", command=enviar)
btn.pack()



root.mainloop()