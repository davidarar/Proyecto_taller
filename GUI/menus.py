
import tkinter as tk
from tkinter import ttk 
from tkinter import Button, Entry, Label, StringVar, Menu
from funcionesAdm import v_addCarrera,RegistroCurso



def v_menuEstudiante():

    menu_estudiante = tk.Tk()
    menu_estudiante.title("Administrador del Tiempo")
    menu_estudiante.geometry("350x320")
    menu_estudiante.resizable(False,False)

    # Menú del sistema
    barra_menu = Menu(menu_estudiante)
    menu_estudiante.config(menu=barra_menu)


    # primer opción del menú
    menu_archivo = tk.Menu(menu_estudiante, tearoff=1)
    menu_archivo.add_command(label="Guardar")
    menu_archivo.add_checkbutton(label="Autoguardado", onvalue=1, offvalue=0)
    menu_archivo.add_command(label="Salir")

    # Segunda opción del menú
    menu_ayuda= tk.Menu(menu_estudiante, tearoff=1)
    menu_ayuda.add_command(label="Creado por ")

    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

    Label(menu_estudiante, text = 'Menu de Estudiante', font = ("Cambria", 24)).place(x=30,y=25)
    Button(menu_estudiante, text = "Cambiar carrera",font = ("Cambria", 14),width = "15", height = "1").place(x = 90, y = 90)
    Button(menu_estudiante, text = "Matricular curso", font = ("Cambria", 14), width = "15", height = "1").place(x = 90, y = 140)
    Button(menu_estudiante, text = "Agregar actividad",font = ("Cambria", 14),  width = "15", height = "1").place(x = 90, y = 190)
    Button(menu_estudiante, text = "Mostrar actividad",font = ("Cambria", 14),  width = "15", height = "1" ).place(x = 90, y = 240)
    #Button(menu_estudiante, text = "Cerrar",font = ("Cambria", 12), width = "8", height = "1",).place(x = 330, y = 280)

    menu_estudiante.mainloop()

def v_menuAdm():

    
    menu_admin = tk.Tk()
    menu_admin.title("Administrador del Tiempo")
    menu_admin.geometry("350x220")
    menu_admin.resizable(False,False)

    
    # Menú del sistema
    barra_menu = Menu(menu_admin)
    menu_admin.config(menu=barra_menu)


    # primer opción del menú
    menu_archivo = tk.Menu(menu_admin, tearoff=1)
    menu_archivo.add_command(label="Guardar")
    menu_archivo.add_checkbutton(label="Autoguardado", onvalue=1, offvalue=0)
    menu_archivo.add_command(label="Salir")

    # Segunda opción del menú
    menu_ayuda= tk.Menu(menu_admin, tearoff=1)
    menu_ayuda.add_command(label="Creado por ")


    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)


    Label(menu_admin, text = 'Menu Aministrador', font = ("Cambria", 24)).place(x=30,y=25)
    Button(menu_admin, text = "Agregar carrera",font = ("Cambria", 14),width = "15", height = "1",command=lambda: v_addCarrera()).place(x = 90, y = 90)    
    Button(menu_admin, text = "Agregar curso",font = ("Cambria", 14),  width = "15", height = "1",command=lambda: RegistroCurso()).place(x = 90, y = 140)
    #Button(menu_admin, text = "Modificar carrera", font = ("Cambria", 12), width = "15", height = "1").place(x = 150, y = 140)

    #Button(menu_admin, text = "Modificar curso",font = ("Cambria", 12),  width = "15", height = "1" ).place(x = 150, y = 240)   
    #Button(menu_admin, text = "Cerrar",font = ("Cambria", 12), width = "8", height = "1").place(x = 330, y = 280)


    menu_admin.mainloop()


#v_menuAdm()


#v_menuEstudiante()



