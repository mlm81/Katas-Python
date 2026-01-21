# Ejercicio 1: Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def contar_frecuencias(cadena):
    frecuencias = {}
    for letra in cadena.replace(" ", ""): 
        letra = letra.lower() 
        if letra in frecuencias:
            frecuencias[letra] += 1
    else:
        frecuencias[letra] = 1
    return frecuencias

# Ejemplo
texto = "Mi primera kata python"
resultado = contar_frecuencias(texto)
print(resultado)



# Ejercicio 2: Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

numeros = [1,2,3,4,5]
valores_dobles = list(map(lambda x : x*2,numeros))
print(list(valores_dobles))



# Ejercicio 3: Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def buscar_palabras(lista_palabras, palabra_objetivo):
    resultado = []
    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            resultado.append(palabra)
    return resultado

# Ejemplo:

palabras = ["camello", "flor", "melón", "casa", "mermelada","tomillo"]
palabra_objetivo = "me"

print(buscar_palabras(palabras, palabra_objetivo))



#Ejercicio 4:  Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencias (lista_numeros1, lista_numeros2):
    return list(map(lambda x, y: x - y, lista_numeros1, lista_numeros2))
    
# Ejemplo

lista_numeros1 = [5, 14,22, 35]
lista_numeros2 = [3,10,15,20]
print(diferencias (lista_numeros1, lista_numeros2))



# Ejercicio 5: Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def estado_nota (lista_parametros, valor_nota_aprobado=5):
    nota_media = sum(lista_parametros) / len(lista_parametros)
    if nota_media >= valor_nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return (nota_media, estado)

# Ejemplo

lista_notas = [6,4,5,3]
resultado = estado_nota (lista_notas)
print(resultado)



# Ejercicio 6: Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo:

print(factorial(8))


# Ejercicio 7: Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda x: str(x), lista_tuplas))

# Ejemplo
tuplas = [("25", "50"), ("75" , "false")]
resultado = tuplas_a_strings(tuplas)
print(resultado)



# Ejercicio 8:  Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

try:
    numero1_usuario = int(input("Dime un número"))
    numero2_usuario = int(input("Dime otro número"))
    resultado = numero1_usuario / numero2_usuario
    
except    ValueError:
    print("Por favor, ingrese un número válido")
    exito = False

except ZeroDivisionError:
    print ("El número 2 no puede ser O")
    exito = False

else:
    print(f"La división pudo realizarse y el resultado es: {round(resultado, 2)}")
    exito = True
    
finally:
    if not exito:
        print("La división no pudo realizarse")



# Ejercicio 9: Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def filtrar_mascotas_permitidas(lista_mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))

# Ejemplo
mascotas = ["Perro", "Gato", "Mapache", "Tigre", "Hámster","Loro","Camello", "Serpiente Pitón","Conejo","Cocodrilo","Hurón","Oso"]
resultado = filtrar_mascotas_permitidas(mascotas)
print(resultado)



# Ejercicio 10: Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.


class ListaVaciaError(Exception):
    pass

def calcular_promedio(lista):
    if len(lista) == 0:            
        raise ListaVaciaError("La lista está vacía.")
    
    return sum(lista) / len(lista)


# Ejemplo

try:
    numeros = []
    promedio = calcular_promedio(numeros)
    print("El promedio es:", promedio)

except ListaVaciaError as e:
    print("Por favor, introduce datos", e)



# Ejercicio 11:  Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente.

try:
    edad = int(input("Por favor, introduce tu edad"))
    
    if edad < 0 or edad >120:
        raise ValueError ("Tu edad está fuera del rango")
    
except    ValueError:
    print("Por favor, ingrese un número válido")

else:
    print(f"La edad introducida es válida: {edad}")



# Ejercicio 12: Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitudes_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

# Ejemplo

print(longitudes_palabras("hola mundo cómo vas"))



# Ejercicio 13: Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def mayus_minus_unicas(caracteres):
    vistos = []
    for c in caracteres:
        if c not in vistos:
            vistos.append(c) 

    return list(map(lambda c: (c.upper(), c.lower()), vistos))

