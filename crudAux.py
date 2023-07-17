# Importar Bibliotecas
#Este proyecto estara en el repo de escuela python
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Desarrollo de la interfaz grafica
root=Tk()
root.title("Colegio Huyapari, Aplicacion CRUD con base de datos")
root.geometry("900x550")

miId=StringVar()
miCedula=StringVar()
miApellido=StringVar()
miNombre=StringVar()
miFechaNacimiento=StringVar()
miFechadeIngreso=StringVar()
miCargo=StringVar
miSueldoBasico=StringVar()
miDescripción=StringVar()

def conexionBBDD():
    rutaBd="C:/Users/FACS/Desktop/Escuela Python/MyCode/proyectoNomina/crudNomina/Nomina.db"
    miConexion=sqlite3.connect(rutaBd)
    miCursor=miConexion.cursor()

    try:
        miCursor.execute("""
        CREATE TABLE empleado(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CI VARCHAR(11) NOT NULL,
        APELLIDOS VARCHAR(50) NOT NULL,
        NOMBRES VARCHAR(50) NOT NULL,
        FECHANACIMIENTO DATETIME,
        FECHADENGRESO DATETIME,
        CARGO VARCHAR(50) NOT NULL,
        SUELDOBASICO REAL NOT NULL,
        DESCRIPCION TEXT
        )
        """)
        


        messagebox.showinfo("CONEXION","Base de datos creada exitosamente")
    except:
        messagebox.showinfo("CONEXION","Conexion exitosa con la base de datos")

def eliminarBBDD():
    miConexion=sqlite3.connect("Nomina.db")
    miCursor=miConexion.cursor()
    if messagebox.askyesno(message="Los datos se perderan definitivamente, Desea continuar ?",title="ADVERTENCIA"):
        miCursor.execute("DROP TABLE empleado")
    else:
        pass

def salirAplicacion():
    valor=messagebox.askquestion("Salir","Estas seguro que deseas salir de la aplicacion")
    if valor=="yes":
        root.destroy()

def limpiarCampos():
    miCedula.set(" ")
    miApellido.set(" ")
    miNombre.set(" ")
    miFechaNacimiento.set(" ")
    miFechadeIngreso.set(" ")
    miCargo.set(" ")
    miSueldoBasico.set(" ")
    miDescripción.set(" ")

def mensaje():
    acerca="""
    Escuela Python
    Alplicación CRUD
    Versión 1.0
    Tecnologia Python Tkinter
    """

################################ Métodos CRUD ######################

def crear():
    miConexion=sqlite3.connect("Nomina1.db")
    miCursor=miConexion.cursor()
    try:
        datos=miCedula.get(),miApellido.get(),miNombre.get(),miFechaNacimiento.get(),miFechadeIngreso.get(),miCargo.get(),miSueldoBasico.get()
        miCursor.execute("INSERT INTO empleado VALUES(NULL,?,?,?,?,?,?,?)",(datos))
        miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique su conexión a a BBDD")
        pass
    limpiarCampos()
    mostrar()

def mostrar():
    miConexion=sqlite3.connect("Nomina.db")
    miCursor=miConexion.cursor()
    registros=tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        miCursor.execute("SELECT * FROM empleado")
        for row in miCursor:
            tree.insert("",0,text=row[0], values=(row[1],row[2],row[3]))
    except:
        pass

########################  TABLA   ########################################

tree=ttk.Treeview(height=10, columns=('#0','#1','#2','#3','#4','#5'))
tree.place(x=40,y=250)

tree.column('#0',width=50)
tree.heading('#0',text="ID", anchor=CENTER)

tree.column('#1',width=150)
tree.heading('#1',text="Nombre del Empleado", anchor=CENTER)

tree.column('#2',width=150)
tree.heading('#2',text="Apellido del Empleado", anchor=CENTER)

tree.heading('#3',text="Cargo del Empleado", anchor=CENTER)
tree.column('#3',width=150)

tree.heading('#4',text="Salario", anchor=CENTER)
tree.column('#4',width=80)


tree.heading('#5',text="Fecha de Nacimiento", anchor=CENTER)
tree.column('#5',width=120)

tree.heading('#6',text="Fecha de Ingreso", anchor=CENTER)
tree.column('#6',width=120)

