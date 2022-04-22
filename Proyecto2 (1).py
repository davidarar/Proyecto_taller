# Inicio del sistema 
from utils import cifrar,obtener_calve

cursos =({'Curso':'Comunicacion Escrita','Créditos': 2 ,'Horas lectivas': 3 ,'Fecha de inicio':'07-02-2022','Fecha de finalización':'03-06-2022','Horario de clases':'Lunes/5:05pm-7:45pm'},
         {'Curso':'Quimica Basica 1','Créditos':3 ,'Horas lectivas': 4 ,'Fecha de inicio':'07-02-2022','Fecha de finalización':'03-06-2022','Horario de clases':'Martes,Jueves/7:55am-9:40am'},
         {'Curso':'Matematica General','Créditos':2 ,'Horas lectivas': 5 ,'Fecha de inicio':'07-02-2022','Fecha de finalización':'03-06-2022','Horario de clases':'Miercoles/12:30md-4:05pm'})

carreras=('Computacion','Agronomia','Electronica','Administracion de empresas')

estudiante = ({'kris':{'Nombre':'Kristell','Apellido1':'Salazar','Apellido2':'Garcia','Carrera':'Electronica','Usuario':('kris','81dc9bdb52d04dc20036dbd8313ed055')}})

administrativo= {'tomy':{'Nombre':'Tomas','Apellido1':'Rodriguez','Apellido2':'Suarez','Carrera':'Computacion','Usuario':('tomy','4a7d1ed414474e4033ac29ccb8653d9b')},
                 'tavo':{'Nombre':'Gustavo','Apellido1':'Nuñez','Apellido2':'Amador','Carrera':'Agronomia','Usuario':('tavo','b56a18e0eacdf51aa2a5306b0f533204')}}
 
usuarios= {'tomy':'4a7d1ed414474e4033ac29ccb8653d9b',
           'kris':'81dc9bdb52d04dc20036dbd8313ed055',
           'tavo':'b56a18e0eacdf51aa2a5306b0f533204'}

estado=''
actividades={} 
 

def convertir_tuple_list(a):
    return (list(a))

def cambiar_carrera():

    convertir_tuple_list(estudiante)

    print(chr(27)+"[2J")

    print('''
                    -------------------------------------------- CARRERAS  ------------------------------------------
                    |             1             |            2            |            3           |              4             |
                    | Ingeniería en Computación | Ingeniería en Agronomía | Ingeniería Electrónica | Administración de Empresas |
        ''')
    opc=input('Ingrese el número de la carrera ')

    match opc:

        case 1:
            for elementos in estudiante:
                if estado in elementos:
                    estudiante['Carrera'] = 'Ingeniería en Computación'
                    print(estudiante)
        case 2:
            for elementos in estudiante:
                if estado in elementos:
                    estudiante['Carrera'] = 'Ingeniería en Agronomía'
                    print(estudiante)
        case 3:
            for elementos in estudiante:
                if estado in elementos:
                    estudiante['Carrera'] = 'Ingeniería Electrónica'
                    print(estudiante)
        case 4:
            for elementos in estudiante:
                if estado in elementos:
                    estudiante['Carrera'] = 'Administración de Empresas'
                    print(estudiante)


def matri_curso():

    print('''
                    -------------------------------------------- CARRERAS  ------------------------------------------
                    |             1             |            2            |            3           |              4             |
                    | Ingeniería en Computación | Ingeniería en Agronomía | Ingeniería Electrónica | Administración de Empresas |
        ''')

    carrera=input('Ingrese el número de su carrera ')

    match carrera:

        case 1:
            for elementos in estudiante:
                if estado in elementos:
                    estudiante['Carrera'] = 'Ingeniería en Computación'
                    print(estudiante)
        case 2:
            for elementos in estudiante:
                if estado in elementos:
                    estudiante['Carrera'] = 'Ingeniería en Agronomía'
                    print(estudiante)
        case 3:
            for elementos in estudiante:
                if estado in elementos:
                    estudiante['Carrera'] = 'Ingeniería Electrónica'
                    print(estudiante)
        case 4:
            for elementos in estudiante:
                if estado in elementos:
                    estudiante['Carrera'] = 'Administración de Empresas'
                    print(estudiante)




#Falta terminar las funciones de actividades

"""def add_actividad():


    name_activid= input('Nombre actividad')
    tipo_actividad = input('Nombre actividad')
    

"""


def add_curso():

    global cursos  

    materia = {}
    materia['Curso']= input("\n\tNombre curso: ")
    materia['Créditos']= int(input("\n\tCréditos: "))
    materia['Horas lectivas']= int(input("\n\tHoras lectivas: "))
    materia['Fecha de inicio']= input("\n\tFecha de inicio: ")
    materia['Fecha de finalización']= input("\n\tFecha de finalización: ")
    materia['Horario de clases']= input("\n\tHorario de clases: ")

    if ("S" == input('\tEste curso pertenece a otras carreras (S o N):').upper()):
        curs_compartido = []
        while True:
            curs_compartido.append(input("\tCarrera a la que pertenece: "))
            if ("N" == input('\tPertenece a otra carrera (S o N):').upper()):
                break
        materia['Carrreras a las que pertenece']= curs_compartido
    
    convertir_tuple_list(cursos)
    cursos.append(materia)
    
    return materia

