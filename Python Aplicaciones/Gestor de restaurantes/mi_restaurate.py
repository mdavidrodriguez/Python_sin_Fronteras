from tkinter import *
import random 
import datetime
from tkinter import filedialog, messagebox



operador = ''

precios_comida = [1.32,1.65,2.31,3.22,1.22,1.99,2.05,2.65]
precios_bebida = [0.25,0.99,1.21,1.54,1.08,1.10,2.00,1.58]
precios_postres = [1.54,1.68,1.32,1.97,2.55,2.14,1.94,1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comidas[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebidas[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1
    x = 0
    for c in cuadros_postre:
        if variables_postres[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida +(float(cantidad.get()) * precios_comida[p])
        p +=1


    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida +(float(cantidad.get()) * precios_bebida[p])
        p +=1


    sub_total_postres = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postres = sub_total_postres +(float(cantidad.get()) * precios_postres[p])
        p +=1
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos 

    var_costo_comida.set(f'$ {round(sub_total_comida,2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida,2)}')
    var_costo_postre.set(f'$ {round(sub_total_postres,2)}')
    var_subtotal.set(f'${round(sub_total,2)}')
    var_impuesto.set(f'$ {round(impuestos,2)}')
    var_total.set(f'$ {round(total,2)}')

def recibo():
    texto_recibo.delete(1.0,END)
    num_recibo = f'N# - {random.randint(1,1000)}' 
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'

    texto_recibo.insert(END,f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END,f'*' * 63 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 75 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t' f'${int(comida.get())* precios_comida[x]}\n')
        x +=1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t' f'${int(bebida.get())* precios_bebida[x]}\n')
        x +=1

    x = 0
    for postres in texto_postre:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t' f'${int(postres.get())* precios_postres[x]}\n')
        x +=1

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Costo de la comida: \t\t\t{var_costo_comida.get()}\n' )
    texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n' )
    texto_recibo.insert(END, f' Costo de la Postres: \t\t\t{var_costo_postre.get()}\n' )

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Sub-Total: \t\t\t{var_subtotal.get()}\n' )
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuesto.get()}\n' )
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n' )
    texto_recibo.insert(END,f'*' * 63 + '\n')
    texto_recibo.insert(END, 'Lo Esperamos Pronto')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo ha sido guardado')

def resetear():
    texto_recibo.delete(0.1,END)
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for v in variables_comidas:
        v.set(0)
    for v in variables_bebidas:
        v.set(0)
    for v in variables_postres:
        v.set(0)
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')

# Iniciar la aplicacion
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry("1050x540+0+0")

# Evitar maximixar
aplicacion.resizable(0, 0)

# Titulo de la ventana
aplicacion.title("Restaurante Los Pinos")

# Establecer color de fondo de la ventana
aplicacion.config(bg="burlywood")
# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturacion", fg="azure4",
                        font=('Arial', 48), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)
# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4", padx=50)
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=(
    "Arial", 18, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel de bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=(
    "Arial", 18, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel de Postres
panel_Postres = LabelFrame(panel_izquierdo, text='Postres', font=(
    "Arial", 18, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_Postres.pack(side=LEFT)


# Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Panel Botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# lista de productos
lista_comidas = ['pollo', 'cordero', 'pescado',
                 'merluza', 'pizza', 'Pizza2', 'Pizza3', 'Pizza4']
lista_bebidas = ['agua', 'Jugos', 'cola', 'vino',
                 'Gaseosa', 'Cerveza1', 'Cerveza2', 'Cerveza3']
lista_postres = ['helado', 'Frutas', 'brownies',
                 'flan', 'mouse', 'pastel1', 'pastel2', 'pastel3']

# Generar Items comida
variables_comidas = []
cuadros_comida = []
texto_comida = []

contador = 0
for comida in lista_comidas:
    # crear check button
    variables_comidas.append('')
    variables_comidas[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Arial', 18, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_comidas[contador], command=revisar_check)
    comida.grid(row=contador, column=0, sticky=W)

    # Crear los cuadro de entrada
    cuadros_comida.append('')
    texto_comida.append("")
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=(
        'Arial', 18, 'bold'), width=6, state=DISABLED, textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1


# Generar Items Bebidas
variables_bebidas = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Arial', 18, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebidas[contador], command=revisar_check)
    bebida.grid(row=contador, column=0, sticky=W)

    # Crear los cuadro de entrada
    cuadros_bebida.append('')
    texto_bebida.append("")
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=(
        'Arial', 18, 'bold'), width=6, state=DISABLED, textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)
    contador += 1

# Generar Items postres
variables_postres = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(panel_Postres, text=postre.title(), font=('Arial', 18, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_postres[contador], command=revisar_check)
    postre.grid(row=contador, column=0, sticky=W)


# Variables
    var_costo_comida = StringVar()
    var_costo_bebida = StringVar()
    var_costo_postre = StringVar()
    var_subtotal = StringVar()
    var_impuesto = StringVar()
    var_total = StringVar()

    # Crear los cuadro de entrada
    cuadros_postre.append('')
    texto_postre.append("")
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_Postres, font=(
        'Arial', 18, 'bold'), width=6, state=DISABLED, textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1)
    contador += 1

# Etiquetas de costos y campos de entrada
etiqueta_costo_comida = Label(panel_costos, text='Costo Comida', font=(
    'Arial', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos, font=(
    "Arial", 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# Etiqueta de costos bebidas
etiqueta_costo_bebida = Label(panel_costos, text='Costo Bebida', font=(
    'Arial', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos, font=(
    "Arial", 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# Etiqueta de costos postres
etiqueta_costo_postres = Label(panel_costos, text='Costo Postres', font=(
    'Arial', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_postres.grid(row=2, column=0)

texto_costo_postres = Entry(panel_costos, font=(
    "Arial", 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_postre)
texto_costo_postres.grid(row=2, column=1, padx=41)


# Etiqueta subtotal
etiqueta_subtotal = Label(panel_costos, text='Subtotal', font=(
    'Arial', 12, 'bold'), bg='azure4', fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos, font=("Arial", 12, 'bold'),
                       bd=1, width=10, state='readonly', textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# Etiqueta Impuesto
etiqueta_Impuesto = Label(panel_costos, text='Impuesto', font=(
    'Arial', 12, 'bold'), bg='azure4', fg='white')
etiqueta_Impuesto.grid(row=1, column=2)

texto_Impuesto = Entry(panel_costos, font=("Arial", 12, 'bold'),
                       bd=1, width=10, state='readonly', textvariable=var_impuesto)
texto_Impuesto.grid(row=1, column=3, padx=41)

# Etiqueta Total
etiqueta_Total = Label(panel_costos, text='Total', font=(
    'Arial', 12, 'bold'), bg='azure4', fg='white')
etiqueta_Total.grid(row=2, column=2)

texto_Total = Entry(panel_costos, font=("Arial", 12, 'bold'),
                    bd=1, width=10, state='readonly', textvariable=var_total)
texto_Total.grid(row=2, column=3, padx=41)


# Botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botonesCreados = []


columnas = 0
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=(
        'Arial', 13, 'bold'), fg="white", bg='azure4', bd=1, width=9)


    botonesCreados.append(boton)

    boton.grid(row=0, column=columnas)
    columnas += 1

botonesCreados[0].config(command=total)
botonesCreados[1].config(command=recibo)
botonesCreados[2].config(command=guardar)
botonesCreados[3].config(command=resetear)


# Area de recibo
texto_recibo = Text(panel_recibo, font=(
    "Arial", 12, 'bold'), bd=1, width=42, height=10)
texto_recibo.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora, font=(
    "Arial", 16, 'bold'), width=32, bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5',
                       '6', '-', '1', '2', '3', 'x', 'R', 'B', '0', '/']

botones_guardados = []


fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton.title(), font=(
        "Arial", 12, 'bold'), fg='white', bg="azure4", bd=1, width=9)

    botones_guardados.append(boton)

    boton.grid(row=fila, column=columna)
    if columna == 3:
        fila += 1
    columna += 1

    if columna == 4:
        columna = 0
botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)

botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))


# Evitar que la pantalla se cierre
aplicacion.mainloop()
