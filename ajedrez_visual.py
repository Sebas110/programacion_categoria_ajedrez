from tkinter import *
from tkinter import messagebox
from datetime import datetime

now = datetime.now()

año_act = now.year
def reset():
      ventana2.destroy()
      inicio()
def inicio():
    global ventana,entrada
    ventana= Tk()
    ventana.title("inicio")
    ventana.attributes("-topmost",True)
    ventana.geometry("500x300+700+250")

    ventana.config(bg="#9DD0EA")
    ventana.resizable(0,0)

    texto = Label(ventana,text="Ingrese año de nacimiento",fg="black",bg="white",font="arial 28")
    texto.place(x=40,y=10)

    entrada= Entry(ventana,font="arial 20",justify=CENTER,selectborderwidth=2)

    entrada.place(x=100,y=80)

    listo=Button(ventana,text="Listo",font="arial 20",command=agregar)
    listo.place(x=215,y=150)
    
    cerrar=Button(ventana,text="X",font="ariañ 13",fg="red",command=ventana.destroy)
    cerrar.place(x=10,y=260)
    ventana.mainloop()

def agregar():
    global año_usu,edad_usu,ventana2
    año_usu=int(entrada.get())
    edad_usu= (año_act - año_usu)


    ventana2= Tk()
    ventana2.title("registro")
    ventana2.geometry("500x300+700+250")
    ventana.destroy()
    ventana2.config(bg="#9DD0EA")
    ventana2.resizable(0,0)
    proceso()
    texto2= Label(ventana2,text="Año de nacimiento",fg="black",bg="white",font="arial 28")
    texto2.place(x=110,y=10)

    texto3 = Label(ventana2,text= año_usu,fg="black",bg="#9DD0EA",font="arial 30")
    texto3.place(x=200,y=60)

    texto4= Label(ventana2,text="Edad",fg="black",bg="white",font="arial 28")
    texto4.place(x=195,y=100)

    texto5= Label(ventana2,text=edad_usu,fg="black",bg="#9DD0EA",font="arial 28")
    texto5.place(x=215,y=150)
    
    texto6= Label(ventana2,text="Categoria",fg="black",bg="white",font="arial 28")
    texto6.place(x=160,y=200)

    texto7= Label(ventana2,text=categoria,fg="black",bg="#9DD0EA",font="arial 28")
    texto7.place(x=170,y=250)

    cerrar=Button(ventana2,text="X",font="arial 13",fg="red",command=ventana2.destroy)
    cerrar.place(x=10,y=260)

    restart=Button(ventana2,text="Reset",font="arial 13",fg="red",command=reset)
    restart.place(x=430,y=260)
    

def proceso():
    global categoria,ventana2
    if edad_usu < 15 and edad_usu > 0:
            categoria= ("infantil")
       
#categoría Junior
    elif edad_usu >= 15 and edad_usu <= 18:
            categoria=("Junior")
    
#categoría Amateur
    elif edad_usu > 18 and edad_usu <= 120:
            categoria=("Amateur")
    else: 
        while edad_usu >= 120 or edad_usu <=1:
            global ventana_error
            ventana2.destroy()
            
            messagebox.showinfo(message="Error: ingresar el año correcto", title="ERROR")
            inicio()
            


inicio()
