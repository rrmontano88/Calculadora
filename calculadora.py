'''Programa para crear una calculadora'''
from tkinter import *
from tkinter import ttk, font


def adicionarNumero(textoviejo, textonuevo):
    '''Función para agregar un número a la entrada de la calculadora'''
    global hayNumero
    if hayNumero:
        if textoviejo == "0":
            texto.set(textonuevo)
        else:
            texto.set(f"{textoviejo}{textonuevo}")
    else:
        hayNumero = True
        texto.set(textonuevo)

def adicionarComa():
    '''Función para agregarle coma a algun número'''
    textoviejo = texto.get()
    textocortado = textoviejo.split(".")
    if len(textocortado) == 1:
        texto.set(f"{textoviejo}.")
        

def limpiarEntrada():
    '''Elimina el número de la entrada'''
    texto.set("0")

def borrar():
    '''Elimina el número y la operacion guardada en memoria'''
    global ultimoNumeroIntroducido, signo, resultado
    ultimoNumeroIntroducido = 0
    signo = ""
    resultado = 0
    texto.set("0")
    textoOperacion.set("")

def borrarUltimoNumero():
    '''Borra el último número de la entrada'''
    if texto.get() != "0":
        if len(texto.get()) == 1:
            texto.set("0")
        else:
            textoviejo = texto.get()
            texto.set(textoviejo[0:-1])

def operacion(signoPasado):
    '''Asigna una operacion'''
    global hayNumero, resultado, signo
    nuevoTextoOperacion = ""
    signo = signoPasado
    if textoOperacion.get() == "":
        resultado = float(texto.get())
        
        nuevoTextoOperacion = f"{texto.get()} {signo} "
        hayNumero = False
    else:
        if not hayNumero:
            nuevoTextoOperacion = textoOperacion.get()
            nuevoTextoOperacion = f"{nuevoTextoOperacion[0:-3]} {signoPasado} "
        else:
            if textoOperacion.get()[-2] == "+":
                resultado += float(texto.get())
            if textoOperacion.get()[-2] == "-":
                resultado -= float(texto.get())
            if textoOperacion.get()[-2] == "x":
                resultado *= float(texto.get())
            if textoOperacion.get()[-2] == "/":
                resultado /= float(texto.get())
            hayNumero = False
            nuevoTextoOperacion = f"{textoOperacion.get()}{texto.get()} {signoPasado} "
            if resultado - int(resultado) == 0: #para saber si es entero el numero
                texto.set(int(resultado))
            else:
                texto.set(resultado)
    textoOperacion.set(nuevoTextoOperacion)

def signoIgual():
    '''Muestra el resultado de la operación'''
    global resultado, ultimoNumeroIntroducido, hayNumero
    if textoOperacion.get() != "":
        if signo == "+":
            resultado += float(texto.get())
        if signo == "-":
            resultado -= float(texto.get())
        if signo == "x":
            resultado *= float(texto.get())
        if signo == "/":
            resultado /= float(texto.get())
        textoOperacion.set("")
        ultimoNumeroIntroducido = float(texto.get())
        if resultado - int(resultado) == 0: #compruebo si el resultado es entero
            texto.set(int(resultado))
        else:
            texto.set(resultado)
    else:
        if signo != "":
            if signo == "+":
                resultado = float(texto.get()) + ultimoNumeroIntroducido
            if signo == "-":
                resultado = float(texto.get()) - ultimoNumeroIntroducido
            if signo == "x":
                resultado = float(texto.get()) * ultimoNumeroIntroducido
            if signo == "/":
                resultado = float(texto.get()) / ultimoNumeroIntroducido
            if resultado - int(resultado) == 0: #compruebo si el resultado es entero
                texto.set(int(resultado))
            else:
                texto.set(resultado)
    hayNumero = False




ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")
ventana.minsize(300, 400)

ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=1)
ventana.columnconfigure(2,weight=1)
ventana.columnconfigure(3,weight=1)
ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=1)
ventana.rowconfigure(2,weight=1)
ventana.rowconfigure(3,weight=1)
ventana.rowconfigure(4,weight=1)
ventana.rowconfigure(5,weight=1)
#Estilos
estilo = ttk.Style()
estilo.configure("pantallaCalc.TEntry", foreground="red", padding=10)
estilo.configure("botones.TButton", foreground="#333333", font = ("Bahnschrift Light Condensed",18))
estilo.map("botones.TButton", font=[("active",("Bahnschrift Light Condensed",30))], foreground=[("active","#007ACC")])
#Estilos

