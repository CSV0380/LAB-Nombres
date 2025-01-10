from collections import namedtuple
import csv
from matplotlib import pyplot as plt
from collections import Counter # brand new 😎😎😎
from collections import defaultdict # brand new 😎😎😎
from matplotlib import pyplot as plt

FrecuenciaNombres = namedtuple("FrecuenciaNombres", "año, nombre, frecuencia, genero")


#APARTADO 1
def leer_frecuencias_nombres(ruta):
    res = []
    with open(ruta, encoding = "utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for año, nombre, frecuencia, genero in lector:
            año = int(año)
            nombre = str(nombre)
            frecuencia = int(frecuencia)
            genero = str(genero)
            res.append(FrecuenciaNombres(año, nombre, frecuencia, genero))
    return res


#APARTADO 2
def filtrar_por_genero(lista, genero):
    res = []
    for nombre in lista:
        if genero == nombre.genero:
            res.append(nombre)
    return res


#APARTADO 3
def calcular_nombres(lista, genero = None): # si es None hay que darle el valor default en los parámetos 🤑🤑
    res = set()
    for persona in lista:
        if genero is None or persona.genero == genero:
            res.add(persona.nombre)
    return sorted(res)


#APARTADO 4
def calcular_top_nombres_de_año(lista, año, numero_lim = 10, genero = None):
    numero_lim = int(numero_lim)
    res = []
    for persona in lista:
        if (genero is None or persona.genero == genero) and persona.año == año:
            res.append((persona.nombre, persona.frecuencia))

    res.sort(key = lambda x: x[1], reverse = True)  # creamos una key para ordenarlo como queremos, en este caso nos fijamos en el 
    return res[:numero_lim]                         #segundo elemento que es la frecuencia, y lo invertimos para que sea de mayor a menor
                                                    # y tambien le ponemos que termine en el numero limite


#APARTADO 5
def calcular_nombres_ambos_generos(lista):
    res = set()
    for personas in lista:
        res.add(personas.nombre)
    return sorted(res)


#APARTADO 6
def calcular_nombres_compuestos(lista, genero = None):
    res = set()
    for personas in lista:
        if ((len(personas.nombre.split()) > 1)) and (personas.genero == genero or genero is None): # genero is None sirve para añadir todos // y el nombre split sirve para dividir las palabras
            res.add(personas.nombre)
    return sorted(res)


#APARTADO 7
def calcular_frecuencia_media_nombre_años(lista, nombre, año_in, año_fin):
    frecuencias = []
    nombre = nombre.upper() # esto es la clave 🔑🔑🔑🗝️🗝️🔐🔧🛠️ para que funcione, yya que el csv estan los nombres en mayúsculas
    for persona in lista:
        if año_in <= persona.año < año_fin and persona.nombre == nombre:
            frecuencias.append(persona.frecuencia)
    
    if len(frecuencias) == 0: # si no se puede calcular la media devuelve 0
        return 0
    
    return sum(frecuencias) / len(frecuencias)


#APARTADO 8
def calcular_nombre_mas_frecuente_año_genero(lista, año, genero):
    res = []
    for persona in lista:
        if persona.año == año and persona.genero == genero:
            res.append((persona.nombre, persona.frecuencia)) #lo hacemos tupla para mirar la frecuencia
    if res: # lo ponemos para que en caso de que no haya nada returneé None
        nombre = max(res, key = lambda x: x[1]) #esto es importante ⏰⏰⏰ hay que implementar el counter
        return nombre
    else:
        return None


#APARTADO 9
def calcular_año_mas_frecuencia_nombre(lista, nombre):
    res = []
    nombre = nombre.upper()
    for persona in lista:
        if persona.nombre == nombre:
            res.append((persona.frecuencia, persona.año)) 
    if res: 
        año = max(res, key = lambda x: x[0]) 
        return año[1]
    else:
        return None


#APARTADO 10 (Se complica)
def calcular_nombres_mas_frecuentes(lista, genero, decada, numero = 5):
    res = []
    inicio_decada = decada
    fin_decada = decada + 9
    for persona in lista:
        if inicio_decada <= persona.año <= fin_decada and persona.genero == genero:
            res.append(persona.nombre)
    
    nombre_frecuencia = Counter(res) # cuenta la frecuencia de las veces que aparece los nombres
    nombres_ordenados = sorted(nombre_frecuencia.items(), key = lambda x: x[1], reverse = True) # para ordenarlos de mayor a menor 💀💀💀☠️☠️☠️ 
    return nombres_ordenados[:numero]


#APARTADO 11
def calcular_año_frecuencia_por_nombre(lista, genero):
    res = defaultdict(list) #crea un diccionario cuyos valores por defecto son las listas
    for persona in lista:
        if persona.genero == genero:
            res[persona.nombre].append((persona.año, persona.frecuencia)) #lo primero crea una clave en diccionario y luego le da los valores años y frecuencia
    return dict(res) #lo convertimos a un diccionario normal


#APARTADO 12 (dificil de hacer 2 bucles, uno para añadir todas las personas; y otro para elegir dentro de todas esas personas, el mas frecuente de cada año)
def calcular_nombre_mas_frecuente_por_año(lista, genero):
    res = defaultdict(list)
    for persona in lista:
        if persona.genero == genero:
            res[persona.año].append((persona.nombre, persona.frecuencia)) #si te piden que le des tres cosas, hacemos de clave el año y dejamos las otras dos como tuplas

    resultado = []
    for año, nombres in res.items(): #no se como funciona el .items()
        #Obtener el nombre con la mayor frecuencia en cada año
        nombre_frecuente = max(nombres, key=lambda x: x[1])
        resultado.append((año, nombre_frecuente[0], nombre_frecuente[1]))

    return sorted(resultado, key=lambda x: x[0]) #ordenarlo por años


#APARTADO 13 (raro)
def calcular_frecuencia_por_año(lista, nombre):
    res = defaultdict(int) # Crear un diccionario donde las claves son los años y los valores son las frecuencias; usamos defaultdict para sumar las frecuencias automáticamente
    nombre = nombre.upper()
    for persona in lista:
        if persona.nombre == nombre:
            res[persona.año] += persona.frecuencia #sumamos las frecuencias
    return sorted(res.items(), key = lambda x: x[0]) #convertimos el diccionario a una lista de tuplas (año, frecuencia) y ordenarlo por año


#APARTADO 14
def mostrar_evolucion_por_año(lista, nombre):
    frecuencias_por_año  = calcular_frecuencia_por_año(lista, nombre)
    años = []
    for i in frecuencias_por_año:
        años.append(i[0])
    frecuencias = []
    for i in frecuencias_por_año:
        frecuencias.append(i[1])

    plt.plot(años, frecuencias)
    plt.title(f"Evolución del nombre '{nombre}'")
    plt.show()



#APARTADO 15
def calcular_frecuencias_por_nombre(lista):
    res = defaultdict(int)
    for persona in lista:
        res[persona.nombre] += persona.frecuencia #a la clave nombre le das el valor frecuencia
    return dict(res)


#APARTADO 16 (rebuscado)
def mostrar_frecuencias_nombres(lista, numero = 10):
    nombres_y_frecuencias = calcular_frecuencias_por_nombre(lista)

    #ordenar por frecuencia en orden descendente y tomar los 'numero' más comunes
    nombres_mas_comunes = sorted(nombres_y_frecuencias.items(), key=lambda x: x[1], reverse=True)[:numero] #los ordena segun la frecuencia y de mayor a menor
    nombres, frecuencias = zip(*nombres_mas_comunes) #el * lo que hace es separarlos en dos listas en lugar de unirlos

    plt.bar(nombres, frecuencias)
    plt.xticks(rotation=80)
    plt.title(f"Frecuencia de los {numero} nombres más comunes")
    plt.show()


#TEST
if __name__ == "__main__":
    datos = leer_frecuencias_nombres("data\\frecuencias_nombres.csv") #daba fallos de lectura leer esta direccion porque tenia \f y eso es un comando default, por lo tanto hay tres soluciones poner \\f ó /f ó (r"data\frecuencias_nombres.csv")
    
    #print(f"{filtrar_por_genero(datos, "Hombre")}")

    #print(f"{calcular_nombres(datos, "Mujer")}")

    #print(f"{calcular_top_nombres_de_año(datos, 2002, 10, "Mujer")}") # ¿Cómo sería si no le pongo ningun valor al numero_lim? 🕵️🕵️🕵️🕵️

    #print(f"{calcular_nombres_ambos_generos(datos)}")

    #print(f"{calcular_nombres_compuestos(datos)}")

    #print(f"{calcular_frecuencia_media_nombre_años(datos, "Juan", 2002, 2012)}")

    #print(f"{calcular_nombre_mas_frecuente_año_genero(datos, 2002, "Hombre")}")

    #print(f"{calcular_año_mas_frecuencia_nombre(datos, "Ana")}")

    #print(f"{calcular_nombres_mas_frecuentes(datos, "Hombre", 2010)}")

    #print(f"{calcular_año_frecuencia_por_nombre(datos, "Hombre")}")

    #print(f"{calcular_nombre_mas_frecuente_por_año(datos, "Hombre")}")

    #print(f"{calcular_frecuencia_por_año(datos, "Juan")}")

    #mostrar_evolucion_por_año(datos, "Iker")

    #print(f"{calcular_frecuencias_por_nombre(datos)}")

    mostrar_frecuencias_nombres(datos, 20)