def Actualizar():
    miConexion=sqlite3.connect("Nomina.db")
    miCursor=miConexion.cursor()
    try:
        datos=miNombre.get(),miApellido.get(),miCargo.get(),miSueldoBasico.get(),miFechaNacimiento.get(),miFechadeIngreso()
        #miCursor.execute("UPDATE empleado SET NOMBRE=?,APELLIDO=?,CARGO=?,SALARIO=?,FECHANACIMIENTO=?,FECHAINGRESO=? WHERE ID="miId.get(),(datos))
        miConexion.commit()
    except:
        messagebox.askyesno("ADVERTENCIA, ocurrio un error al actualizar el registro")

        pass
    limpiarCampos()
    mostrar()
def borrar():
    miConexion=sqlite3.connect("Nomina.db")
    miCursor=miConexion.cursor()
    try:
        if messagebox.askyesno(message="¿ Desea eliminar el registro ?",title="ADVERTENCIA"):
            miCursor.execute("DELETE FROM empleado WHERE ID="+miId.get())
    except:
        messagebox.askyesno("ADVERTENCIA, ocurrio un error al tratar de eliminar el registro")
        pass

############## Crear Menu #####################

menubar=Menu(root)
menubasedat=Menu(menubar,tearoff=0)
menubasedat.add_command(label="Crear/Conectar base de Datos", command=conexionBBDD)
menubasedat.add_command(label="Eliminar Base de Datos", command=eliminarBBDD)
menubasedat.add_command(label="Salir", command=salirAplicacion)
menubar.add_cascade(label="Inicio", menu=menubasedat)

ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Resetear Campos", command=limpiarCampos)
ayudamenu.add_command(label="Acerca", command=mensaje)
menubar.add_cascade(label="Ayuda", menu=ayudamenu)

################## Creando etiquetes y cajas de textos ############################
e1=Entry(root, textvariable=miId)

labelCedula=Label(root, text="Ingrese Cedula:")
labelCedula.place(x=40,y=20)
entryCedula=Entry(root, textvariable=miCedula, width=10)
entryCedula.place(x=135,y=20)

labelTituloCrud=Label(root, text="S I S T E M A  N O M I N A  H U Y A P A R I")
labelTituloCrud.place(x=350,y=5)

labelApellidos=Label(root, text="Apellidos:")
labelApellidos.place(x=40,y=60)
entryApellidos=Entry(root, textvariable=miApellido,width=30)
entryApellidos.place(x=100,y=60)

labelNombres=Label(root, text="Nombres:")
labelNombres.place(x=300,y=60)
entryNombres=Entry(root, textvariable=miNombre,width=30)
entryNombres.place(x=360,y=60)

labelFechaIngreso=Label(root, text="Fecha de Ingreso:")
labelFechaIngreso.place(x=40,y=100)
entryFechaIngreso=Entry(root,textvariable=miFechadeIngreso,width=11)
entryFechaIngreso.place(x=140,y=100)

labelFechaIngreso=Label(root, text="Fecha de Ingreso:")
labelFechaIngreso.place(x=40,y=100)
entryFechaIngreso=Entry(root,textvariable=miFechadeIngreso,width=11)
entryFechaIngreso.place(x=140,y=100)

labelFechaNacimiento=Label(root,text="Fecha de Nacimiento:")
labelFechaNacimiento.place(x=230,y=100)
entryFechaNacimiento=Entry(root,textvariable=miFechaNacimiento,width=11)
entryFechaNacimiento.place(x=350,y=100)

labelCargo=Label(root, text="Cargo:")
labelCargo.place(x=40,y=140)
entryCargo=Entry(root, textvariable=miCargo,width=50)
entryCargo.place(x=80,y=140)


labelSalario=Label(root, text="Salario:")
labelSalario.place(x=280,y=140)
entrySalario=Entry(root, textvariable=miSueldoBasico, width=10)
entrySalario.place(x=325,y=140)
labelBolivares=Label(root,text="Bs.d")
labelBolivares.place(x=400,y=140)

################ Creando Botones ##########################

botonCrearRegistro=Button(root, text="Crear Registro", command=crear)
botonCrearRegistro.place(x=40,y=200)

botonModificarRegistro=Button(root, text="Modificar Registro", command=Actualizar)
botonModificarRegistro.place(x=150,y=200)

botonMostrarRegistro=Button(root, text="Mostrar Registro", command=mostrar)
botonMostrarRegistro.place(x=280,y=200)

botonEliminarRegistro=Button(root, text="Eliminar Registro", bg="red", command=borrar)
botonEliminarRegistro.place(x=390,y=200)
root.config(menu=menubar)




root.mainloop()
