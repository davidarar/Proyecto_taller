from tkinter import *
from tkinter import ttk as ttk


def v_menuEstudiante():
    menu_estudiante = Tk()
    menu_estudiante.title("Menu Estudiante")
    menu_estudiante.geometry("450x350")
    menu_estudiante.resizable(False,False)


    lb_menu=Label(menu_estudiante, text = 'Menu de Estudiante', font = ("Cambria", 24)).place(x=90,y=25)


    btn_Login = Button(menu_estudiante, text = "Cambiar carrera",font = ("Cambria", 12),width = "15", height = "1")
    btn_Login.place(x = 150, y = 90)

    btn_Registro = Button(menu_estudiante, text = "Matricular curso", font = ("Cambria", 12), width = "15", height = "1")
    btn_Registro.place(x = 150, y = 140)

    btn_Login = Button(menu_estudiante, text = "Agregar actividad",font = ("Cambria", 12),  width = "15", height = "1")
    btn_Login.place(x = 150, y = 190)

    btn_Registro = Button(menu_estudiante, text = "Mostrar actividad",font = ("Cambria", 12),  width = "15", height = "1" )
    btn_Registro.place(x = 150, y = 240)

    btn_Registro = Button(menu_estudiante, text = "Cerrar",font = ("Cambria", 12), width = "8", height = "1",)
    btn_Registro.place(x = 330, y = 280)


    menu_estudiante.mainloop()
