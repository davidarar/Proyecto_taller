import tkinter as tk
from tkinter import Button, Entry, Label, StringVar
from tkinter.messagebox import showwarning
from accionesVentanas import volverVentana,cerrarVentana, mostrarVentana,ocultarVentana
from lista_usuarios import cargar_lista_estudiantes,cargar_lista_administrativos
from menus import v_menuEstudiante,v_menuAdm
from registros import RegistroEst,RegistroAdm

#Ventana Login 
class vLogin:
    sv_contrasena,sv_username,vtna,rol,vtna_login=[None,None,None,None,None]

    def __init__(self,vtna,rol) -> None:

        #Se cargan las listas de estudiantes y administrativos para verificar usuarios 
        self.l_estudiantes=cargar_lista_estudiantes()
        self.l_administrativos= cargar_lista_administrativos()

        #Se recibe la ventana que se ocultara al abrir la ventana login 
        #El rol permite diferenciar si es estudiante o administrativo
        self.vtna=vtna
        self.rol=rol
     
        self.vtna.withdraw()
        
        #Ventana Login 
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

        #Botones de ventana login    
        Button(self.vtna_login, text = "Iniciar sesión", width = "15",command=lambda : self.validacion()).place(x = 210, y = 215)
        Button(self.vtna_login, text = "Regisrarse", width = "15",command= lambda : self.abrirRegistro()).place(x = 60, y = 215) 
        Button(self.vtna_login, text = "Atras", width = "5", command=lambda: self.regresar()).place(x = 335, y = 260) 

        self.vtna_login.mainloop()

        #Oculta la ventana Login y regresa a la ventana de ocuapcion 
    def regresar(self):
        volverVentana(self.vtna_login,self.vtna)

        # Se abre el registro dependiendo del rol que tenga el usuario
    def abrirRegistro(self):
        if self.rol==0:         # 0-> Si es estudiante
            RegistroEst()
        else:                   # 1-> Si es administrador
            RegistroAdm()

        
    def validacion(self):
        if self.rol==0:                 # 0-> Si es estudiante, se valida el usuario en el archivo estudintes
            self.validar_estudiante()
        else:                           # 1-> Si es administrador, se valida el usuario en el archivo administrador
            self.validar_admin()

    def validar_admin(self): #Se obtiene el usuario y la contraseña de las entradas de texto
        user=self.sv_username.get()
        psw=self.sv_contrasena.get()

        if user=="" and psw=="": #Si las entradas de texto estan vacias, muestra ventana de alerta
            showwarning (title="Alerta", message="No pueden estan en blanco el nombre de usuario ni la contraseña")
        else:
            punteroAdm=self.l_administrativos
            if punteroAdm==None:  # Si la lista de administradores esta vacia, muestra ventana de alerta
                showwarning (title="Alerta", message="Usuario no válido")
            else:
                valido=False
                while punteroAdm!=None:  # Si en la lista de admistradores hay personas, se recorre toda la lista para comparar el usuario y contraseña
                    if (punteroAdm.usuario==user and punteroAdm.contraseña==psw):  
                        valido=True                                              
                        ocultarVentana(self.vtna_login) # Si el usuario es valido,
                        v_menuAdm() #Se oculta la ventana de login y se abre la ventana del menu administrador 
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
                while puntero!=None:    # Si en la lista de estudiantes hay personas, se recorre toda la lista para comparar el usuario y contraseña
                    if (puntero.usuario==user and puntero.contraseña==psw):
                        valido=True

                        ocultarVentana(self.vtna_login)#Se oculta la ventana de login 
                        v_menuEstudiante(user) # Se muestra la ventana menu de estudiante, a la cual se le manda el usuario actual
                        break
                    else:
                        puntero=puntero.sig
                if not valido:
                    showwarning (title="Alerta", message="Usuario no válido")

