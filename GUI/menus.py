import tkinter as tk
from tkinter import ttk 
from tkinter import Button, Entry, Label, StringVar, Menu
from funcionesAdm import v_addCarrera,RegistroCurso
from funcEstudiantes import v_cambiarCarrera,v_agregarActividad,v_matricularCurso,v_mostrarActividad
from accionesVentanas import cerrarVentana,ocultarVentana



def v_menuEstudiante(user): 
    #Muestra el munu del usario Estudiante 
    menu_estudiante = tk.Tk()
    menu_estudiante.title("Administrador del Tiempo")
    menu_estudiante.geometry("350x320")
    menu_estudiante.resizable(False,False)


    #Texto y botones del menu
    Label(menu_estudiante, text = 'Menu de Estudiante', font = ("Cambria", 24)).place(x=30,y=25)
    Button(menu_estudiante, text = "Cambiar carrera",font = ("Cambria", 14),width = "15", height = "1",command= lambda:v_cambiarCarrera(user)).place(x = 90, y = 90)
    Button(menu_estudiante, text = "Matricular curso", font = ("Cambria", 14), width = "15", height = "1").place(x = 90, y = 140)
    Button(menu_estudiante, text = "Agregar actividad",font = ("Cambria", 14),  width = "15", height = "1").place(x = 90, y = 190)
    Button(menu_estudiante, text = "Mostrar actividad",font = ("Cambria", 14),  width = "15", height = "1",command=lambda: cerrarVentana(v_menuEstudiante) ).place(x = 90, y = 240)
    Button(menu_estudiante, text = "salir",font = ("Cambria", 12), width = "5",command=lambda: cerrarVentana(menu_estudiante)).place(x = 280, y = 270)

    menu_estudiante.mainloop()


def v_menuAdm():
    #Muestra la ventana del usuario Administrativo
    menu_admin = tk.Tk()
    menu_admin.title("Administrador del Tiempo")
    menu_admin.geometry("350x220")
    menu_admin.resizable(False,False)

    #Texto y botones del menu
    Label(menu_admin, text = 'Menu Aministrador', font = ("Cambria", 24)).place(x=30,y=25)
    Button(menu_admin, text = "Agregar carrera",font = ("Cambria", 14),width = "15", height = "1",command=lambda: v_addCarrera()).place(x = 90, y = 90)    
    Button(menu_admin, text = "Agregar curso",font = ("Cambria", 14),  width = "15", height = "1",command=lambda: RegistroCurso()).place(x = 90, y = 140)
    Button(menu_admin, text = "salir",font = ("Cambria", 12), width = "5",command=lambda: cerrarVentana(menu_admin)).place(x = 280, y = 170)


    menu_admin.mainloop()



