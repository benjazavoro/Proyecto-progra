from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser


raizEmpleadoCliente = Tk()
raizEmpleadoCliente.title("Menu Principal")

#------------------MenuEmpleado-------------------------------------------
def MenuEmpleado():
    raiz= Toplevel(raizEmpleadoCliente)
    raiz.title("Menu Empleado")

    #------------------------Pantalla Menu Empleado -----------------------------------------------------
    frameinicialEmpleado = Frame(raiz, width=700, height=500)
    frameinicialEmpleado.pack()
    frameinicialEmpleado.config(bg="#B5CBDC")

    #Imagen 
    fotoempleadomenu = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\IC2.png")
    labelfotoempleado = Label(frameinicialEmpleado, image=fotoempleadomenu, width=185, height=200)
    labelfotoempleado.pack()
    labelfotoempleado.place(x=35, y=150)

    #Boton Ver Menu
    BotonVerMenu = Button(frameinicialEmpleado, width=45, height=5, text="Ver Menú", command=VerMenu)
    BotonVerMenu.place(x=250, y=100)
    #Boton Ver registro
    BotonVerRegistro = Button(frameinicialEmpleado, width=45, height=5, text="Ver Registro", command=lambda: webbrowser.open("Registro_clientes.txt"))
    BotonVerRegistro.place(x=250, y=200)
    #Boton Regresar menu principal
    BotonRefresarmenu = Button(frameinicialEmpleado, width=45, height=5, text="Regresar Menu Principal", command=lambda: raiz.destroy())
    BotonRefresarmenu.place(x=250, y=300)

    raiz.mainloop()
#------------------MenuCliente--------------------------------------------
def MenuCliente():
    raiz= Toplevel(raizEmpleadoCliente)
    raiz.title("Menu Cliente")
    #------------------------Pantalla Menu Cliente -----------------------------------------------------
    frameinicialCliente = Frame(raiz, width=700, height=500)
    frameinicialCliente.pack()
    frameinicialCliente.config(bg="#B5CBDC")

    #Imagen Cliente
    fotoclientemenu = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\Mariachibien.png")
    labelfotocliente = Label(frameinicialCliente, image=fotoclientemenu, width=185, height=250)
    labelfotocliente.pack()
    labelfotocliente.place(x=35, y=109)
    labelfotocliente.config(bg="#B5CBDC")

    #Boton Ver Menu
    BotonVerMenu = Button(frameinicialCliente, width=45, height=5, text="Ver Menú", command=VerMenu)
    BotonVerMenu.place(x=250, y=150)
    #Boton Regresar menu principal
    BotonRefresarmenu = Button(frameinicialCliente, width=45, height=5, text="Regresar Menu Principal", command=lambda: raiz.destroy())
    BotonRefresarmenu.place(x=250, y=250)


    raiz.mainloop()
