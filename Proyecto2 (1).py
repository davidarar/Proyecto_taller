from utils import cifrar,obtener_calve # Librería que contine funciones que permiten cifrar y ocultar la clave ingresada
from time import sleep # Libreria que contienen la función sleep que permite agregar un retraso en la ejecución de un programa

# Variable global tipo tupla que guarda diccionarios con datos de cada curso
cursos =({'Curso':'Comunicacion Escrita','Créditos': 2 ,'Horas lectivas': 3 ,'Fecha inicio':'07-02-2022','Fecha finalizacion':'03-06-2022','Horario clases':'Lunes/5:05pm-7:45pm','Carreras':['Computacion','Agronomia','Administracion de Empresas']},
        {'Curso':'Quimica Basica 1','Créditos':3 ,'Horas lectivas': 4 ,'Fecha inicio':'07-02-2022','Fecha finalizacion':'03-06-2022','Horario clases':'Martes,Jueves/7:55am-9:40am','Carreras':['Agronomia','Electronica']},
        {'Curso':'Matematica General','Créditos':2 ,'Horas lectivas': 5 ,'Fecha inicio':'07-02-2022','Fecha finalizacion':'03-06-2022','Horario clases':'Miercoles/12:30md-4:05pm','Carreras':['Computacion','Agronomia','Administracion de Empresas','Electronica']})

# Variable global tipo tupla que guarda los nombres de cada carrera
carreras = ('Computacion','Agronomia','Electronica','Administracion de empresas')

# Variable global tipo diccionario que guarda diccionarios con datos de cada usuario estudiante
estudiante = {'kris':{'Nombre':'Kristell','Apellido1':'Salazar','Apellido2':'Garcia','Carrera':'Electronica','Usuario':('kris','81dc9bdb52d04dc20036dbd8313ed055'),}}

# Variable global tipo tupla que guarda diccionarios con datos de cada usuario administrador
administrativo = {'tomy':{'Nombre':'Tomas','Apellido1':'Rodriguez','Apellido2':'Suarez','Telefono':'87895634','Usuario':('tomy','4a7d1ed414474e4033ac29ccb8653d9b')},
                 'tavo':{'Nombre':'Gustavo','Apellido1':'Nuñez','Apellido2':'Amador','Telefono':'60253875','Usuario':('tavo','b56a18e0eacdf51aa2a5306b0f533204')}}

curso_estudiante=() #Almacena los cursos matriculados por el estudiante

# Variable global tipo tupla que guarda diccionarios con datos de cada usuario y su contraseña
usuarios = ({'tomy':'4a7d1ed414474e4033ac29ccb8653d9b',
           'kris':'81dc9bdb52d04dc20036dbd8313ed055',
           'tavo':'b56a18e0eacdf51aa2a5306b0f533204'})

def add_curso():
    """ Función que le permite al usuario administrador agregar un curso y su información.
    """
    global cursos
    temp_cursos=list(cursos)  
    materia = {}
    materia['Curso']= input("\n\tNombre curso: ")
    materia['Créditos']= int(input("\n\tCréditos: "))
    materia['Horas lectivas']= int(input("\n\tHoras lectivas: "))
    materia['Fecha inicio']= input("\n\tFecha de inicio [aaaa/mm/dd]: ")
    materia['Fecha finalización']= input("\n\tFecha de finalización [aaaa/mm/dd]: ")
    materia['Horario clases']= input("\n\tHorario de clases [dia/hora]: ")

    if ("S" == input('\n\tEste curso pertenece a otras carreras (S o N): ').upper()):
        curs_compartido = []
        while True:
            curs_compartido.append(input("\tCarrera a la que pertenece: "))
            if ("N" == input('\tPertenece a más carreras (S o N):').upper()):
                break
        materia['Carrreras']= curs_compartido
    
    temp_cursos.append(materia)
    cursos = tuple(temp_cursos)
    return cursos

