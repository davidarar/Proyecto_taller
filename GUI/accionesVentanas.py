from tkinter.messagebox import askyesno, showerror, showwarning

def cerrarVentana(v):
    confirmacion = askyesno(title='Confirmación', message='¿Esta seguro de que desae salir de esta ventana?')
    if (confirmacion):
        v.destroy()

def ocultarVentana(v):
    v.withdraw()


def mostrarVentana(v,vp):
    vp.withdraw()
    v.deiconify()
    
def volverVentana(v,vp):
    v.destroy()
    vp.update()
    vp.deiconify()


