from tkinter import ttk as ttk
from tkinter import * 
from tkinter.messagebox import showwarning, askyesno
from accionesVentanas import cerrarVentana
from vLogin import vLogin

#-------------------------------------Ventana principal del Programa -----------------------------------------------------------------------

vtna_principal = Tk() 
vtna_principal.geometry("400x300")
vtna_principal.title("Administrador del Tiempo")
vtna_principal.resizable(False,False)

lb_ocupacion = Label(vtna_principal,text = "¿Cómo desea iniciar sesión?",font = ("Cambria", 18)).place(x = 70, y = 50)

btn_estudiante = Button(vtna_principal, text = "Estudiante",font = ("Cambria", 12),  width = "20", height = "2",command=lambda: vLogin(vtna_principal,0)).place(x = 97, y = 110)
btn_administrador = Button(vtna_principal, text = "Administrador",font = ("Cambria", 12), width = "20", height = "2",command=lambda: vLogin(vtna_principal,1)).place(x = 97, y = 180) 
btn_salir = Button(vtna_principal, text = "Salir",font = ("Cambria", 10), width = "5", command=lambda: cerrarVentana(vtna_principal)).place(x = 320, y = 250) 

vtna_principal.mainloop()






