from accionesVentanas import cerrarVentana,ocultarVentana,volverVentana
from tkinter import *
from tkinter import ttk as ttk
from lista_usuarios import Carrera,Estudiante,cargar_lista_estudiantes
from tkinter.messagebox import showwarning, askyesno


# Funcion para cambiar la carrera del Estudiante 
def cambioCar(user_name,n_carrera): 
    try:
        with open("estudiantes.txt","r+") as lector: # Se abre el archivo estudiantes.txt  para leer y encontrar 
            a=lector.read()                          # el usuario que desea cambiar de carrera
            users = [eval(user) for user in a.split("\n")] # Users guarda en una lista la lista de los estudiantes 

            for user in users: # Se recorre la lista de estudiantes, comparando los estudiantes con el estudiante actual 
                if user[4] == user_name: # Si el estudiante es igual al usario actual, en esa lista se cambia la carrera
                    user[3]=n_carrera

        lector.close() # cierra el archivo de estudiantes.txt

        with open("estudiantes.txt","w+") as writer: #Se abre el archivo para escribir el estudiante con la carrera modificada
            cont = 0
            while cont < len(users):    #Con esta condicion se determina como se debe agregar el usario, dependeindo si 
                if cont == len(users)-1:                           #  tiene un salto de linea o no      
                    writer.write(str(users[cont]))
                else:
                    writer.write(users[cont].__str__()+"\n")
                cont += 1
    except: # si no se pudo modificar la carrera se muestra una alerta 
        showwarning(title="Alerta", message="No se ha pudo hacer el cambio de carrera")                     
    finally:
        writer.close() # Se cierra el archivo
        
            


def v_cambiarCarrera(u):

  # Ventana de agregar actividad 
    vtna_carrera = Tk()
    vtna_carrera.title("Menu Estudiante")
    vtna_carrera.geometry("400x200")
    vtna_carrera.resizable(False,False)

    #Texto y entrada de datos 
    Label(vtna_carrera, text = 'Selecione su nueva carrera', font = ("Cambria", 14)).place(x=90,y=25)
    sv_carrera = StringVar(vtna_carrera)
    cbCarrera = ttk.Combobox(vtna_carrera,values=["Computacion",
                                                      "Electronica",
                                                      "Agronomia",
                                                      "Administracion de Empresas"],
                                                      state="readonly",width = "26",font = ("Cambria", 10),textvariable=sv_carrera).place(x = 100, y = 70)
                
    n_carrera=sv_carrera.get()

    
    Button(vtna_carrera,text = "Cambiar", width = "20", height = "2", command=lambda:cambioCar(u,n_carrera)).place(x = 130, y = 110)
    Button(vtna_carrera,text = "Atras", width = "10", height = "2",command=lambda: ocultarVentana(vtna_carrera,)).place(x = 290, y = 150)
    
    vtna_carrera.mainloop()

#--------------------------------------Ventanas sin funciones--------------------------------------------------
def v_matricularCurso(): # Incompleto - No se logró crear las funciones 

    #Ventana de matricular curso
    vtna_carrera = Tk()
    vtna_carrera.title("Menu Estudiante")
    vtna_carrera.geometry("400x200")
    vtna_carrera.resizable(False,False)
    
    #Texto y entrada de datos 
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

def v_agregarActividad(): # Incompleto - No se logró crear las funciones 

    #Ventana de agregar actividad
    vtna_actividad = Tk()
    vtna_actividad.title("Menu Estudiante")
    vtna_actividad.geometry("400x300")
    vtna_actividad.resizable(False, False)
    Label(vtna_actividad, text = 'Agregar actividad', font = ("Cambria", 14)).place(x=90, y=20)

    #Texto y entrada de datos 
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


def v_mostrarActividad(): # Incompleto - No se logró crear las funciones 
 
    #Ventana de mostrar actividad
    vtna_verActividad = Tk()
    vtna_verActividad.title("Menu Estudiante")
    vtna_verActividad.geometry("400x300")
    vtna_verActividad.resizable(False, False)
    Label(vtna_verActividad, text='Lista de Actividades',font=("Cambria", 14)).place(x=100, y=25)

    #Texto y entrada de datos 
    Label(vtna_verActividad, text = 'Fecha a consultar:', font = ("Cambria", 12)).place(x=30,y=65)
    s_fechConsulta= StringVar()
    Entry(textvariable = s_fechConsulta, width = "29").place(x = 165, y = 70)

    sv_actividades = StringVar()
    Entry(textvariable = sv_actividades, width = "29").place(x = 165, y = 100)

    Button(vtna_verActividad,text = "Regresar", width = "10").place(x = 265, y = 235)

