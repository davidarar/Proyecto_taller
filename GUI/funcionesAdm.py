from os import name
from tkinter import *
from tkinter import ttk as ttk
from lista_usuarios import Carrera,cargar_lista_carrera,Cursos
from tkinter.messagebox import showerror, showwarning, askyesno
from accionesVentanas import cerrarVentana, ocultarVentana, volverVentana
sv_nameCarrera=None


def agregar_carrera(): #Funcion para agregar carrera
    global sv_nameCarrera    

    try:   # Obtiene la carrera ingresada en la ventana de agregar carrera
        n_carrera=Carrera(nombre=sv_nameCarrera.get())
        sv_nameCarrera.set(" ")     # Limpia la entrada de texto de la ventana 
        n_carrera.guardar_carrera() # Agrega la carrera al archivo de carreras.txt

    except: # Si no logra agregar la carrera al archivo muestra una alerta 
        showwarning(title="Alerta", message="No se ha pudo agregar la carrera")


def v_addCarrera():

    global sv_nameCarrera

    #Ventana de agregar carrera 
    v_addCarrera = Tk()
    v_addCarrera.title("Menu Administrador")
    v_addCarrera.geometry("400x180")
    v_addCarrera.resizable(False,False)

    #Textos y entradas de datos 
    Label(v_addCarrera, text = 'Agregue la nueva carrera', font = ("Cambria", 12)).place(x=20,y=25)
    Label(v_addCarrera, text = 'Nombre carrera:', font = ("Cambria", 12)).place(x=20,y=60)
    sv_nameCarrera = StringVar(v_addCarrera)
    Entry(v_addCarrera,textvariable=sv_nameCarrera,width = "37",show="").place(x=147,y=65)

    #Botones de la ventana 
    Button(v_addCarrera,text = "Agregar", width = "8",command= lambda: agregar_carrera()).place(x = 30, y = 110)
    Button(v_addCarrera,text = "Atras", width = "6",command= lambda:  ocultarVentana(v_addCarrera)).place(x = 240, y = 110)
    Button(v_addCarrera,text = "Cancelar", width = "6",command= lambda: cerrarVentana (v_addCarrera)).place(x = 305, y = 110)

    v_addCarrera.mainloop()


class RegistroCurso:

    sv_nameCurso,sv_creditoCurso,sv_horarioClase,sv_fechaInicio,sv_FechaFinal,sv_carreraCurso,sv_horasLectiva= None,None,None,None,None,None,None

    def __init__(self) -> None:

        #Ventana de Agregar Curso
        self.v_addCurso = Tk()
        self.v_addCurso.title("Menu Administrador")
        self.v_addCurso.geometry("400x320")
        self.v_addCurso.resizable(False,False)

        #Texto y entradas de datos 
        Label(self.v_addCurso,text = "Nombre curso:",font = ("Cambria", 12)).place(x = 25, y = 30)
        self.sv_nameCurso = StringVar(self.v_addCurso)
        Entry(self.v_addCurso,textvariable = self.sv_nameCurso, width = "33").place(x = 135, y = 35)

        Label(self.v_addCurso,text = "Creditos:",font = ("Cambria", 12)).place(x = 65, y = 60)
        self.sv_creditoCurso = StringVar(self.v_addCurso)
        Entry(self.v_addCurso,textvariable = self.sv_creditoCurso, width = "33").place(x = 135, y = 65)

        Label(self.v_addCurso,text = "Horas Lectivas:",font = ("Cambria", 12)).place(x = 25, y = 90)
        self.sv_horasLectiva = StringVar(self.v_addCurso)
        Entry(self.v_addCurso,textvariable = self.sv_horasLectiva, width = "33").place(x = 137, y = 95)

        Label(self.v_addCurso,text = "Fecha de inicio:",font = ("Cambria", 12)).place(x = 25, y = 120)
        self.sv_fechaInicio = StringVar(self.v_addCurso)
        Entry(self.v_addCurso,textvariable = self.sv_fechaInicio, width="33").place(x = 137, y = 125)

        Label(self.v_addCurso,text = "Fecha de final:",font = ("Cambria", 12)).place(x = 25, y = 150)
        self.sv_FechaFinal = StringVar(self.v_addCurso)
        Entry(self.v_addCurso,textvariable = self.sv_FechaFinal, width = "33").place(x = 137, y = 155)

        Label(self.v_addCurso,text = "Horario de clase:",font = ("Cambria", 12)).place(x = 25, y = 180)
        self.sv_horarioClase = StringVar(self.v_addCurso)
        Entry(self.v_addCurso,textvariable = self.sv_horarioClase, width = "31").place(x = 150, y = 185)
        
        Label(self.v_addCurso,text = "Pertenece a la carrera:",font = ("Cambria", 12)).place(x = 25, y = 220)
        self.sv_carreraCurso= StringVar(self.v_addCurso)
        c_carreraCurso = ttk.Combobox(self.v_addCurso,values=[
                                                    "Computacion", 
                                                    "Electronica",
                                                    "Agronomia",
                                                    "Administracion de Empresas"],
                                                    state="readonly",width = "23",font = ("Cambria", 9),textvariable=self.sv_carreraCurso).place(x = 187, y = 225)

        # Botones de la ventana 
        Button(self.v_addCurso,text = "Registrarse", width = "15", height = "2",command= lambda: self.agregar_curso() ).place(x = 70, y = 265)
        Button(self.v_addCurso,text = "Cancelar", width = "15", height = "2",command= lambda: cerrarVentana(self.v_addCurso)).place(x = 230, y = 265)

        self.v_addCurso.mainloop()

    def agregar_curso(self): # Funcion agregar curso
        try: # Se obtiene los datos del curso y se manda a la clase Cursos(Lista) para agregarla a la lista de punteros 
            n_curso=Cursos(nombre=self.sv_nameCurso.get(),creditos=self.sv_creditoCurso.get(),
                                    horario_de_clase=self.sv_horarioClase.get(),horas_lectivas=self.sv_horasLectiva.get(),
                                    fecha_de_inicio=self.sv_fechaInicio.get(),fecha_de_finalizacion=self.sv_FechaFinal.get(),careras=self.sv_carreraCurso.get())
            
            #Se agrega el curso al archivo de cursos.txt
            Cursos.guardar_curso(n_curso)

            #Se limpian las entadas de texto    
            self.sv_nameCurso.set('')
            self.sv_creditoCurso.set('')
            self.sv_horasLectiva.set('')
            self.sv_horarioClase.set('')
            self.sv_FechaFinal.set('')
            self.sv_fechaInicio.set('')
            self.sv_carreraCurso.set('')

            ocultarVentana(self.v_addCurso) # Se oculta la ventana de agregar curso
            
        except: #Si no se puede agregar el curso al archivo se muestra una alerta 
            showwarning(title="Alerta", message="No se ha pudo agregar el curso")