def modif_curs():

    global cursos

    edit_curs=input('Ingrese el nombre del curso que desea modificar')

    opc=input(''' 
                1)Editar curso
                2)Elmiminar curso

               ¿Qué acción desea realizar?
             ''')
    
    if opc == 1 :
        for e in cursos:
            if edit_curs in e:
                print(True)
       #Falta completar esta parte
           
    elif opc == 2 :
            for e in cursos:
                if edit_curs in e:
                    cursos.remove(e)
    return cursos

####################################################################

def add_carrera():

    global carreras  

    print('''
                 -------------------------------------------- CARRERAS EXISTENTES ------------------------------------------
                |            IC             |           AG            |           IE           |             ADMI           |
                | Ingeniería en Computación | Ingeniería en Agronomía | Ingeniería Electrónica | Administración de Empresas |
         ''')
    
    opc = int(input("\n\tDigite el código carrera que desea agregar: "))

    match opc:
        case 'IC':
            carreras.append('Ingeniería en Computación')
        case 'AG':
            carreras.append('Ingeniería en Agronomía ')
        case 'IE':
            carreras.append('Ingeniería Electrónica')
        case 'ADMI':
            carreras.append('Administración de Empresas')

    while True:
        if ("N" == input('\t¿Desea agregar otra carrera? (S o N):').upper()):
            break
        else:
            add_carrera()
    
def modif_carrera():

    global carreras

    edit_carrera=input('Ingrese el nombre del curso que desea modificar')

    opc=input(''' 
                    1)Editar carrera
                    2)Elmiminar carrera

                ¿Qué acción desea realizar?
                ''')
    if opc == 1 :
        for e in cursos:
            if edit_carrera in e:
                print(True)
        #Falta completar esta parte
            
    elif opc == 2 :
        for e in carreras:
            if edit_carrera in e:
                carreras.remove(e)
    return carreras


def bienvenida():

    global estudiante
    global administrativo
    global usuarios   #diccionario para meter los usuarios con su contraseña     
    opc= 0
    
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
        opc= int(input('''Ingrese la acción que desea realizar: '''))
        
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

            if opc== 1: # Datos de persona estudiante
                
                cuenta_estudiante =dict()
                cuenta_estudiante ['Nombre'] = input ("\tNombre: ")
                cuenta_estudiante ['Apellido 1°'] = input ("\tPrimer apellido: ")
                cuenta_estudiante ['Apellido 2°'] = input ("\tSegundo apellido: ")
                cuenta_estudiante ['Carrera'] = input("\tCarrera que cursa: ")

                #Solicita usuario y contraseña
                print("\nAutenticación: ")
                user_estudiante = input("\n\n\tNombre de usuario: ")
                contraseña = cifrar(obtener_calve("\tContraseña "))
                tupla_estudiante= (user_estudiante,contraseña)
                cuenta_estudiante ['Cuenta de usuario'] = tupla_estudiante
                
                usuarios[user_estudiante]=contraseña

                convertir_tuple_list(estudiante)
                estudiante[user_estudiante]=cuenta_estudiante

            elif opc == 2: # Datos de persona administrativa

                    cuenta_admin =dict()
                    cuenta_admin ['Nombre'] = input ("\tNombre: ")
                    cuenta_admin ['Apellido 1°'] = input ("\tPrimer apellido: ")
                    cuenta_admin ['Apellido 2°'] = input ("\tSegundo apellido: ")
                    
                    if ("S" == input('\tDesea agregar telefonos (S o N):').upper()):
                        lista_telefono = []
                        while True:
                            lista_telefono.append(input("\tNúmero de teléfono: "))
                            if ("N" == input('\tDesea agregar más telefonos (S o N):').upper()):
                                break
                        cuenta_admin['Telefono']=lista_telefono

                    #Solicita usuario y contraseña
                    print ('\nAutenticación: ')
                    user_admin = input ("\n\n\tNombre de usuario: ")
                    contraseña = cifrar(obtener_calve('\tContraseña '))
                    tupla_admin= (user_admin,contraseña)
                    cuenta_admin ['Cuenta de usuario'] = tupla_admin

                    usuarios[user_admin]=contraseña
                    temp_admin = convertir_tuple_list(administrativo)
                    temp_admin[user_admin]=cuenta_admin

        elif opc == 2: #Iniciar sesión
            print(chr(27)+"[2J")
            print( '''
                    |||||||                          |||||||
                    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                            Administrador del tiempo
                    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                    |||||||                          |||||||
                                INICIAR SESIÓN
                 ''')

            user=input('Escriba su usuario: ')
            contraseña = cifrar(obtener_calve('Ingrese su contraseña '))

            if usuarios.get(user) == contraseña: #se comprueba que el usuario y su contraseña estén en el diccionario o supuesta base de datos
                print(f'\nBienvenido {user}')
                break
            else:
                print('El usuario o la contraseña son incorrectos')
        elif opc == 3:
            exit()
        
    
    if user in estudiante:

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
            4) Salir
            """) 
        opc = int(input("\n\tDigite la acción que desea realizar: "))

        match opc:

            case 1:
                cambiar_carrera()
                
            case 2:
                matri_curso()
            case 3:
                add_carrera()
            case 4:
               pass

    elif user in administrativo:
        # todo este codigo hay que cambiarlo 
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

            """)
        opc = int(input("\n\tDigite la acción que desea realizar: "))

        match opc:

            case 1:
                add_curso()
            case 2:
                modif_curs()
            case 3:
                add_carrera()
            case 4:
                modif_carrera()
    
    global estado
    #estado=user

    return user

bienvenida()