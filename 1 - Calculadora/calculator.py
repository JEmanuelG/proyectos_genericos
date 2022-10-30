
from tkinter import *

# VENTANA PRINCIPAL
root = Tk()

root.title('Mi calculadora')
root.geometry('350x400')
# PONE EN FALSO RESIZABLE PARA QUE EL TAMAÑO LA VENTANA NO SE PUEDA MODIFICAR
root.resizable(False,False)
root.config(background='gray')

# Funciones
operacion = ''
resultado = StringVar()
flag_result = False

def resetear():
    global operacion
    global resultado
    
    operacion = ''
    calculator_display.delete(0, END)

def pulsar(valor):
    global operacion
    global resultado
    
    operacion += str(valor)
    calculator_display.delete(0, END)
    calculator_display.insert(0, operacion)

def calcular():
    global operacion
    global resultado

    try:
        resultado = str(eval(operacion))
    except:
        resultado = 'Error'
    finally:
        calculator_display.delete(0, END)
        calculator_display.insert(0, resultado)
        operacion = ''



#                       *** PANTALLA ***
calculator_display = Entry(root,font=('arial',20, 'bold'), borderwidth=2)
calculator_display.grid(row=0, column=0, columnspan=4, pady=10, padx=20)

#                       *** TECLADO ***
# BOTON BORRAR AC
button_ac = Button(root, text='AC', width=8, height=2, background='red', command=lambda:resetear())
button_ac.grid(row=1, column=0, pady=5)


# NÚMEROS
button_cero = Button(root, text='0', width=20, height=2, command=lambda:pulsar('0'))
button_cero.grid(row=5, column=0, columnspan=2, pady=5)
button_one = Button(root, text='1', width=8, height=2, command=lambda:pulsar('1'))
button_one.grid(row=4, column=0, pady=5)
button_two = Button(root, text='2', width=8, height=2, command=lambda:pulsar('2'))
button_two.grid(row=4, column=1, pady=5)
button_three = Button(root, text='3', width=8, height=2, command=lambda:pulsar('3'))
button_three.grid(row=4, column=2, pady=5)
button_four = Button(root, text='4', width=8, height=2, command=lambda:pulsar('4'))
button_four.grid(row=3, column=0, pady=5)
button_five = Button(root, text='5', width=8, height=2, command=lambda:pulsar('5'))
button_five.grid(row=3, column=1, pady=5)
button_six = Button(root, text='6', width=8, height=2, command=lambda:pulsar('6'))
button_six.grid(row=3, column=2, pady=5)
button_seven = Button(root, text='7', width=8, height=2, command=lambda:pulsar('7'))
button_seven.grid(row=2, column=0, pady=5)
button_eight = Button(root, text='8', width=8, height=2, command=lambda:pulsar('8'))
button_eight.grid(row=2, column=1, pady=5)
button_nine = Button(root, text='9', width=8, height=2, command=lambda:pulsar('9'))
button_nine.grid(row=2, column=2, pady=5)

# OPERACIONES
button_point = Button(root, text='.', width=8, height=2, command=lambda:pulsar('.'))
button_point.grid(row=5, column=2, pady=1)
button_mult = Button(root, text='*', width=8, height=2, command=lambda:pulsar('*'))
button_mult.grid(row=1, column=2, pady=1)
button_div = Button(root, text='/', width=8, height=2, command=lambda:pulsar('/'))
button_div.grid(row=1, column=1, pady=1)
button_add = Button(root, text='+', width=6, height=5, command=lambda:pulsar('+'))
button_add.grid(row=2, column=3, rowspan=2, pady=1)
button_subt = Button(root, text='-', width=6, height=2, command=lambda:pulsar('-'))
button_subt.grid(row=1, column=3, pady=1)
button_equal = Button(root, text='=', width=6, height=5, command=lambda:calcular())
button_equal.grid(row=4, column=3, rowspan=2, pady=1)

root.mainloop()