texto = StringVar()
texto.set(0)
textoOperacion = StringVar()
hayNumero = True
resultado = 0
ultimoNumeroIntroducido = 0
signo = ""

#pantalla de entrada numeros
pantalla = ttk.Entry(ventana, style="pantallaCalc.TEntry", justify=RIGHT,font=font.Font(family="DS-Digital", 
    size=30, weight=font.BOLD), width=10, textvariable=texto)
pantalla.focus()
pantalla.icursor(1)
pantalla.grid(row=0,column=0, columnspan=4, sticky="wens")

labelOperacion = ttk.Label(ventana, background="white", textvariable=textoOperacion)
labelOperacion.grid(row=0,column=0, columnspan=4, sticky="ne", padx=2, pady=2)


botonBorrarParcial = ttk.Button(ventana, text="CE", style="botones.TButton", command=limpiarEntrada)
botonBorrarParcial.grid(row=1,column=0, sticky="wesn")
botonBorrar = ttk.Button(ventana, text="C", style="botones.TButton", command=borrar)
botonBorrar.grid(row=1,column=1,sticky="wesn")
botonAtras = ttk.Button(ventana, text="<-", style="botones.TButton", command=borrarUltimoNumero)
botonAtras.grid(row=1,column=2,sticky="wesn")
botonDivicion = ttk.Button(ventana, text="/", style="botones.TButton", command=lambda:operacion("/"))
botonDivicion.grid(row=1,column=3,sticky="wesn")

boton7 = ttk.Button(ventana, text="7", style="botones.TButton", command=lambda:adicionarNumero(texto.get(), "7"))
boton7.grid(row=2,column=0, sticky="wesn")
boton8 = ttk.Button(ventana, text="8", style="botones.TButton", command=lambda:adicionarNumero(texto.get(), "8"))
boton8.grid(row=2,column=1,sticky="wesn")
boton9 = ttk.Button(ventana, text="9", style="botones.TButton", command=lambda:adicionarNumero(texto.get(), "9"))
boton9.grid(row=2,column=2,sticky="wesn")
botonDivicion = ttk.Button(ventana, text="x", style="botones.TButton", command=lambda:operacion("x"))
botonDivicion.grid(row=2,column=3,sticky="wesn")

boton4 = ttk.Button(ventana, text="4", style="botones.TButton", command=lambda:adicionarNumero(texto.get(), "4"))
boton4.grid(row=3,column=0, sticky="wesn")
boton5 = ttk.Button(ventana, text="5", style="botones.TButton", command=lambda:adicionarNumero(texto.get(), "5"))
boton5.grid(row=3,column=1,sticky="wesn")
boton6 = ttk.Button(ventana, text="6", style="botones.TButton", command=lambda:adicionarNumero(texto.get(), "6"))
boton6.grid(row=3,column=2,sticky="wesn")
botonMultiplicacion = ttk.Button(ventana, text="-", style="botones.TButton", command=lambda:operacion("-"))
botonMultiplicacion.grid(row=3,column=3,sticky="wesn")

boton1 = ttk.Button(ventana, text="1", style="botones.TButton", command=lambda:adicionarNumero(texto.get(), "1"))
boton1.grid(row=4,column=0, sticky="wesn")
boton2 = ttk.Button(ventana, text="2", style="botones.TButton", command=lambda:adicionarNumero(texto.get(), "2"))
boton2.grid(row=4,column=1,sticky="wesn")
boton3 = ttk.Button(ventana, text="3", style="botones.TButton", command=lambda:adicionarNumero(texto.get(), "3"))
boton3.grid(row=4,column=2,sticky="wesn")
botonResta = ttk.Button(ventana, text="+", style="botones.TButton", command=lambda:operacion("+"))
botonResta.grid(row=4,column=3,sticky="wesn")

botonSigno = ttk.Button(ventana, text="+/-", style="botones.TButton")
botonSigno.grid(row=5,column=0, sticky="wesn")
boton0 = ttk.Button(ventana, text="0", style="botones.TButton", command=lambda:adicionarNumero(texto.get(), "0"))
boton0.grid(row=5,column=1,sticky="wesn")
botonPunto = ttk.Button(ventana, text=".", style="botones.TButton", command=adicionarComa)
botonPunto.grid(row=5,column=2,sticky="wesn")
botonSuma = ttk.Button(ventana, text="=", style="botones.TButton", command=signoIgual)
botonSuma.grid(row=5,column=3,sticky="wesn")
ventana.mainloop()