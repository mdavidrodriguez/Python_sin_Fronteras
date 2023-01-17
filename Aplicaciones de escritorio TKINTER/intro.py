from tkinter import *

root = Tk()
root.title("Hola Mundo")
root.geometry('500x500')

l1 = Label(root,text='Hola Mundo, Mi primera etiqueta')
l2 = Label(root,text='Chao Mundo, Mi segunda etiqueta')
l3 = Label(root,text='                     ')

l1.grid(row=0,column=0)
l3.grid(row=1,column=1)
l2.grid(row=10,column=10)

root.mainloop()