# Ejemplo:

resultado = mayus_minus_unicas("aAdDiIpP")
print(resultado)



# Ejercicio 14: Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def palabras_con_letra(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))

# Ejemplo:
palabras = ["hola", "mundo", "mi", "nombre", "es", "maria"]
print (palabras_con_letra(palabras,"m"))



# Ejercicio 15: Crea una función lambda que  sume 3 a cada número de una lista dada.

numero_mas_tres = list(map(lambda numero : numero+3, numeros))

# Ejemplo

numeros =[1,2,3,4,5]
print(numero_mas_tres)



# Ejercicio 16: Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_mas_largas(cadena, n):
    palabras = cadena.split()  
    return list(filter(lambda x: len(x) > n, palabras))

# Ejemplo

texto = "Cada día aprendo más Python"
print(palabras_mas_largas(texto, 3))



# Ejercicio 17: Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def digitos_a_numero(lista_digitos):
    return reduce(lambda x, y: x * 10 + y, lista_digitos)

# Ejemplo

print(digitos_a_numero([5, 7, 2]))



# Ejercicio 18:  Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

estudiantes = [
    {"Nombre":"Maria","Edad":"21","Calificacion":68},
    {"Nombre":"Juan","Edad":"25","Calificacion":85},
    {"Nombre":"Pepe","Edad":"24","Calificacion":91},
    {"Nombre":"Jose","Edad":"23","Calificacion":100},
    {"Nombre":"Paco","Edad":"22","Calificacion":90}
]
    
estudiantes_sobresaliente = list(filter(lambda estudiante: estudiante["Calificacion"] >= 90, estudiantes))
print(estudiantes_sobresaliente)
    


# Ejercicio 19: Crea una función lambda que filtre los números impares de una lista dada.

numeros =[1,2,3,4,5,6]
numeros_impares = filter(lambda numeros : numeros%2 != 0, numeros)
print (list(numeros_impares))



# Ejercicio 20: Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

elementos = ["valor", 66, "true", "marciano", 33]
elementos_numeros = filter(lambda elemento : type(elemento) == int , elementos)
print(list(elementos_numeros))



# Ejercicio 21: Crea una función que calcule el cubo de un número dado mediante una función lambda

numero_al_cubo = lambda numero : numero ** 3

# Ejemplo

numero1 = 5
print(f"el numero1 es {numero_al_cubo(numero1)}")



# Ejercicio 22:Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()

from functools import reduce

def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)

# Ejemplo

numeros = [5, 8, 2, 9]
print(producto_total(numeros)) 



# Ejercicio 23: Concatena una lista de palabras.Usa la función reduce()

from functools import reduce

def concatenar_palabras(lista):
    return reduce(lambda x, y: x + y, lista)

# Ejemplo

palabras = ["Buenos", " ", "días", "!"]
print(concatenar_palabras(palabras))



# Ejercicio 24: Calcula la diferencia total en los valores de una lista. Usa la función reduce()

from functools import reduce

def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)

# Ejemplo:

numeros = [10, 21, 17]
print(diferencia_total(numeros))



# Ejercicio 25: Crea una función que cuente el número de caracteres en una cadena de texto dada

cadena = "hola Mundo"
print(f"La longitud de nuestra cadena es: {len(cadena)}")



# Ejercio 26: Crea una función lambda que calcule el resto de la división entre dos números dados

resto_division = lambda a , b : a % b

# Ejemplo

numero_1 = 26
numero_2 = 5
print(resto_division (numero_1, numero_2))



# Ejercicio 27: Crea una función que calcule el promedio de una lista de números.

def promedio_lista (lista_numeros):
    promedio = sum(lista_numeros)/len(lista_numeros)
    return promedio

#Ejemplo

datos =[5,25,35,4]
resultado = promedio_lista (datos)
print (f"El promedio de la lista es :{resultado}")



# Ejercicio 28:Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None  

# Ejemplo

