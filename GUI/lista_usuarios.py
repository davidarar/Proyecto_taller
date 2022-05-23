from tkinter.messagebox import showerror, showwarning
import pickle
#-----------------------------------------------------------------------clase lista "classe madre"----------------------------------------------------------------------------------------
# las demas clases se heredan de esta 
 
class Lista:
    self=None
    def __init__(self) -> None:
        self.sig = None
        
    # metodo imprimir 
    def imprimir(self):
        print(self)
        if self.sig != None:
            self.sig.imprimir()

    # agregar nuevo curso  

    def insertar (self,nuevo):
        puntero=self
        while (puntero.sig!=None):
            puntero=puntero.sig
        puntero.sig=nuevo

    def obtener(self,posi):
        if posi == 0:
            return self 
    
        if self.sig == None:
            return None
        
        return self.sig.obtener(posi-1)

# ------------------------------------------------------------------classes hija de lista, 'clase cursos'-------------------------------------------------------------------------------------------------
class Cursos(Lista):
    # constructor de la clase
    def __init__(
        self,
        nombre,
        creditos,
        horas_lectivas,
        fecha_de_inicio,
        fecha_de_finalizacion,
        horario_de_clase,
        careras,
    ) -> None:
        super().__init__()
        self.curso = nombre
        self.creditos = creditos
        self.horas_lectivas = horas_lectivas
        self.fecha_de_inicio = fecha_de_inicio
        self.fecha_de_finalizacion = fecha_de_finalizacion
        self.horario_de_clase = horario_de_clase
        self.careras = careras

    def guardar_curso(self):
        puntero=self
        try:
            with open("cursos.txt","ta") as archivo:
                archivo.writelines([puntero.curso,puntero.creditos,puntero.horas_lectivas,puntero.fecha_de_inicio,puntero.fecha_de_finalizacion,puntero.horario_de_clase,puntero.careras].__str__()+"\n")
                while puntero.sig!=None:
                    puntero=puntero.sig
                    archivo.writelines([puntero.curso,puntero.creditos,puntero.horas_lectivas,puntero.fecha_de_inicio,puntero.fecha_de_finalizacion,puntero.horario_de_clase,puntero.careras].__str__()+"\n")
        except FileNotFoundError as error:
            showerror(message='No se pudo agregar el curso al archivo')
        finally:
            archivo.close()  

def cargar_lista_cursos():
    """Carga del archivo de cursos a una lista de instancias cursos"""
    lista_cursos=None
    try:
        with open("estudiantes.txt","tr") as lector:
            a=lector.readline()
            p=eval(a)
            lista_cursos=Cursos(p[0],p[1],p[2],p[3],p[4],p[5])
            p=lector.readline()
            while (p!=""):
                p=eval(p)
                lista_cursos.insertar(Cursos(p[0],p[1],p[2],p[3],p[4],p[5]))
                p=lector.readline()
    except FileNotFoundError as error:
        showwarning(title="Error", message="No se pudo cargar los cursos del archivo")
    finally:
        lector.close()  
    return lista_cursos

# -------------------------------------------------------------------classes hija de lista, 'clase carrera----------------------------------------------------------------------------------------------
class Carrera(Lista):
    # declaramos el contructor
    def __init__(self, nombre) -> None:
        super().__init__()
        self.nombre = nombre



    def guardar_carrera(self):
        puntero=self
        try:
            with open("carreras.txt","ta") as archivo:
                archivo.writelines(puntero.nombre.__str__()+"\n")
                while puntero.sig!=None:
                    puntero=puntero.sig
                    archivo.writelines(puntero.nombre.__str__()+"\n")        
        except FileNotFoundError as error:
            showerror(message='No se pudo agregar la carrera al archivo')
        finally:
            archivo.close()  

def cargar_lista_carrera():
    """Carga del archivo de carreras a una lista de instancias carrera"""
    lista_carreras=None
    try:
        with open("carreras.txt","tr") as lector:
            a=lector.readline()
            p=eval(a)
            lista_carreras=Cursos(p[0])
            p=lector.readline()
            while (p!=""):
                p=eval(p)
                lista_carreras.insertar(Cursos(p[0]))
                p=lector.readline()
    except FileNotFoundError as error:
        showwarning(title="Error", message="No se pudo cargar la lista de carreras")
    finally:
        lector.close()  
    return lista_carreras
