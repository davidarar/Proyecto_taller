import tkinter as tk
from tkinter import Button, Entry, Label, StringVar
from tkinter.messagebox import showwarning
from accionesVentanas import volverVentana,cerrarVentana, mostrarVentana,ocultarVentana
from lista_usuarios import cargar_lista_estudiantes,cargar_lista_administrativos
from menus import v_menuEstudiante,v_menuAdm
from registros import RegistroEst,RegistroAdm


class vLogin:
    sv_contrasena,sv_username,vtna,rol,vtna_login=[None,None,None,None,None]
    """l_estudiantes=None
    l_administrativos=None"""
    #l_estudiantes=cargar_lista_estudiantes()
    #l_administrativos= cargar_lista_administrativos

    def __init__(self,vtna,rol) -> None:
        self.l_estudiantes=cargar_lista_estudiantes()
        self.l_administrativos= cargar_lista_administrativos

        self.vtna=vtna
        self.rol=rol
     
        self.vtna.withdraw()
        
        self.vtna_login = tk.Tk()
        self.vtna_login.title("Administrador del Tiempo")
        self.vtna_login.geometry("390x300")
        self.vtna_login.resizable(False,False)
        Label (self.vtna_login, text = 'Iniciar Sesión', font = ("Cambria", 24)).place(x=90,y=25)

        #Texto y entradas usuario
        Label(self.vtna_login,text="Usuario: ",font = ("Cambria", 13)).place(x=70,y=115)
        self.sv_username = StringVar(self.vtna_login)
        Entry (self.vtna_login,textvariable=self.sv_username, width = "25").place(x=150,y=119)

        #Texto y entradas contraseña
        Label(self.vtna_login,text="Contraseña: ",font = ("Cambria", 12)).place(x=50,y=161)
        self.sv_contrasena = StringVar(self.vtna_login)
        Entry(self.vtna_login,textvariable=self.sv_contrasena,width = "25",show="*").place(x=150,y=165)

        Button(self.vtna_login, text = "Iniciar sesión", width = "15",command=lambda : self.validacion()).place(x = 210, y = 215)
        Button(self.vtna_login, text = "Registrarse", width = "15",command= lambda : self.abrirRegistro()).place(x = 60, y = 215) 
        Button(self.vtna_login, text = "Atras", width = "5", command=lambda: self.regresar()).place(x = 335, y = 260) 

        self.vtna_login.mainloop()

    def regresar(self):
        volverVentana(self.vtna_login,self.vtna)


    def abrirRegistro(self):
        if self.rol==0:
            RegistroEst()
        else:
            RegistroAdm()

    def cambiarCarrera(self):
        user=self.sv_username.get()
        psw=self.sv_contrasena.get()

        puntero=self.l_estudiantes
        if puntero==None:
            showwarning (title="Alerta", message="No hay usuarios en en archivo")
        else:
            while puntero!=None:
                if  (puntero.carrera==user and puntero.contraseña==psw):
                    ocultarVentana(self.vtna_login)
                    us=user
                    v_menuEstudiante()
                    break
                else:
                    puntero=puntero.sig


    def validacion(self):
        if self.rol==0:
            self.validar_estudiante()
        else:
            self.validar_admin()

    def validar_admin(self):
        user=self.sv_username.get()
        psw=self.sv_contrasena.get()

        if user=="" and psw=="":
            showwarning (title="Alerta", message="No pueden estan en blanco el nombre de usuario ni la contraseña")
        else:
            punteroAdm=self.l_administrativos
            if punteroAdm==None:
                showwarning (title="Alerta", message="Usuario no válido")
            else:
                valido=False
                while punteroAdm!=None:
                    if (punteroAdm.usuario==user and punteroAdm.contraseña==psw):
                        valido=True
                        ocultarVentana(self.vtna_login)
                        v_menuAdm()
                        break
                    else:
                        punteroAdm=punteroAdm.sig
                if not valido:
                    showwarning (title="Alerta", message="Usuario no válido")


    def validar_estudiante(self):
        user=self.sv_username.get()
        psw=self.sv_contrasena.get()

        if user=="" and psw=="":
            showwarning (title="Alerta", message="No pueden estan en blanco el nombre de usuario ni la contraseña")
        else:
            puntero=self.l_estudiantes
            if puntero==None:
                showwarning (title="Alerta", message="Usuario no válido")
            else:
                valido=False
                while puntero!=None:
                    if (puntero.usuario==user and puntero.contraseña==psw):
                        valido=True
                        ocultarVentana(self.vtna_login)
            
                        v_menuEstudiante()
                        break
                    else:
                        puntero=puntero.sig
                if not valido:
                    showwarning (title="Alerta", message="Usuario no válido")

if __name__ == "__main__":
    pass