#-----------------------------------------------------------------------clase lista "classe madre"----------------------------------------------------------------------------------------
# las demas clases se heredan de esta 
 
class Lista:
    
    def __init__(self) -> None:
        self.sig = None
        
    # metodo imprimir 
    def imprimir(self):
        print(self)
        if self.sig != None:
            self.sig.imprimir()

    # agregar nuevo curso
    def insertar(self, nuevo):
        if self.sig == None:
            self.sig = nuevo
        else:
            self.sig.insertar(nuevo)
            
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

lista_de_cursos = Cursos(
    "Comunicacion Escrita",
    "2",
    "3",
    "07/02/2022",
    "03/06/2022",
    "Lunes/5:05pm-7:45pm",
    "Computacion, Agronomia, Administracion de Empresas",
)
lista_de_cursos.insertar(
    Cursos(
        "Quimica Basica 1",
        "3",
        "4",
        "07/02/2022",
        "03/06/2022",
        "Martes,Jueves/7:55am-9:40pm",
        "Agronomia, Electronica",
    )
)
lista_de_cursos.insertar(
    Cursos(
        "Matematica General",
        "2",
        "5",
        "07/02/2022",
        "03/06/2022",
        "Miercoles/12:30pm-4:40pm",
        "Computacion, Agronomia, Administracion de Empresas, Electronica",
    )
)
lista_de_cursos.imprimir()
print(lista_de_cursos.obtener(0)) #imprimir un elemento en la posicion espesifica 

# -------------------------------------------------------------------classes hija de lista, 'clase carrera----------------------------------------------------------------------------------------------
class Carrera(Lista):
    # declaramos el contructor
    def __init__(self, nombre) -> None:
        super().__init__()
        self.nombre = nombre


# listas de punteros de la clase carreras
lista_de_carreras = Carrera("Computacion")
lista_de_carreras.insertar(Carrera("Agronomia"))
lista_de_carreras.insertar(Carrera("Electronica"))
lista_de_carreras.insertar(Carrera("Administracion de Empresas"))
lista_de_carreras.imprimir()
print(lista_de_carreras.obtener(0)) #imprimir un elemento en la posicion espesifica

# ----------------------------------------------------------classe hija de la clase lista "clase persona" la cual hereda los metodos de la clase lista-------------------------------------------------------
class Persona(Lista):
    def __init__(self, nombre, apellido1, apellido2) -> None:
        super().__init__()
        self.nombre = nombre
        self.primer_apellido = apellido1
        self.segundo_apellido = apellido2

# --------------------------------------------------------------classe hija de la clase persona la cual herela los metodos de la clase lista---------------------------------------------------------------------
class Estudiante(Persona):
    def __init__(self, nombre, apellido1, apellido2, carrera) -> None:
        super().__init__(nombre, apellido1, apellido2)
        self.carrera = carrera


# lista de punteros de la clase hija Estudiantes
lista_Estudiante = Estudiante("Kristell", "Salazar", "Garcia", "Electronica")
lista_Estudiante.sig = Estudiante("Aaron", "Gonzalez", "Araya", "Computacion")
lista_Estudiante.sig.sig = Estudiante("Kennet", "Araya", "Arias", "Agronomia")

# uso del metodo implementado que es imprimir, que se coloco en la classe madre "persona"
lista_Estudiante.imprimir()
print(lista_Estudiante.obtener(0)) #imprimir un elemento en la posicion espesifica
# ----------------------------------------------------------------clase Hija de persona la cual hereda los metodos de la clase lista-----------------------------------------------------------------------

class Administrativo(Persona):
    def __init__(self, nombre, apellido1, apellido2, telefonos) -> None:
        super().__init__(nombre, apellido1, apellido2)
        self.telefonos = telefonos

# lista de punteros de la clase hija administrativos
lista_administrativos = Administrativo("Tomas", "Rodriguez", "Suarez", "8789-5634")
lista_administrativos.sig = Administrativo("Gustavo", "Nuñez", "Amador", "6025-3875")
lista_administrativos.imprimir()  # uso del metodo implementado que es imprimir, que se coloco en la classe madre "persona"
print(lista_administrativos.obtener(0)) #imprimir un elemento en la posicion espesifica