print("Calculator!!")

from tkinter import *
import operations

# VENTANA PRINCIPAL
root = Tk()

root.title('Mi calculadora')
root.geometry('350x600')
# PONE EN FALSO RESIZABLE PARA QUE EL TAMAÑO LA VENTANA NO SE PUEDA MODIFICAR
root.resizable(False,False)
root.config(background='grey')

#                       *** DISPLAY ***
calculator_display = Entry(root,font=('arial',20, 'bold'), borderwidth=2)
calculator_display.grid(row=0, column=0, columnspan=4, pady=10, padx=20)

#                       *** TECLADO ***
# BOTON BORRAR AC
button_ac = Button(root, text='AC', width=8, height=2, background='red')
button_ac.grid(row=1, column=0, pady=5)


# NÚMEROS
button_cero = Button(root, text='0', width=20, height=2).grid(row=5, column=0, columnspan=2, pady=5)
button_one = Button(root, text='1', width=8, height=2).grid(row=4, column=0, pady=5)
button_two = Button(root, text='2', width=8, height=2).grid(row=4, column=1, pady=5)
button_three = Button(root, text='3', width=8, height=2).grid(row=4, column=2, pady=5)
button_four = Button(root, text='4', width=8, height=2).grid(row=3, column=0, pady=5)
button_five = Button(root, text='5', width=8, height=2).grid(row=3, column=1, pady=5)
button_six = Button(root, text='6', width=8, height=2).grid(row=3, column=2, pady=5)
button_seven = Button(root, text='7', width=8, height=2).grid(row=2, column=0, pady=5)
button_eight = Button(root, text='8', width=8, height=2).grid(row=2, column=1, pady=5)
button_nine = Button(root, text='9', width=8, height=2).grid(row=2, column=2, pady=5)

# OPERACIONES
button_point = Button(root, text='.', width=8, height=2).grid(row=5, column=2, pady=1)
button_mult = Button(root, text='*', width=8, height=2).grid(row=1, column=2, pady=1)
button_div = Button(root, text='/', width=8, height=2).grid(row=1, column=1, pady=1)
button_add = Button(root, text='+', width=6, height=5).grid(row=2, column=3, rowspan=2, pady=1)
button_subt = Button(root, text='-', width=6, height=2).grid(row=1, column=3, pady=1)
button_equal = Button(root, text='=', width=6, height=5).grid(row=4, column=3, rowspan=2, pady=1)

root.mainloop()