#------------------VerMenu------------------------------------------------
def VerMenu():
    raiz=Toplevel(raizEmpleadoCliente)
    miframe=Frame(raiz, width=1000 , heigh=700)
    miframe.pack()

    raiz.title("Menu")

    Menulabel=Label(miframe, text="Menu")
    Menulabel.place(x=450, y=0)
    Menulabel.config(font=("Courier", 25, "italic"))

    fotoHome = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\home.png")
    Botonhome = Button(miframe, image=fotoHome, width=50, height=50, command=lambda: raiz.destroy())
    Botonhome.place(x=900, y=0)

    Menulabel2=Label(miframe, text="Enchiladas - $40")
    Menulabel2.place(x=120, y=120)
    Menulabel2.config(font=("Courier", 20, "italic"))

    Fotoenchiladas = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\enchiladas.png")
    labelenchiladas = Label(miframe, image=Fotoenchiladas, width=100, height=100)
    labelenchiladas.pack()
    labelenchiladas.place(x=10, y=90)

    Menulabel3=Label(miframe, text="Enmoladas - $35")
    Menulabel3.place(x=120, y=220)
    Menulabel3.config(font=("Courier", 20, "italic"))

    Fotoenmoladas = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\enmoladas.png")
    labelenmoladas = Label(miframe, image=Fotoenmoladas, width=100, height=100)
    labelenmoladas.pack()
    labelenmoladas.place(x=10, y=200)

    Menulabel4=Label(miframe, text="Pozole - $65")
    Menulabel4.place(x=120, y=320)
    Menulabel4.config(font=("Courier", 20, "italic"))

    Fotopozole = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\pozole.png")
    labelpozole = Label(miframe, image=Fotopozole, width=100, height=100)
    labelpozole.pack()
    labelpozole.place(x=10, y=290)

    Menulabel5=Label(miframe, text="Mole - $90")
    Menulabel5.place(x=120, y=420)
    Menulabel5.config(font=("Courier", 20, "italic"))

    Fotomole = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\mole.png")
    labelmole = Label(miframe, image=Fotomole, width=100, height=100)
    labelmole.pack()
    labelmole.place(x=10, y=390)

    Menulabel6=Label(miframe, text="Burritos - $45")
    Menulabel6.place(x=120, y=520)
    Menulabel6.config(font=("Courier", 20, "italic"))

    Fotoburritos = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\burrito.png")
    labelburritos = Label(miframe, image=Fotoburritos, width=100, height=100)
    labelburritos.pack()
    labelburritos.place(x=10, y=490)

    Menulabel7=Label(miframe, text="Flautas - $40")
    Menulabel7.place(x=120, y=620)
    Menulabel7.config(font=("Courier", 20, "italic"))

    Fotoflauta = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\flautas.png")
    labelflauta = Label(miframe, image=Fotoflauta, width=100, height=100)
    labelflauta.pack()
    labelflauta.place(x=10, y=590)

    Menulabel8=Label(miframe, text="Refresco - $20")
    Menulabel8.place(x=650, y=120)
    Menulabel8.config(font=("Courier", 20, "italic"))

    Fotorefresco = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\refresco.png")
    labelrefresco = Label(miframe, image=Fotorefresco, width=100, height=100)
    labelrefresco.pack()
    labelrefresco.place(x=540, y=90)

    Menulabel9=Label(miframe, text="Agua fresaca - $25")
    Menulabel9.place(x=650, y=220)
    Menulabel9.config(font=("Courier", 20, "italic"))

    Fotoagua = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\agua.png")
    labelagua = Label(miframe, image=Fotoagua, width=100, height=100)
    labelagua.pack()
    labelagua.place(x=540, y=190)

    Menulabel10=Label(miframe, text="Cafe - $10")
    Menulabel10.place(x=700, y=320)
    Menulabel10.config(font=("Courier", 20, "italic"))

    Fotofcafe = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\cafe.png")
    labelcafe = Label(miframe, image=Fotofcafe, width=100, height=100)
    labelcafe.pack()
    labelcafe.place(x=540, y=290)

    Menulabel11=Label(miframe, text="Jugo - $20")
    Menulabel11.place(x=700, y=420)
    Menulabel11.config(font=("Courier", 20, "italic"))

    Fotojugo = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\jugo.png")
    labeljugo = Label(miframe, image=Fotojugo, width=100, height=100)
    labeljugo.pack()
    labeljugo.place(x=540, y=390)

    #Flautas = 40
    #Enchiladas = 30
    #Enmoladas = 35
    #Pozole = 65
    #Mole = 90
    #Burritos = 45

    #Refresco = 20
    #Agua fresaca = 25
    #Cafe = 10
    #jugo = 20

    BotonPedido = Button(miframe, width=20, height=5, text="Pedir", command=verpedido)
    BotonPedido.place(x=800, y=580)

    raiz.mainloop()