print(primer_duplicado([3, 5, 2, 3, 8, 5]))   
         


# Ejercicio 29: Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro.

def enmascarar(variable):
    texto = str(variable)          
    if len(texto) <= 4:            
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]

# Ejemplo

print(enmascarar(123456789))      



# Ejercicio 30: Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo

print(son_anagramas("monja", "jamon"))
print(son_anagramas("roma", "amor"))
print(son_anagramas ("hielo", "cielo"))



# Ejercicio 31: Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre_en_lista():
    try:
        nombres_input = input("Ingresa una lista de nombres separados por comas: ")
        lista_nombres = [nombre.strip() for nombre in nombres_input.split(",")]
        nombre_buscar = input("Ingresa el nombre que deseas buscar: ").strip()
        if nombre_buscar in lista_nombres:
            print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
        else:
            raise ValueError(f"El nombre '{nombre_buscar}' no se encuentra en la lista.")

    except ValueError as e:
        print(f"Error: {e}")

# Ejemplo
buscar_nombre_en_lista()



# Ejercicio 32: Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_puesto_empleado(nombre_completo, lista_empleados):
    for nombre, puesto in lista_empleados:
        if nombre.lower() == nombre_completo.lower():
            return f"{nombre_completo} trabaja como {puesto}"
    return f"{nombre_completo} no trabaja aquí"

# Ejemplo

empleados = [
    ("Carlos Perez", "Analista"),
    ("Maria Ruiz", "Gerente"),
    ("Marcos Perez", "Contable"),
    ("Juan Gonzalez", "Supervisor")
]

nombre = input("Introduce el nombre completo del empleado: ")
resultado = buscar_puesto_empleado(nombre, empleados)
print(resultado)



# Ejercicio 33: Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

# Ejemplo

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

resultado = sumar_listas(lista_a, lista_b)
print(resultado)



# Ejercicio 34: Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
#Código a seguir:
    #1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
    #2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
    #3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
    #4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
    #5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
    #6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
#Caso de uso:
    #1. Crear un árbol.
    #2. Hacer crecer el tronco del árbol una unidad.
    #3. Añadir una nueva rama al árbol.
    #4. Hacer crecer todas las ramas del árbol una unidad.
    #5. Añadir dos nuevas ramas al árbol.
    #6. Retirar la rama situada en la posición 2.
    #7. Obtener información sobre el árbol.
    
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []
    def crecer_tronco (self):
        self.tronco += 1
    def nueva_rama (self):
        self.ramas.append(1)
    def crecer_ramas (self):
        self.ramas = [rama + 1 for rama in self.ramas]
    def quitar_rama (self, posicion):
        if 0<= posicion < len(self.ramas): 
            del self.ramas [posicion]
        else:
            print ("esa posición no se puede quitar")
    def info_arbol (self):
        return {
            "tamaño_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "tamaño_ramas": self.ramas
        }
    
# Ejemplo

arbol =Arbol ()
arbol.crecer_tronco ()
arbol.nueva_rama ()
arbol.crecer_ramas ()
arbol.nueva_rama ()
arbol.nueva_rama ()
arbol.quitar_rama (2)
info = arbol.info_arbol()
print(f"Información del árbol: {info}")
    
        

# Ejercicio 36: Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
#Código a seguir:
    # 1 Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
    # 2 Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
    # 3 Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
    # 4 Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
#Caso de uso:
    # 1 Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
    # 2 Agregar 20 unidades de saldo de "Bob".
    # 3 Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
    # 4 Retirar 50 unidades de saldo a "Alicia".
    
    
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    def retirar_dinero (self, cantidad):
        if not self.cuenta_corriente:
            print("No se puede retirar dinero porque no tiene cuenta bancaria")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no puedes retirar tanta {cantidad}.")
        self.saldo -= cantidad
    def transferir_dinero(self, otro_usuario, cantidad):
        if not otro_usuario:
            raise ValueError(f"Uno de los usuarios no tiene cuenta corriente")
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

  
# Ejemplo  