def modificar_curso():
    """Función que le permite al usuario administrador editar la información de un curso.
    """
    global cursos
    temp_cursos = list(cursos) # Convierte la tupla de cursos a una lista y la amacena en otra variable temporal

    print(chr(27)+"[2J")
    print('\n\tCursos existentes:')

    for e in temp_cursos: # Muestra todos los cursos disponibles
        print(f'\n\t-> {e["Curso"]}')
    respuesta = input('\n\tIngrese el curso que desea editar: ')
    
    for a in temp_cursos: #Recorre los cursos de la lista y busca el curso que el ususario desea editar
        if respuesta in a['Curso']:
            print("""
                    1) Nombre del curso
                    2) Créditos
                    3) Horas lectivas
                    4) Fecha de inicio
                    5) Fecha de finalización
                    6) Horario de clases
                    7) Carreras a las que pertenece      
                    """)
            opc=int(input('\t¿Qué elemento desea modificar: '))
            
            match opc: # Evalua cual dato del curso quiere editar el usuario y modifica la información
                case 1:
                    a['Curso']= input("\n\tNombre del curso: ")
                case 2:
                    a['Créditos']= int(input("\n\tCréditos: "))
                case 3:
                    a['Horas lectivas']= int(input("\n\tHoras lectivas: "))
                case 4:
                    a['Fecha inicio']= input("\n\tFecha de inicio [aaaa/mm/dd]: ")
                case 5:
                    a['Fecha finalización']= input("\n\tFecha de finalización [aaaa/mm/dd]: ")
                case 6:
                    a['Horario clases']= input("\n\tHorario de clases [dia/hora]: ")
                case 7:
                    curs_compartido = []
                    curs_compartido.append(input("\tCarrera a la que pertenece: "))
                    a['Carrreras']= curs_compartido

    cursos = tuple(temp_cursos) # Devuelve la lista de cursos a una tupla
    return cursos

def add_carrera():
    """ Función que le permite al administrador agregar carreras.
    """
    global carreras  
    temp_carreras = list(carreras) 
    temp_carreras.append(input("\n\tIngrese el nombre de la carerra: " ))

    while True:
        if ("N" == input('\t¿Desea agregar otra carrera? (S o N): ').upper()):
            break
        else:
            add_carrera()
    carreras = tuple(temp_carreras) 
    return(carreras)
    
def modif_carrera():
    """Función que le permite al usuario administrador editar el nombre de una carrera.
    """
    global carreras
    temp_carreras = list(carreras) 

    respuesta = input('Ingrese el nombre del curso que desea modificar')
    if respuesta in temp_carreras:
        temp_carreras.remove(respuesta)
        add_carrera()

