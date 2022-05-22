from accionesVentanas import cerrarVentana,ocultarVentana
from logging import root
from tkinter import *
from tkinter import ttk as ttk
from lista_usuarios import Carrera,Estudiante,cargar_lista_estudiantes
from tkinter.messagebox import showwarning, askyesno


lista_estudiantes=cargar_lista_estudiantes


def v_cambiarCarrera():
  
    vtna_carrera = Tk()
    vtna_carrera.title("Menu Estudiante")
    vtna_carrera.geometry("400x200")
    vtna_carrera.resizable(False,False)
    Label(vtna_carrera, text = 'Selecione su nueva carrera', font = ("Cambria", 14)).place(x=90,y=25)
    sv_carrera = StringVar()
    comboCarreras = ttk.Combobox(vtna_carrera,values=["Computacion",
                                                      "Electronica",
                                                      "Agronomia",
                                                      "Administracion de Empresas"],
                    state="readonly",width = "26",font = ("Cambria", 10),textvariable=sv_carrera).place(x = 100, y = 70)#lista_de_carreras.nombre
    Button(vtna_carrera,text = "Cambiar", width = "15", height = "2").place(x = 70, y = 120)
    Button(vtna_carrera,text = "Cancelar", width = "15", height = "2").place(x = 230, y = 120)
    
    vtna_carrera.mainloop()



def v_matricularCurso(): 
    vtna_carrera = Tk()
    vtna_carrera.title("Menu Estudiante")
    vtna_carrera.geometry("400x200")
    vtna_carrera.resizable(False,False)
    
    Label(vtna_carrera, text = 'Los cursos disponibles ', font = ("Cambria", 14)).place(x=90,y=25)
    sv_carrera = StringVar()
    combo = ttk.Combobox(vtna_carrera,values=["Matematicas General",
                                                      "Comucicacion Escrita",
                                                      "Quimica Basica 1",
                                                      "Taller de Programacion"],
                    state="readonly",width = "26",font = ("Cambria", 10),textvariable=sv_carrera).place(x = 100, y = 70)
    Button(vtna_carrera,text = "Matricular", width = "15", height = "2").place(x = 70, y = 120)
    Button(vtna_carrera,text = "Cancelar", width = "15", height = "2").place(x = 230, y = 120)
    
    vtna_carrera.mainloop()

def v_agregarActividad():

    vtna_actividad = Tk()
    vtna_actividad.title("Menu Estudiante")
    vtna_actividad.geometry("400x300")
    vtna_actividad.resizable(False, False)
    Label(vtna_actividad, text = 'Agregar actividad', font = ("Cambria", 14)).place(x=90, y=20)

    Label(vtna_actividad, text='Tipo de actividad: ',font=("Cambria", 12)).place(x=30, y=75)
    sv_actividad = StringVar()
    c_tipoActividad = ttk.Combobox(vtna_actividad, values=["Ocio",
                                                           "Clase",
                                                           "Extraclase"],
                                   state="readonly", width="26", font=("Cambria", 10), textvariable=sv_actividad).place(x=165, y=78)

    Label(vtna_actividad, text='Descripcion: ',font=("Cambria", 12)).place(x=45, y=105)
    s_descrip = StringVar()
    Entry(textvariable=s_descrip, width="33").place(x=165, y=110)

    Label(vtna_actividad, text='Fecha de inicio:', font=("Cambria", 12)).place(x=45, y=135)
    s_fechInicio = StringVar()
    Entry(textvariable=s_fechInicio, width="33").place(x=165, y=140)

    Label(vtna_actividad, text='Fecha de finalizacion:', font=("Cambria", 12)).place(x=30, y=165)
    s_fechFinal = StringVar()
    Entry(textvariable=s_fechFinal, width="29").place(x=185, y=170)

    Button(vtna_actividad, text="Agregar", width="15", height="2").place(x=70, y=230)
    Button(vtna_actividad, text="Cancelar", width="15", height="2").place(x=230, y=230)

    vtna_actividad.mainloop()


def v_mostrarActividad():
    vtna_verActividad = Tk()
    vtna_verActividad.title("Menu Estudiante")
    vtna_verActividad.geometry("400x300")
    vtna_verActividad.resizable(False, False)
    Label(vtna_verActividad, text='Lista de Actividades',font=("Cambria", 14)).place(x=100, y=25)

    Label(vtna_verActividad, text = 'Fecha a consultar:', font = ("Cambria", 12)).place(x=30,y=65)
    s_fechConsulta= StringVar()
    Entry(textvariable = s_fechConsulta, width = "29").place(x = 165, y = 70)

    sv_actividades = StringVar()
    Entry(textvariable = sv_actividades, width = "29").place(x = 165, y = 100)

    Button(vtna_verActividad,text = "Regresar", width = "10").place(x = 265, y = 235)


"""class RegistroActividad:

    sv_nombre,sv_apellido1,sv_apellido2,sv_telefono,sv_username,sv_contra=[None,None,None,None,None,None]

    def __init__(self) -> None:

        self.self.vtna_actividad = Tk()
        self.vtna_actividad.title("Menu Estudiante")
        self.vtna_actividad.geometry("400x300")
        self.vtna_actividad.resizable(False, False)
        Label(self.vtna_actividad, text = 'Agregar actividad', font = ("Cambria", 14)).place(x=90, y=20)

        Label(self.vtna_actividad, text='Tipo de actividad: ',font=("Cambria", 12)).place(x=30, y=75)
        self.sv_actividad = StringVar()
        c_tipoActividad = ttk.Combobox(self.vtna_actividad, values=["Ocio",
                                                            "Clase",
                                                            "Extraclase"],
                                    state="readonly", width="26", font=("Cambria", 10), textvariable=self.sv_actividad).place(x=165, y=78)

        Label(self.vtna_actividad, text='Descripcion: ',font=("Cambria", 12)).place(x=45, y=105)
        self.s_descrip = StringVar()
        e_descrip = Entry(textvariable=self.s_descrip, width="33").place(x=165, y=110)

        Label(self.vtna_actividad, text='Fecha de inicio:',font=("Cambria", 12)).place(x=45, y=135)
        self.s_fechInicio = StringVar()
        e_fechInicio = Entry(textvariable=self.s_fechInicio,width="33").place(x=165, y=140)

        Label(self.vtna_actividad, text='Fecha de finalizacion:',font=("Cambria", 12)).place(x=30, y=165)
        self.s_fechFinal = StringVar()
        e_fechFinal = Entry(textvariable=self.s_fechFinal,width="29").place(x=185, y=170)

        Button(self.vtna_actividad, text="Agregar",width="15", height="2").place(x=70, y=230)
        Button(self.vtna_actividad, text="Cancelar",width="15", height="2").place(x=230, y=230)

        self.vtna_actividad.mainloop()

"""
"""
    def agregar_actividad(self):
        try:
            n_curso=self.sv_nombre.get(),self.sv_apellido1.get(),self.sv_apellido2.get(),self.sv_telefono.get(),self.sv_username.get(),self.sv_contra.get()
            Cursos.(p_admin)

            self.sv_nombre.set('')
            self.sv_apellido1.set('')
            self.sv_apellido2.set('')
            self.sv_telefono.set('')
            self.sv_username.set('')
            self.sv_contra.set('')

            ocultarVentana(self.vtna_registro)
            
        except:
            showwarning(title="Alerta", message="No se ha pudo agregar el administrativo")
"""



#v_cambiarCarrera()
#v_matricularCurso()
#v_agregarActividad()
#v_mostrarActividad()
#v_calendario()
