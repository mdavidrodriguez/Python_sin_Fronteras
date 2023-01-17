from tkinter import *
from tkinter import messagebox


root  = Tk()

# def click():
#     messagebox.showwarning('Popup', 'Hola Mundo')

# def click():
#     messagebox.showinfo('Popup', 'Hola Mundo')

# def click():
#     messagebox.showerror('Popup', 'Hola Mundo:()')

# def click():
#   respuesta =   messagebox.askquestion('Popup', 'Hola Mundo:(')
#   if respuesta == 'yes':
#     messagebox.showinfo('respuesta ', 'la respuesta fue ' + respuesta)
#   else:
#     messagebox.showinfo('Respuesta', 'la respuesta fue '+ respuesta)

# def click():
#    respuesta =  messagebox.askokcancel('Hola Mundo', 'Desea realizar accion')
#    if respuesta:
#        messagebox.showinfo('Hola Mundo', 'La respuesta fue ok')
#    else:
#         messagebox.showinfo('Hola Mundo', 'La respuesta fue cancelar')


def click():
   respuesta =  messagebox.askyesno('Hola Mundo', 'Desea realizar accion')
   print(respuesta)
   if respuesta:
       messagebox.showinfo('Hola Mundo', 'La respuesta fue Yes')
   else:
        messagebox.showinfo('Hola Mundo', 'La respuesta fue no')


root.title('Hola Mundo')
btn = Button(root,text='Presioname',command=click)
btn.pack()

root.mainloop()
