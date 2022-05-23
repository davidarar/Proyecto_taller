from ast import Lambda
import tkinter as tk
from tkinter import Button, Entry, Label, StringVar,ttk
from lista_usuarios import Estudiante,Administrativo,Cursos
from tkinter.messagebox import showwarning, askyesno
from accionesVentanas import volverVentana,cerrarVentana,ocultarVentana


class RegistroEst:

    sv_nombre,sv_apellido1,sv_apellido2,sv_carrera,sv_username,sv_contra=[None,None,None,None,None,None]

    def __init__(self) -> None:
        
        #ventana registro Estudiante
        self.vtna_registro=tk.Tk()
        self.vtna_registro.geometry("400x350")
        self.vtna_registro.title("Administrador del Tiempo")
        self.vtna_registro.resizable(False,False)
        self.lb_registro=Label(self.vtna_registro, text = 'Registro de Estudiante', font = ("Cambria", 22))
        self.lb_registro.place(x=75,y=20)


        #Texto y entradas de datos
        Label(self.vtna_registro,text = "Nombre:",font = ("Cambria", 12)).place(x = 25, y = 70)
        self.sv_nombre = StringVar(self.vtna_registro)
        Entry(self.vtna_registro,textvariable = self.sv_nombre , width = "33").place(x = 120, y = 75)

        Label(self.vtna_registro,text = "1° Apellido:",font = ("Cambria", 12)).place(x = 25, y = 105)
        self.sv_apellido1 = StringVar(self.vtna_registro)
        Entry(self.vtna_registro,textvariable = self.sv_apellido1, width = "33").place(x = 120, y = 110)

        Label(self.vtna_registro,text = "2° Apellido:",font = ("Cambria", 12)).place(x = 25, y = 140)
        self.sv_apellido2 = StringVar(self.vtna_registro)
        Entry(self.vtna_registro,textvariable = self.sv_apellido2, width = "33").place(x = 120, y = 145)
        
        Label(self.vtna_registro,text = "Carrera:",font = ("Cambria", 12)).place(x = 25, y = 175)
        self.sv_carrera = StringVar(self.vtna_registro)

        comboCarreras = ttk.Combobox(self.vtna_registro,values=[
                                            "Computacion", 
                                            "Electronica",
                                            "Agronomia",
                                            "Administracion de Empresas"],
                                            state="readonly",width = "26",font = ("Cambria", 10),textvariable=self.sv_carrera).place(x = 120, y = 180)


        Label(self.vtna_registro,text = "Usuario:",font = ("Cambria", 12)).place(x = 25, y = 210)
        self.sv_username = StringVar(self.vtna_registro)
        Entry(self.vtna_registro,textvariable = self.sv_username, width = "33").place(x = 120, y = 215)

        Label(self.vtna_registro,text = "Contraseña:",font = ("Cambria", 12)).place(x = 25, y = 245)
        self.sv_contra = StringVar(self.vtna_registro)
        Entry(self.vtna_registro,textvariable = self.sv_contra, width = "33",  show = "*").place(x = 120, y = 250)
        
        #Botones de ventana registro
        Button(self.vtna_registro,text = "Registrarse", width = "10", height = "2",command=lambda :self.agregar_estudiante()).place(x = 70, y = 290)
        Button(self.vtna_registro,text = "Cancelar", width = "10", height = "2", command=lambda: cerrarVentana(self.vtna_registro)).place(x = 230, y = 290)# No se puede llamar al login otra vez porque da error REVISAR
        
        self.vtna_registro.mainloop()

    def agregar_estudiante(self):  # Se obtiene los datos del estudiante y se manda a la clase Estudiante(Persona) para agregarla a la lista de punteros 
        try:
            p_estudiante=Estudiante(nombre=self.sv_nombre.get(),apellido1=self.sv_apellido1.get(),
                                    apellido2=self.sv_apellido2.get(),carrera=self.sv_carrera.get(),
                                    usuario=self.sv_username.get(),contraseña=self.sv_contra.get())

            #Se agrega el estudiante al archivo estudiantes.txt                    
            Estudiante.guardar_estudiante(p_estudiante)

            #Se limpian las cajas de texto de la ventana registro Estudiante
            self.sv_nombre.set('')
            self.sv_apellido1.set('')
            self.sv_apellido2.set('')
            self.sv_carrera.set('')
            self.sv_username.set('')
            self.sv_contra.set('')

            ocultarVentana(self.vtna_registro)  #Se oculta la ventana de registro 
            
        except: # Si no se logra agregar el estudiante al archivo estudiantes.txt
            showwarning(title="Alerta", message="No se ha pudo agregar el estudiante")
    