Usuario1 = UsuarioBanco("Alicia", 100, True)
Usuario2 = UsuarioBanco("Bob", 50, True)
Usuario2.agregar_dinero(20)
Usuario1.transferir_dinero("Bob", 80)
Usuario1.retirar_dinero(50)


        
# Ejercicio 37: Crea una función llamada procesar_texto que procesa un texto según la opción especificada: reemplazar_palabras , procesar_texto .contar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función 
#Código a seguir:
    # 1 Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
    # 2 Crear una función reemplazar_palabras para remplazar una que devolver el texto con el remplazo de palabras.
    # 3 Crear una función palabra_original del texto por una palabra_nueva . Tiene eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
    # 4 Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
#Caso de uso:
    # Comprueba el funcionamiento completo de la función procesar_texto
    
def contar_palabras (texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in conteo:
            conteo[palabra] +=1
        else:
            conteo [palabra] = 1
    return conteo

def reemplazar_palabras (texto, palabra_original, palabra_nueva):
    return texto.replace (palabra_original, palabra_nueva)

def eliminar_palabras (texto, palabra):
    palabras = texto.split()
    palabras = [p for p in palabras if p != palabra]
    return " ".join(palabras)

def procesar_texto (texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras (texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError ("tienes que dar la palabra que quieres reemplazar y la palabra nueva")
        return reemplazar_palabras (texto, args[0], args [1] )
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError ("tienes que decir la palabra que quieres eliminar")
        return eliminar_palabras (texto, args[0])
    else:
        raise ValueError ("tienes que elegir: contar, reemplazar o elimiar")
    
    # Ejemplo
    
    texto = "buenos días, princesa!"
    print("contar palabras: ")
    print(procesar_texto(texto,"contar"))
    print("remplar_palabras: ")
    print(reemplazar_palabras(texto,"reemplazar", "princesa","principe"))
    print("eliminar_palabras: ")
    print(procesar_texto(texto, "eliminar", "princesa"))
    
    

# Ejercicio 38: Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

hora= int(input("Introduce que hora es 0-23: "))

if hora < 0 or hora > 23:
    print ("por favor, introduce una hora valida")
elif 6 <= hora < 12:
    print("es por la mañana")
elif 12<= hora > 20:
    print("es por la tarde")
else:
    print("es por la noche")
    
    
    

# Ejercicio 39: Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
    # Las reglas de calificación son:
        # 0 - 69 insuficiente
        # 70 - 79 bien
        # 80 - 89 muy bien
        # 90 - 100 excelente
        
calificacion = int(input("por favor, introduce la calificación del alumno (0-100): "))

if 0 <= calificacion <= 69:
    print("Insuficiente")
elif 70 <= calificacion <= 79:
    print("Bien")
elif 80 <= calificacion <= 89:
    print("Muy bien")
elif 90 <= calificacion <= 100:
    print("Excelente")



# Ejercicio 40: Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).     

def area_figura(figura, datos):

    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio, = datos
        return 3.14159 * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError("Figura no reconocida. Usa: rectangulo, circulo o triangulo.")

# Ejemplo

print(area_figura ("triangulo", (9,2)))
print(area_figura ("rectangulo", (38,15)))
print(area_figura ("circulo", (3,)))



# Ejercicio 41: En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
    # 1. Solicita al usuario que ingrese el precio original de un artículo.
    # 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
    # 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
    # 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 
    # 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
    # 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.


precio = float(input("Introduce el precio original del artículo: "))

tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

descuento = 0  

if tiene_cupon == "sí" or tiene_cupon == "si":
    descuento = float(input("Introduce el valor del cupón de descuento: "))
    if descuento > 0:
        precio_final = precio - descuento
        if precio_final < 0:
            precio_final = 0  
    else:
        print("El cupón no es válido (debe ser mayor a 0).")
        precio_final = precio
elif tiene_cupon == "no":
    precio_final = precio
else:
    print("Respuesta no válida. No se aplicará descuento.")
    precio_final = precio

print(f"El precio final de la compra es: {precio_final} €")