def inicio():    
    """ Función que muestra el menú de inicio, el registro de usuarios y el inicio de sesión.
        Se implementó la estructura del algoritmo que creó Francisco Javier para hacer un menú de registros.

        - Muestra y ejecuta las funciones del estudiante
        - Muestra y ejecuta las funciones del administrador 
    """
    # Se llama a las variables globales que almacenaran la información de los usuarios
    global estudiante 
    global administrativo
    global usuarios     
    opc= 0
    global curso_estudiante

    while opc != 3:

        print(chr(27)+"[2J")
        print( """
                |||||||                          |||||||
                ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                        Administrador del tiempo
                ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                |||||||                          |||||||

                1) Registrarse
                2) Iniciar Sesión
                3) Salir 
                
                """)
        opc= int(input('\tIngrese la acción que desea realizar: '))
        
        if opc == 1: # Registro de usuarios

            print(chr(27)+"[2J")
            print( """
                    |||||||                          |||||||
                    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                            Administrador del tiempo
                    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                    |||||||       Registrarse        |||||||                

                    1) Estudiante
                    2) Administrativo
                """)
            opc = int(input("\n\tDigite su ocupación: "))

            if opc == 1: # Datos de persona estudiante
                
                cuenta_estudiante =dict()
                cuenta_estudiante ['Nombre'] = input ("\tNombre: ")
                cuenta_estudiante ['Apellido 1°'] = input ("\tPrimer apellido: ")
                cuenta_estudiante ['Apellido 2°'] = input ("\tSegundo apellido: ")
                cuenta_estudiante ['Carrera'] = input("\tCarrera que cursa: ")

                # Solicita usuario y contraseña
                
                print("\nAutenticación: ")
                user_estudiante = input("\n\n\tNombre de usuario: ")
                contraseña = cifrar(obtener_calve("\tContraseña "))
                tupla_estudiante= (user_estudiante,contraseña)
                cuenta_estudiante ['Cuenta de usuario'] = tupla_estudiante
                usuarios[user_estudiante]=contraseña 
                estudiante[user_estudiante]=cuenta_estudiante #En el diccionario global de estudiantes, se guarda el usuario y su información

            elif opc == 2: # Datos de persona administrativa
                    cuenta_admin = dict()
                    cuenta_admin ['Nombre'] = input ("\tNombre: ")
                    cuenta_admin ['Apellido 1°'] = input ("\tPrimer apellido: ")
                    cuenta_admin ['Apellido 2°'] = input ("\tSegundo apellido: ")
                    if ("S" == input('\t¿Desea agregar telefonos? (S o N):').upper()):
                        lista_telefono = []
                        while True:
                            lista_telefono.append(input("\tNúmero de teléfono: "))
                            if ("N" == input('\t¿Desea agregar más telefonos? (S o N):').upper()):
                                break
                        cuenta_admin['Telefono']=lista_telefono

                    # Solicita usuario y contraseña
                    print ('\nAutenticación: ')
                    user_admin = input ("\n\n\tNombre de usuario: ")
                    contraseña = cifrar(obtener_calve('\tContraseña '))
                    tupla_admin = (user_admin,contraseña)
                    cuenta_admin ['Cuenta de usuario'] = tupla_admin
                    usuarios[user_admin]=contraseña
                    administrativo[user_admin]=cuenta_admin # En el diccionario global de administrativo, se guarda el usuario y su información

        elif opc == 2: # Iniciar sesión
            print(chr(27)+"[2J")
            print( '''
                    |||||||                          |||||||
                    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                            Administrador del tiempo
                    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                    |||||||                          |||||||
                                INICIAR SESIÓN
                 ''')

            user = input('\tEscriba su usuario: ')
            contraseña = cifrar(obtener_calve('\tIngrese su contraseña '))
            if usuarios.get(user) == contraseña: # se comprueba que el usuario y su contraseña estén en el diccionario o supuesta base de datos
                print(f'\nBienvenido {user}')
                opc=3
            else:
                print("\n\tEl usuario o la contraseña son incorrectos")   
                sleep(3)   
        elif opc == 3:
            break
        
    if user in estudiante: # Verifica si el usuario es un estudiante

        while True:
            print(chr(27)+"[2J")
            print( """
                    |||||||                          |||||||
                    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                            Administrador del tiempo
                    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                    |||||||                          |||||||
                                MENÚ PRINCIPAL

                1) Cambiar de carrera  
                2) Matricular curso
                3) Agregar actividades
                4) Mostrar actividades 
                5) Salir
                """) 
            opc = int(input("\n\tDigite la acción que desea realizar: "))

            match opc: 
                case 1: # Cambio carrera
                    print(chr(27)+"[2J")
                    for e in carreras: # Imprime las carreras disponibles
                        print(f'\nCarrera disponible: {e}')

                    opc=input('\nIngrese el nombre de la carrera que desea: ')

                    match opc: # Evalua cual es la carrera que se desea agregar y la incorpora a la información del usuario
                        case 'Computacion': 
                            estudiante[user]['Carrera'] = 'Computacion'
                            print(f"\nSu nueva carrera es {estudiante[user]['Carrera']}")
                            sleep(6)
                        case 'Agronomia':
                            estudiante[user]['Carrera'] = 'Agronomia'
                            print(f"\nSu nueva carrera es {estudiante[user]['Carrera']}")
                            sleep(6)
                        case 'Electronica':
                            estudiante[user]['Carrera'] = 'Electronica'
                            print(f"\nSu nueva carrera es {estudiante[user]['Carrera']}")
                            sleep(6)
                        case 'Administracion de empresas':
                            estudiante[user]['Carrera'] = 'Administracion de Empresas'
                            print(f"\nSu nueva carrera es {estudiante[user]['Carrera']}")
                            sleep(6)

                case 2: # Agregar curso
                    print(chr(27)+"[2J")
                    

                    # Se determina cual es la carrera que tiene el usuario 
                    if 'Computacion' in estudiante[user]['Carrera']: 
                        for e in cursos:  # Se toman los diccionarios con los datos de los cursos 
                            a = e['Carreras'] # Se asigna a la variable "a" la lista de carreras a las cuales pertence el curso
                            if 'Computacion' in a:   # Si la carrera del usuario pertenece a la lista del curso, se muestra la información los cursos
                                print(f'''\nCurso disponible para Computacion: {e["Curso"]}
                                \nCréditos: {e["Créditos"]}
                                \nHoras lectivas: {e["Horas lectivas"]}
                                \nFecha de inicio: {e["Fecha inicio"]}
                                \nFecha de finalización: {e["Fecha finalizacion"]}
                                \nHorario: {e["Horario clases"]}
                                \nCarreras a las que pertenece : {e["Carreras"]}''')
                        tem_curso_estudiante=list(curso_estudiante)
                        tem_curso_estudiante.append(input('\n\nIngrese el nombre del curso que desea matricular: '))
                        curso_estudiante=tuple(tem_curso_estudiante)
                        estudiante[user]['Cursos']=curso_estudiante
                        print(estudiante)
                        sleep(6)

                    elif 'Agronomia' in estudiante[user]['Carrera']: 
                        for e in cursos: 
                            a = e['Carreras']
                            if 'Agronomia' in a:
                                print(f'''\nCurso disponible para Agronomia: {e["Curso"]}
                                \nCréditos: {e["Créditos"]}
                                \nHoras lectivas: {e["Horas lectivas"]}
                                \nFecha de inicio: {e["Fecha inicio"]}
                                \nFecha de finalización: {e["Fecha finalizacion"]}
                                \nHorario: {e["Horario clases"]}
                                \nCarreras a las que pertenece : {e["Carreras"]}''')
                        tem_curso_estudiante=list(curso_estudiante)
                        tem_curso_estudiante.append(input('\n\nIngrese el nombre del curso que desea matricular: '))
                        curso_estudiante=tuple(tem_curso_estudiante)
                        estudiante[user]['Cursos']=curso_estudiante
                        print(estudiante)
                        sleep(6)

                    elif 'Electronica' in estudiante[user]['Carrera']:
                        for e in cursos: 
                            a = e['Carreras']
                            if 'Electronica' in a:
                                print(f'''\nCurso disponible para Electronica: {e["Curso"]}
                                \nCréditos: {e["Créditos"]}
                                \nHoras lectivas: {e["Horas lectivas"]}
                                \nFecha de inicio: {e["Fecha inicio"]}
                                \nFecha de finalización: {e["Fecha finalizacion"]}
                                \nHorario: {e["Horario clases"]}
                                \nCarreras a las que pertenece : {e["Carreras"]}''')
                        tem_curso_estudiante=list(curso_estudiante)
                        tem_curso_estudiante.append(input('\n\nIngrese el nombre del curso que desea matricular: '))
                        curso_estudiante=tuple(tem_curso_estudiante)
                        estudiante[user]['Cursos']=curso_estudiante
                        print(estudiante)
                        sleep(6)

                    elif 'Administracion de Empresas' in estudiante[user]['Carrera']:
                        for e in cursos: 
                            a = e['Carreras']
                            if 'Administracion de Empresas' in a:
                                print(f'''\nCurso disponible para Electronica: {e["Curso"]}
                                \nCréditos: {e["Créditos"]}
                                \nHoras lectivas: {e["Horas lectivas"]}
                                \nFecha de inicio: {e["Fecha inicio"]}
                                \nFecha de finalización: {e["Fecha finalizacion"]}
                                \nHorario: {e["Horario clases"]}
                                \nCarreras a las que pertenece : {e["Carreras"]}''')
                        tem_curso_estudiante=list(curso_estudiante)
                        tem_curso_estudiante.append(input('\n\nIngrese el nombre del curso que desea matricular: '))
                        curso_estudiante=tuple(tem_curso_estudiante)
                        estudiante[user]['Cursos']=curso_estudiante
                        print(estudiante)
                        sleep(6)

                case 3: # Agregar actividades
                    print(chr(27)+"[2J")
                    actividades = {}
                    actividades ['Descripcion'] = input ('\t\nIngresar descripción de la actividad: ')
                    if ("S" == input('\t\n¿Esta actividad pertenece a un curso?(S o N):').upper()):
                        while True:
                            actividades ['Curso asociado'] = input('\t\nNombre del curso al que pertenece: ')
                            break
                    actividades ['Fecha inicio'] = input('\t\nIngrese la fecha de inicio [aaaa/mm/dd]: ')
                    actividades ['Fecha final'] = input('\t\nIngrese la fecha de finalizacion [aaaa/mm/dd]: ')
                    estudiante[user]['Actividades'] = actividades 
                    print(f"\t\nLa actividad agregada es {estudiante[user]['Actividades']}")
                    sleep(6) 

                    
                case 4: # Imprimir actividades/ Esta parte esta incompleta 
                    print(chr(27)+"[2J")
                    consulta_actividad = input('\t\nIngrese la fecha que desea consultar: ')
                    if consulta_actividad in estudiante[user]['Actividades']:
                        print(estudiante[user]['Actividades'])
                        sleep(10)
                    else:
                        print('No tiene ninguna actividad')
                        sleep(10)
                case 5: 
                    break
                                     
    elif user in administrativo: # Verifica si el usuario es un administrador
        while True:
            print(chr(27)+"[2J")
            print( """
                    |||||||                          |||||||
                    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                            Administrador del tiempo
                    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                    |||||||                          |||||||
                                MENÚ PRINCIPAL

                    1) Agregar cursos
                    2) Modificar curso
                    3) Agregar carrera
                    4) Modificar carrera
                    5) Salir
                """)
            opc = int(input("\tDigite la acción que desea realizar: "))

            match opc:
                case 1: # Ejecuta la función de agregar curso
                    add_curso()
                case 2: # Ejecuta la función de modificar curso
                    modificar_curso()
                case 3: # Ejecuta la función de agregar carrera
                    add_carrera()
                case 4: # Ejecuta la función de modificar carrera
                    modif_carrera()
                case 5: # Sale del sistema 
                    break
    
inicio()