class RegistroAdm:

    sv_nombre,sv_apellido1,sv_apellido2,sv_telefono,sv_username,sv_contra=[None,None,None,None,None,None]

    def __init__(self) -> None:
        
        #ventana registro Administrador
        self.vtna_registro=tk.Tk()
        self.vtna_registro.geometry("430x350")
        self.vtna_registro.title("Administrador del Tiempo")
        self.vtna_registro.resizable(False,False)
        self.lb_registro=Label(self.vtna_registro, text = 'Registro de Administrador', font = ("Cambria", 22))
        self.lb_registro.place(x=75,y=20)

        #Texto y entradas  de datos       
        Label(self.vtna_registro,text = "Nombre:",font = ("Cambria", 12)).place(x = 25, y = 70)
        self.sv_nombre = StringVar(self.vtna_registro)
        Entry(self.vtna_registro,textvariable = self.sv_nombre , width = "33").place(x = 120, y = 75)

        Label(self.vtna_registro,text = "1° Apellido:",font = ("Cambria", 12)).place(x = 25, y = 105)
        self.sv_apellido1 = StringVar(self.vtna_registro)
        Entry(self.vtna_registro,textvariable = self.sv_apellido1, width = "33").place(x = 120, y = 110)

        Label(self.vtna_registro,text = "2° Apellido:",font = ("Cambria", 12)).place(x = 25, y = 140)
        self.sv_apellido2 = StringVar(self.vtna_registro)
        Entry(self.vtna_registro,textvariable = self.sv_apellido2, width = "33").place(x = 120, y = 145)
        
        Label(self.vtna_registro,text = "Telefono:",font = ("Cambria", 12)).place(x = 25, y = 175)
        self.sv_telefono = StringVar(self.vtna_registro)
        Entry(self.vtna_registro,textvariable = self.sv_telefono, width = "33").place(x = 120, y = 180)

        Label(self.vtna_registro,text = "Usuario:",font = ("Cambria", 12)).place(x = 25, y = 210)
        self.sv_username = StringVar(self.vtna_registro)
        Entry(self.vtna_registro,textvariable = self.sv_username, width = "33").place(x = 120, y = 215)

        Label(self.vtna_registro,text = "Contraseña:",font = ("Cambria", 12)).place(x = 25, y = 245)
        self.sv_contra = StringVar(self.vtna_registro)
        Entry(self.vtna_registro,textvariable = self.sv_contra, width = "33",  show = "*").place(x = 120, y = 250)

        Button(self.vtna_registro,text = "Guardar", width = "10", height = "2",command=lambda :self.agregar_admin()).place(x = 70, y = 290)
        Button(self.vtna_registro,text = "Cancelar", width = "10", height = "2",command=lambda: cerrarVentana(self.vtna_registro)).place(x = 230, y = 290)# No se puede llamar al login otra vez porque da error REVISAR

        self.vtna_registro.mainloop()

    def agregar_admin(self):  # Se obtiene los datos del administrativo y se manda a la clase Aministrativo(Persona) para agregarla a la lista de punteros 
        try:
            p_admin=Administrativo(nombre=self.sv_nombre.get(),apellido1=self.sv_apellido1.get(),
                                    apellido2=self.sv_apellido2.get(),telefonos=self.sv_telefono.get(),
                                    usuario=self.sv_username.get(),contraseña=self.sv_contra.get())
            Administrativo.guardar_admin(p_admin)

            #Se limpian las cajas de texto de la ventana registro Estudiante
            self.sv_nombre.set('')
            self.sv_apellido1.set('')
            self.sv_apellido2.set('')
            self.sv_telefono.set('')
            self.sv_username.set('')
            self.sv_contra.set('')

            ocultarVentana(self.vtna_registro) #Se oculta la ventana de registro 
            
        except: # Si no se logra agregar el administrativo al archivo administrativos.txt
            showwarning(title="Alerta", message="No se ha pudo agregar el administrativo")