# ----------------------------------------------------------classe hija de la clase lista "clase persona" la cual hereda los metodos de la clase lista-------------------------------------------------------
class Persona(Lista):
    def __init__(self, nombre, apellido1, apellido2,usuario,contraseña) -> None:
        super().__init__()
        self.nombre = nombre
        self.primer_apellido = apellido1
        self.segundo_apellido = apellido2
        self.usuario = usuario
        self.contraseña = contraseña


# --------------------------------------------------------------classe hija de la clase persona la cual herela los metodos de la clase lista---------------------------------------------------------------------
class Estudiante(Persona):
    def __init__(self, nombre, apellido1, apellido2, carrera,usuario,contraseña) -> None:
        super().__init__(nombre, apellido1, apellido2,usuario,contraseña)
        self.carrera = carrera

    def guardar_estudiante(self):
        puntero=self
        try:
            with open("estudiantes.txt","ta") as archivo:
                archivo.writelines("\n"+[puntero.nombre,puntero.primer_apellido,puntero.segundo_apellido,puntero.carrera,puntero.usuario,puntero.contraseña].__str__())
                while puntero.sig!=None:
                    puntero=puntero.sig
                    archivo.writelines("\n"+[puntero.nombre,puntero.primer_apellido,puntero.segundo_apellido,puntero.carrera,puntero.usuario,puntero.contraseña].__str__()) 
        except FileNotFoundError as error:
            showerror(message='No se pudo agregar el estudiante a estudiantes.txt')
        finally:
            archivo.close()  

def cargar_lista_estudiantes():
    """Carga del archivo de estudiantes a una lista de instancias persona"""
    lista_personas=None
    try:
        with open("estudiantes.txt","tr") as lector:
            a=lector.readline()
            p=eval(a) 
            lista_personas=Estudiante(p[0],p[1],p[2],p[3],p[4],p[5])
            p=lector.readline()
            while (p!=""):
                p=eval(p)
                lista_personas.insertar(Estudiante(p[0],p[1],p[2],p[3],p[4],p[5]))
                p=lector.readline()
    except FileNotFoundError as error:
        showwarning(title="Error", message="No se pudo cargar la lista de estudiantes de administrativos.txt")
    finally:
        lector.close()   
    return lista_personas


# ----------------------------------------------------------------clase Hija de persona la cual hereda los metodos de la clase lista-----------------------------------------------------------------------

class Administrativo(Persona):
    def __init__(self, nombre, apellido1, apellido2, telefonos,usuario,contraseña) -> None:
        super().__init__(nombre, apellido1, apellido2,usuario,contraseña)
        self.telefonos = telefonos
    
    def guardar_admin(self):
        puntero=self
        try:
            with open("administrativos.txt","tw") as archivo:
                archivo.writelines([puntero.nombre,puntero.primer_apellido,puntero.segundo_apellido,puntero.telefonos,puntero.usuario,puntero.contraseña].__str__()+"\n")
                while puntero.sig!=None:
                    puntero=puntero.sig
                    archivo.writelines([puntero.nombre,puntero.primer_apellido,puntero.segundo_apellido,puntero.telefonos,puntero.usuario,puntero.contraseña].__str__()+"\n") 
        except FileNotFoundError as error:
            showerror(message='No se pudo guardar el administrador en el archivo ')
        finally:
            archivo.close()   


def cargar_lista_administrativos():
    """Carga del archivo de estudiantesa una lista de instancias persona"""
    lista_admin=None
    try:
        with open("administrativos.txt","tr") as lector:
            a=lector.readline()
            p=eval(a)
            lista_admin=Administrativo(p[0],p[1],p[2],p[3],p[4],p[5])
            p=lector.readline()
            while (p!=""):
                p=eval(p)
                lista_admin.insertar(Administrativo(p[0],p[1],p[2],p[3],p[4],p[5]))
                p=lector.readline()
    except FileNotFoundError as error:
        showwarning(title="Error", message="No se pudo cargar la lista de administrativos")
    finally:
        lector.close()   
    return lista_admin