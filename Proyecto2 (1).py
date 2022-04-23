# Inicio del sistema 
from utils import cifrar,obtener_calve

cursos =({'Curso':'Comunicacion Escrita','Créditos': 2 ,'Horas lectivas': 3 ,'Fecha de inicio':'07-02-2022','Fecha de finalización':'03-06-2022','Horario de clases':'Lunes/5:05pm-7:45pm','Carreras':['Computacion','Agronomia','Administracion de Empresas']},
         {'Curso':'Quimica Basica 1','Créditos':3 ,'Horas lectivas': 4 ,'Fecha de inicio':'07-02-2022','Fecha de finalización':'03-06-2022','Horario de clases':'Martes,Jueves/7:55am-9:40am','Carreras':['Agronomia','Electronica']},
         {'Curso':'Matematica General','Créditos':2 ,'Horas lectivas': 5 ,'Fecha de inicio':'07-02-2022','Fecha de finalización':'03-06-2022','Horario de clases':'Miercoles/12:30md-4:05pm','Carreras':['Computacion','Agronomia','Administracion de Empresas','Electronica']})

carreras = ('Computacion','Agronomia','Electronica','Administracion de empresas')

estudiante = {'kris':{'Nombre':'Kristell','Apellido1':'Salazar','Apellido2':'Garcia','Carrera':'Electronica','Usuario':('kris','81dc9bdb52d04dc20036dbd8313ed055')}}

administrativo = {'tomy':{'Nombre':'Tomas','Apellido1':'Rodriguez','Apellido2':'Suarez','Carrera':'Computacion','Usuario':('tomy','4a7d1ed414474e4033ac29ccb8653d9b')},
                 'tavo':{'Nombre':'Gustavo','Apellido1':'Nuñez','Apellido2':'Amador','Carrera':'Agronomia','Usuario':('tavo','b56a18e0eacdf51aa2a5306b0f533204')}}

actividades ={}  

usuarios = ({'tomy':'4a7d1ed414474e4033ac29ccb8653d9b',
           'kris':'81dc9bdb52d04dc20036dbd8313ed055',
           'tavo':'b56a18e0eacdf51aa2a5306b0f533204'})


def convertir_tuple_list(a):
    return (list(a))




def add_curso():

    global cursos  

    materia = {}
    materia['Curso']= input("\n\tNombre curso: ")
    materia['Créditos']= int(input("\n\tCréditos: "))
    materia['Horas lectivas']= int(input("\n\tHoras lectivas: "))
    materia['Fecha de inicio']= input("\n\tFecha de inicio: ")
    materia['Fecha de finalización']= input("\n\tFecha de finalización: ")
    materia['Horario de clases']= input("\n\tHorario de clases [dia/hora]: ")

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
                    tupla_admin = (user_admin,contraseña)
                    cuenta_admin ['Cuenta de usuario'] = tupla_admin

                    usuarios[user_admin]=contraseña
                    administrativo.append(cuenta_admin)

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

            user = input('Escriba su usuario: ')
            contraseña = cifrar(obtener_calve('Ingrese su contraseña '))

          
            if usuarios.get(user) == contraseña: #se comprueba que el usuario y su contraseña estén en el diccionario o supuesta base de datos
                print(f'\nBienvenido {user}')
                opc=3
            else:
                print('El usuario o la contraseña son incorrectos')  #no lo ejecuta al usar pass
                
        elif opc == 3:
            break
        
    if user in estudiante:

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
                4) Salir
                """) 
            opc = int(input("\n\tDigite la acción que desea realizar: "))

            match opc: 
                case 1: # Cambio carrera
                    print(chr(27)+"[2J")
                    for e in carreras: #Imprime las carreras disponibles
                        print(f'\nCarrera disponible: {e}')

                    opc=input('\nIngrese el nombre de la carrera que desea: ')

                    match opc:
                        case 'Computacion':
                            estudiante[user]['Carrera'] = 'Computacion'
                            print(estudiante)
                        case 'Agronomia':
                            estudiante[user]['Carrera'] = 'Agronomia'
                            print(estudiante)
                        case 'Electronica':
                            estudiante[user]['Carrera'] = 'Electronica'
                            print(estudiante)
                        case 'Administracion de empresas':
                            estudiante[user]['Carrera'] = 'Administracion de Empresas'
                            print(estudiante)

                case 2: # Agregar curso
                    print(chr(27)+"[2J")

                    if 'Computacion' in estudiante[user]['Carrera']:
                        for e in cursos: 
                            a = e['Carreras']
                            if 'Computacion' in a:   
                                print(f'\nCurso disponible para Computacion: {e["Curso"]}\nCréditos: {e["Créditos"]}\nHoras lectivas: {e["Horas lectivas"]}')
                        respuesta=input('\nIngrese el nombre del curso que desea matricular:')
                        if respuesta in cursos[0]['Curso']:
                            estudiante[user]['Cursos']=respuesta
                            print(estudiante)

                    elif 'Agronomia' in estudiante[user]['Carrera']:
                        for e in cursos: 
                            a = e['Carreras']
                            for b in a:
                                if 'Agronomia' in b:
                                    print(f'\nCurso disponible para Agronomia: {e}')
                            else:
                                pass
                    if 'Electronica' in estudiante[user]['Carrera']:
                        for e in cursos: 
                            a = e['Carreras']
                            for b in a:
                                if 'Electronica' in b:
                                    print(f'\nCurso disponible para Electronica: {e}')
                            else:
                                pass    
                    if 'Administracion de Empresas' in estudiante[user]['Carrera']:
                        for e in cursos: 
                            a = e['Carreras']
                            for b in a:
                                if 'Administracion de Empresas' in b:
                                    print(f'\nCurso disponible para Administracion de Empresas {e}')
                            else:
                                pass

                    opc=input('\nIngrese el nombre de la carrera que desea: ')

                    carrera=input('\nIngrese el número de su carrera ')
                case 3:
                    actividades['Descripcion']

                    
                    

    elif user in administrativo:
        # todo este codigo hay que cambiarlo 
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
                """)
            opc = int(input("\tDigite la acción que desea realizar: "))

            match opc:
                case 1:
                    add_curso()
                case 2:
                    modif_curs()
                case 3:
                    add_carrera()
                case 4:
                    modif_carrera()
    
    estado=user# permite saber cual es el usuario que esta en el sistema
    return user

bienvenida()