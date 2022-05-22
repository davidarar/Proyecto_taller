from tkinter import *
from tkinter import ttk as ttk



def v_menuAdm():
    menu_admin = Tk()
    menu_admin.title("Menu Administrador")
    menu_admin.geometry("450x350")
    menu_admin.resizable(False,False)



    lb_menu=Label(menu_admin, text = 'Menu Aministrador', font = ("Cambria", 24)).place(x=90,y=25)


    btn_cambCarrera = Button(menu_admin, text = "Agregar carrera",font = ("Cambria", 12),width = "15", height = "1")
    btn_cambCarrera.place(x = 150, y = 90)

    btn_matrCurso = Button(menu_admin, text = "Modificar carrera", font = ("Cambria", 12), width = "15", height = "1")
    btn_matrCurso.place(x = 150, y = 140)

    btn_addActividad = Button(menu_admin, text = "Agregar curso",font = ("Cambria", 12),  width = "15", height = "1")
    btn_addActividad.place(x = 150, y = 190)

    btn_showActividad = Button(menu_admin, text = "Modificar curso",font = ("Cambria", 12),  width = "15", height = "1" )
    btn_showActividad.place(x = 150, y = 240)

    btn_cerrar = Button(menu_admin, text = "Cerrar",font = ("Cambria", 12), width = "8", height = "1",)
    btn_cerrar.place(x = 330, y = 280)


    menu_admin.mainloop()