from json import load, decoder, dump
from time import sleep

data = {
    'alumnos':[],
    'profesores':[]
    
    }

# Clase Profesor
class Profesor:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
# Clase Alumno (los metodos estaran dentro de esta clase)
class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
# Metodo de la interfaz de seleccion 
    def interfaz(self):
        while True:
            print(''' 
                ¿Ingrese una opcion?
                1) agregar datos de un alumno
                2) agregar datos de un Profesor
                3) Mostrar datos
                4) Salir de aplicación\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.ingresar_alumno()
            elif opcion == "2":
               self.ingresar_profesor()
            elif opcion == "3":
                self.mostrar_datos()
            elif opcion == "4":
                break
            else:
                print("\nIntroduciste una opcion incorrecta")
# Metodo para introducir datos de 1 alumno
    def ingresar_alumno(self):
        lista_notas = []
        nombre = input("ingrese nombre del alumno: ")
        cantidad_notas = input("ingrese la cantidad de notas: ")
        cantidad_notas=int(cantidad_notas)
        for i in range(cantidad_notas):
            nota = int(input(f"ingrese nota{i+1}: "))
            lista_notas.append(nota)

        alumno_nuevo = Alumno(nombre, lista_notas)
        datos = {
            "nombre": alumno_nuevo.nombre,
            "notas": alumno_nuevo.notas,
            "nota maxima": max(alumno_nuevo.notas),
            "nota minima": min(alumno_nuevo.notas),
            "promedio": sum(alumno_nuevo.notas)/cantidad_notas
        }
        self.guardar_persona(datos, "alumnos")
# Metodo para introducir datos de 1 profesor
    def ingresar_profesor(self):
        nombre = input("ingrese nombre del profesor: ")
        edad = input("ingrese la edad del profesor: ")
        dni = input("ingrese el dni del profesor: ")
        profesor_nuevo = Profesor(nombre, edad, dni)
        datos = {
            "nombre": profesor_nuevo.nombre,
            "edad": profesor_nuevo.edad,
            "dni": profesor_nuevo.dni
        }
        self.guardar_persona(datos, "profesores")
# Metodo para guardar los datos que se ingresaron de 1 alumno o profesor en los archivos json
    def guardar_persona(self, dato_nuevo, tipo):
        if tipo=="alumnos":
            data["alumnos"].append(dato_nuevo)
            archivo = open("registro_alumnos.json", "w")
            dump(data[tipo], archivo, indent=4)
            archivo.close()
        elif tipo=="profesores":
            data["profesores"].append(dato_nuevo)
            archivo = open("registro_profesores.json", "w")
            dump(data[tipo], archivo, indent=4)
            archivo.close()
        else:
            pass

# Metodo para cargar los archivos json en la variable local
    def cargar_datos(self):
        try:
            archivo = open("registro_alumnos.json", "r")
            data["alumnos"] = load(archivo)
            archivo.close()
            archivo = open("registro_profesores.json", "r")
            data["profesores"] = load(archivo)
            archivo.close()
        except FileNotFoundError:
            print("\n Creando base de datos...")
            sleep(1)
            archivo = open("registro_alumnos.json", "w")
            archivo.close()
            archivo = open("registro_profesores.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print("\nNo hay datos aun")

# Metodo para mostrar datos de los alumnos o profesores
    def mostrar_datos(self):
        print('''
            Que registros desea que se muestre?
            1) Alumnos
            2) Profesores''')
        dato_a_mostrar = input("> ")

        if dato_a_mostrar =="1":
            for alumno in data["alumnos"]:
                print(" ")
                for key in alumno:
                    print(key,":",alumno[key])

        elif dato_a_mostrar =="2":
            for profesor in data["profesores"]:
                print(" ")
                for key in profesor:
                    print(key,":",profesor[key])
        else:
            print("ingreso una opcion incorrecta")


# Clase principal para correr el programa
class Start(Alumno, Profesor):
    def __init__(self):
        try:
            self.cargar_datos()
            self.interfaz()
        except KeyboardInterrupt:
            print('\nAplicacion interrumpida')

Start()


