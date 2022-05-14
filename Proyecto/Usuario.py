from cursos import Cursos  # importamos el archivo cursos.py

cursos = Cursos(
    "Comunicacion Escrita",
    "2",
    "3",
    "07/02/2022",
    "03/06/2022",
    "Lunes/5:05pm-7:45pm",
    "Computacion, Agronomia, Administracion de Empresas",
)
cursos.insertar(
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
cursos.insertar(
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

def crear_curso():
    global cursos
    nombre = input("Dijite el Nombre del Nuevo Curso: ")
    creditos = input("Dijite los creditos del curso: ")
    horas_lectivas = input("Dijite la cantidad de horas lectivas: ")
    fecha_de_inicio = input("Dijite la fecha de inicio del curso: ")
    fecha_de_finalizacion = input("Dijite la fecha de finalización del curso: ")
    horario_de_clase = input("Dijite el Horario del curso: ")
    careras = input("A cuales carreras Pertenese: ")
    
    curso = Cursos(
        nombre,
        creditos,
        horas_lectivas,
        fecha_de_inicio,
        fecha_de_finalizacion,
        horario_de_clase,
        careras,
    )
    if cursos == None:
        cursos = curso
    else:
        cursos.insertar(curso)


def consultar_cursos():
    global cursos
    if cursos == None:
       print("No hay cursos registrados")
    else:
        cursos.imprimir()  
    
    
def menu_principal():
    while True:
        print("\n\n1) Insertar Nuevo Curso")
        print("2) listar Cursos")
        print("3) Salir")

        respuesta = input("dijite su Opción: ")
        if respuesta == "1":
            crear_curso()
        elif respuesta == "2":
            consultar_cursos()
        elif respuesta == "3":
            break

menu_principal()