#------------------VerPedido----------------------------------------------
def verpedido():
    win= Tk()
    win.title("Pedir")
    miframe=Frame(win, width=500 , heigh=400)
    miframe.pack()

    def get_value():
        e_text=entry.get()
        pedido = e_text.split(",")
        resultado = []
        for p in pedido:
            resultado.append(p.lower())
        pedido=resultado
        menu ={
            "flautas" : float(40),
            "enchiladas" : float(30),
            "enmoladas" : float(35),
            "pozole" : float(65),
            "mole" : float(90),
            "burritos" :float(45),
            "quesadillas": float(20),
            "tortas" : float(70),
            "sopes" :float(15),
            "tamales": float(20),
            "frijoles":float(40),
            "birria": float(80),
            "cocacola":float(15),
            "pepsi" : float(13),
            "manzanita" : float(10),
            "squirt":float(15),
            "jugo":float(20),
            "cafe":float(10)
        }

        total = 0
        ticket= ""
        pedidosexistentes = []
        for comida in pedido:
            if comida in menu:
                total += menu[comida]
                pedidosexistentes.append(comida)
                ticket+="\n"+comida + "..... $" + str(menu[comida])
            
        ticket+="\nTotal " + str(total)


        Label(win, text=ticket, font= ('Century 15 bold')).pack()
        #-------------Base de datos---------------#
        archivo = open("Registro_clientes.txt","a")
        archivo.write("Registro de todas las comidas\n")
        nombre=entrynombre.get()
        archivo.write(nombre + '\n')
        archivo.write(f'pedidos={ pedidosexistentes }')

        archivo.close()

    entry= ttk.Entry(win,font=('Century 12'),width=40)
    entry.pack()
    entry.place(x=65, y=50)

    button= ttk.Button(win, text="Enter", command= get_value)
    button.pack()
    button.place(x=210, y=200)

    NombreClientelabel = Label(miframe, text="Nombre")
    NombreClientelabel.place(x=180, y=90)
    NombreClientelabel.config(font=("Courier", 25, "italic"))

    entrynombre = Entry(win,font=('Century 12'),width=40)
    entrynombre.pack()
    entrynombre.place(x=65, y=130)

    Pedirlabel=Label(miframe, text="Pedir")
    Pedirlabel.place(x=200, y=10)
    Pedirlabel.config(font=("Courier", 25, "italic"))



    win.mainloop()
#-----------------ContraseñaEmpleado------------------------------------
def Contrausuario():
    raiz = Toplevel(raizEmpleadoCliente)
    raiz.title("Seguridad Usuario")

    frameSeguridad = Frame(raiz, width=500, height=500) 
    frameSeguridad.pack()
    frameSeguridad.config(bg="#B5CBDC")

    fotoSeguridad = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\Usuario.png")
    labelfotoSeguridad = Label(frameSeguridad, image=fotoSeguridad, width=185, height=200)
    labelfotoSeguridad.pack()
    labelfotoSeguridad.place(x=150, y=90)

    def compararcontra():
        contrasena=entrycontra.get()
        if contrasena == '1234':
            raiz.destroy()
            MenuEmpleado()
        else:
            messagebox.showerror(message="Contraseña incorrecta", title="Seguridad")
        

    entrycontra = Entry(frameSeguridad,font=('Century 12'),width=20)
    entrycontra.pack()
    entrycontra.place(x=150, y=300)
    entrycontra.config(show="*")

    botonenter = Button(frameSeguridad, text="Enter",width=10, command=compararcontra)
    botonenter.pack()
    botonenter.place(x=200, y=325)

    

    raiz.mainloop()

#------------------------Pantalla botones Empleado Cliente-------------------------------------------------------------
frameClienEmpleado = Frame(raizEmpleadoCliente, width=600, height=450)
frameClienEmpleado.pack()
frameClienEmpleado.config(bg="#B5CBDC")

#Imagen Empleado-Cliente
fotoEmpleado = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\Empleado.png")
fotoCliente = PhotoImage(file= r"D:\Udg\PrimerSemestre\FundamentosdelaProgramacion\ProyectoInter\Proyecto de Programacion Final\images\Cliente.png")
#Botones empleado
BotonEmpleado = Button(frameClienEmpleado, width=200,height=150,image=fotoEmpleado, command=Contrausuario)
BotonEmpleado.place(x=50, y=100)
labelEmpleado = Label(frameClienEmpleado, text= "Empleado")
labelEmpleado.place(x=105, y=260)
labelEmpleado.config(font="Montserrat",bg="#B5CBDC")

#Boton Cliente
BotonCliente = Button(frameClienEmpleado, width=200, height=150, image=fotoCliente, command=MenuCliente)
BotonCliente.place(x=340, y= 100)
labelCliente = Label(frameClienEmpleado, text="Cliente")
labelCliente.place(x=415, y=260)
labelCliente.config(font="Montserrat", bg="#B5CBDC")



raizEmpleadoCliente.mainloop()
