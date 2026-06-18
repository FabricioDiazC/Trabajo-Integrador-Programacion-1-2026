#TRABAJO PRÁCTICO INTEGRADOR - Programación 1
#Sistema de Gestión de Datos de Países

import csv
import os

#  CONSTANTES 
NOMBRE_ARCHIVO = "paises.csv"   # Nombre del archivo CSV de datos
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]  # Encabezados del CSV


#  MÓDULO 1: ENTRADA / SALIDA (lectura y escritura del CSV)
def cargar_csv(nombre_archivo):
    #Lee el archivo CSV y devuelve una lista de diccionarios. Cada fila del CSV se convierte en un diccionario con las claves: nombre, poblacion, superficie, continente.
    """
    Argumentos:
        nombre_archivo (str): Ruta al archivo CSV.

    Retorna:
        list: Lista de diccionarios con los datos de países.
    """
    paises = []

    # Verificamos que el archivo exista antes de intentar abrirlo
    if not os.path.exists(nombre_archivo):
        print(f"No se encontró '{nombre_archivo}'. Se comenzará con una lista vacía.")
        return paises

    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Convertimos población y superficie a enteros al cargar
                pais = {
                    "nombre":     fila["nombre"].strip(),
                    "poblacion":  int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip()
                }
                paises.append(pais)
    except (KeyError, ValueError) as e:
        print(f"Error: El archivo CSV tiene un formato incorrecto: {e}")
    except Exception as e:
        print(f"Error: No se pudo leer el archivo: {e}")

    return paises


def guardar_csv(paises, nombre_archivo):
    
    #Guarda la lista de diccionarios de vuelta al archivo CSV, sobreescribiendo su contenido con los datos actuales en memoria.
    """
    Argumentoss:
        paises (list): Lista de diccionarios con los datos de países.
        nombre_archivo (str): Ruta al archivo CSV destino.
    """
    try:
        with open(nombre_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()          # Escribe la línea de encabezado
            escritor.writerows(paises)      # Escribe todos los países
        print(f"Datos guardados correctamente en '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error: No se pudo guardar el archivo: {e}")



#  MÓDULO 2: VISUALIZACIÓN
def imprimir_separador(ancho=70):
    print("-" * ancho)


def imprimir_pais(pais):
    """
    Muestra los datos de un único país con formato legible.

    Argumento:
        pais (dict): Diccionario con los datos del país.
    """
    print(f"  País       : {pais['nombre']}")
    print(f"  Continente : {pais['continente']}")
    print(f"  Población  : {pais['poblacion']:,} habitantes")
    print(f"  Superficie : {pais['superficie']:,} km²")
    imprimir_separador()


def imprimir_lista_paises(paises, titulo="Lista de países"):
    """
    Muestra una lista de países precedida de un título.

    Argumentos:
        paises (list): Lista de diccionarios.
        titulo (str): Título a mostrar antes de la lista.
    """
    imprimir_separador()
    print(f"  {titulo.upper()}")
    imprimir_separador()
    if not paises:
        print("  (No hay países para mostrar con ese criterio.)")
        imprimir_separador()
    else:
        for pais in paises:
            imprimir_pais(pais)



#  MÓDULO 3: VALIDACIONES DE INPUT
def pedir_texto(mensaje):

    #Solicita al usuario una cadena de texto no vacía.Repite la solicitud hasta recibir un valor válido.

    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: El campo no puede estar vacío. Inténtelo de nuevo.")


def pedir_entero_positivo(mensaje):
    #Le pide al usuario un número entero positivo. Repite la solicitud hasta recibir un valor válido.

    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor > 0:
                return valor
            else:
                print("Error: El valor debe ser un número entero positivo (mayor a 0).")
        except ValueError:
            print("Error: Entrada inválida. Por favor, ingrese solo números enteros.")


def pedir_opcion_menu(opciones_validas, mensaje="  Seleccione una opción: "):
    
    #Le pide al usuario que elija entre un conjunto de opciones válidas.

    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        print(f"Error: Opción no válida. Opciones posibles: {opciones_validas}")


#MÓDULO 4: BÚSQUEDA
def buscar_pais_por_nombre(paises, nombre_buscado):

    #Busca países cuyo nombre contenga el texto ingresado(búsqueda parcial, sin distinción de mayúsculas/minúsculas).
    """
    Argumentos:
        paises (list): Lista completa de países.
        nombre_buscado (str): Texto a buscar en el nombre.

    Retorna:
        list: Lista de países que coinciden con la búsqueda.
    """
    termino = nombre_buscado.lower()
    resultados = [p for p in paises if termino in p["nombre"].lower()]
    return resultados


def encontrar_pais_exacto(paises, nombre):

    #Devuelve el diccionario del país cuyo nombre coincida exactamente (sin distinción de mayúsculas/minúsculas).
    """
    Argumentos:
        paises (list): Lista completa de países.
        nombre (str): Nombre exacto a buscar.

    Retorna:
        diccionario o None: El diccionario del país o None si no existe.
    """
    nombre_lower = nombre.lower()
    for pais in paises:
        if pais["nombre"].lower() == nombre_lower:
            return pais
    return None


# MÓDULO 5: FILTROS
def filtrar_por_continente(paises, continente):
    
    #Filtra la lista de países por continente.

    termino = continente.lower()
    return [p for p in paises if termino in p["continente"].lower()]


def filtrar_por_rango_poblacion(paises, minimo, maximo):
    """
    Filtra países cuya población esté dentro de un rango dado.

    Argumentos:
        paises (list): Lista completa de países.
        minimo (int): Población mínima (incluida).
        maximo (int): Población máxima (incluida).

    Retorna:
        list: Países dentro del rango de población.
    """
    return [p for p in paises if minimo <= p["poblacion"] <= maximo]


def filtrar_por_rango_superficie(paises, minimo, maximo):
    """
    Filtra países cuya superficie esté dentro de un rango dado.

    Argumentos:
        paises (list): Lista completa de países.
        minimo (int): Superficie mínima en km² (incluida).
        maximo (int): Superficie máxima en km² (incluida).

    Retorna:
        list: Países dentro del rango de superficie.
    """
    return [p for p in paises if minimo <= p["superficie"] <= maximo]


#  MÓDULO 6: ORDENAMIENTO
def ordenar_paises(paises, criterio, ascendente=True):
    """
    Ordena la lista de países según el criterio indicado
    usando una función lambda como clave de ordenamiento.

    Argumentos:
        paises (list): Lista de países a ordenar.
        criterio (str): Campo por el que ordenar ('nombre', 'poblacion', 'superficie').
        ascendente (bool): True = ascendente, False = descendente.

    Retornas:
        list: Nueva lista ordenada (no modifica la original).
    """
    # Usamos sorted() con lambda para no modificar la lista en memoria
    lista_ordenada = sorted(paises, key=lambda p: p[criterio], reverse=not ascendente)
    return lista_ordenada



#  MÓDULO 7: ESTADÍSTICAS
def calcular_estadisticas(paises):
    """
    Calcula y muestra estadísticas generales sobre los países:
    - País con mayor y menor población.
    - Promedio de población y superficie.
    - Cantidad de países por continente.

    Argumento:
        paises (list): Lista completa de países.
    """
    if not paises:
        print("No hay datos suficientes para calcular estadísticas.")
        return

    #Población máxima y mínima usando la función max/min con key lambda
    pais_max_pob = max(paises, key=lambda p: p["poblacion"])
    pais_min_pob = min(paises, key=lambda p: p["poblacion"])

    #Promedios
    total_paises    = len(paises)
    suma_poblacion  = sum(p["poblacion"]  for p in paises)
    suma_superficie = sum(p["superficie"] for p in paises)
    prom_poblacion  = suma_poblacion  // total_paises   # División entera
    prom_superficie = suma_superficie // total_paises

    #Conteo por continente 
    conteo_continentes = {}
    for pais in paises:
        cont = pais["continente"]
        # Si el continente ya existe en el diccionario, sumamos 1; si no, lo inicializamos
        conteo_continentes[cont] = conteo_continentes.get(cont, 0) + 1

    #Mostrar resultados 
    imprimir_separador()
    print("  ESTADÍSTICAS GENERALES")
    imprimir_separador()
    print(f"  Total de países registrados : {total_paises}")
    print()
    print(f"  País con MAYOR población    : {pais_max_pob['nombre']} ({pais_max_pob['poblacion']:,} hab.)")
    print(f"  País con MENOR población    : {pais_min_pob['nombre']} ({pais_min_pob['poblacion']:,} hab.)")
    print()
    print(f"  Promedio de población       : {prom_poblacion:,} habitantes")
    print(f"  Promedio de superficie      : {prom_superficie:,} km²")
    print()
    print("  Cantidad de países por continente:")
    for continente, cantidad in sorted(conteo_continentes.items()):
        print(f"    · {continente:<15} : {cantidad} país/es")
    imprimir_separador()


#  MÓDULO 8: OPERACIONES de Alta, Baja y Modificación
def agregar_pais(paises):
    """
    Solicita datos al usuario y agrega un nuevo país a la lista.
    Valida que el país no exista previamente (por nombre exacto).
    Guarda los cambios en el CSV automáticamente.

    Argumento:
        paises (list): Lista de países (se modifica en el lugar).
    """
    imprimir_separador()
    print("  AGREGAR NUEVO PAÍS")
    imprimir_separador()

    nombre = pedir_texto("  Nombre del país    : ")

    # Verificamos que el país no exista ya en la lista
    if encontrar_pais_exacto(paises, nombre):
        print(f"El país '{nombre}' ya existe en el registro.")
        return

    poblacion   = pedir_entero_positivo("  Población          : ")
    superficie  = pedir_entero_positivo("  Superficie (km²)   : ")
    continente  = pedir_texto("  Continente         : ")

    nuevo_pais = {
        "nombre":     nombre,
        "poblacion":  poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    print(f"\n País '{nombre}' agregado correctamente.")
    guardar_csv(paises, NOMBRE_ARCHIVO)


def actualizar_pais(paises):
    """
    Permite actualizar la población y/o superficie de un país existente.
    Busca el país por nombre exacto y guarda los cambios en el CSV.

    Argumento:
        paises (list): Lista de países (se modifica en el lugar).
    """
    imprimir_separador()
    print("  ACTUALIZAR DATOS DE UN PAÍS")
    imprimir_separador()

    nombre = pedir_texto("  Nombre del país a actualizar: ")
    pais   = encontrar_pais_exacto(paises, nombre)

    if pais is None:
        print(f"Error: No se encontró el país '{nombre}'.")
        return

    print(f"\n  Datos actuales de {pais['nombre']}:")
    imprimir_pais(pais)
    print("  (Presione ENTER para mantener el valor actual)")

    # Actualización de población (permite mantener valor actual con ENTER)
    entrada_pob = input(f"  Nueva población (actual: {pais['poblacion']:,}): ").strip()
    if entrada_pob:
        try:
            nueva_pob = int(entrada_pob)
            if nueva_pob > 0:
                pais["poblacion"] = nueva_pob
            else:
                print("Valor no válido. Se mantuvo la población original.")
        except ValueError:
            print("Entrada no numérica. Se mantuvo la población original.")

    # Actualización de superficie
    entrada_sup = input(f"  Nueva superficie (actual: {pais['superficie']:,} km²): ").strip()
    if entrada_sup:
        try:
            nueva_sup = int(entrada_sup)
            if nueva_sup > 0:
                pais["superficie"] = nueva_sup
            else:
                print("Valor no válido. Se mantuvo la superficie original.")
        except ValueError:
            print("Entrada no numérica. Se mantuvo la superficie original.")

    print(f"\n Datos de '{pais['nombre']}' actualizados.")
    guardar_csv(paises, NOMBRE_ARCHIVO)


#  MÓDULO 9: SUBMENÚS 
def submenu_buscar(paises):
    #Submenú para la búsqueda de países por nombre.
    imprimir_separador()
    print("  BÚSQUEDA DE PAÍSES")
    imprimir_separador()

    termino = pedir_texto("  Ingrese el nombre o parte del nombre: ")
    resultados = buscar_pais_por_nombre(paises, termino)
    imprimir_lista_paises(resultados, titulo=f"Resultados para '{termino}'")


def submenu_filtrar(paises):
    """Submenú con los distintos tipos de filtros disponibles."""
    imprimir_separador()
    print("  FILTRAR PAÍSES")
    imprimir_separador()
    print("  1. Por continente")
    print("  2. Por rango de población")
    print("  3. Por rango de superficie")
    imprimir_separador()

    opcion = pedir_opcion_menu(["1", "2", "3"])

    if opcion == "1":
        continente = pedir_texto("  Ingrese el continente: ")
        resultados = filtrar_por_continente(paises, continente)
        imprimir_lista_paises(resultados, titulo=f"Países en '{continente}'")

    elif opcion == "2":
        print("  Ingrese el rango de población:")
        minimo = pedir_entero_positivo("    Mínimo (habitantes): ")
        maximo = pedir_entero_positivo("    Máximo (habitantes): ")
        if minimo > maximo:
            print("Error: El mínimo no puede ser mayor que el máximo.")
            return
        resultados = filtrar_por_rango_poblacion(paises, minimo, maximo)
        imprimir_lista_paises(resultados, titulo=f"Países con población entre {minimo:,} y {maximo:,}")

    elif opcion == "3":
        print("  Ingrese el rango de superficie:")
        minimo = pedir_entero_positivo("    Mínimo (km²): ")
        maximo = pedir_entero_positivo("    Máximo (km²): ")
        if minimo > maximo:
            print("Error: El mínimo no puede ser mayor que el máximo.")
            return
        resultados = filtrar_por_rango_superficie(paises, minimo, maximo)
        imprimir_lista_paises(resultados, titulo=f"Países con superficie entre {minimo:,} y {maximo:,} km²")


def submenu_ordenar(paises):
    #Submenú para ordenar y mostrar la lista de países.
    imprimir_separador()
    print("  ORDENAR PAÍSES")
    imprimir_separador()
    print("  Ordenar por:")
    print("  1. Nombre")
    print("  2. Población")
    print("  3. Superficie")
    imprimir_separador()

    opcion_criterio = pedir_opcion_menu(["1", "2", "3"])
    criterios = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    criterio = criterios[opcion_criterio]

    print("\n  Orden:")
    print("  1. Ascendente")
    print("  2. Descendente")
    opcion_orden = pedir_opcion_menu(["1", "2"])
    ascendente = (opcion_orden == "1")

    lista_ordenada = ordenar_paises(paises, criterio, ascendente)
    orden_str = "ascendente" if ascendente else "descendente"
    imprimir_lista_paises(lista_ordenada, titulo=f"Países ordenados por {criterio} ({orden_str})")


#  MÓDULO 10: MENÚ PRINCIPAL
def mostrar_menu_principal():
    #Imprime el menú principal del programa
    print("   GESTIÓN DE DATOS DE PAÍSES")
    print("  1. Agregar un país")
    print("  2. Actualizar población y superficie")
    print("  3. Buscar país por nombre")
    print("  4. Filtrar países")
    print("  5. Ordenar países")
    print("  6. Ver estadísticas")
    print("  7. Mostrar todos los países")
    print("  0. Salir")

def ejecutar_menu_principal(paises):
    """
    Bucle principal del programa. Muestra el menú y llama
    a la función correspondiente según la opción del usuario.

    Argumento:
        paises (list): Lista de diccionarios con los datos cargados.
    """
    opciones_validas = ["0", "1", "2", "3", "4", "5", "6", "7"]

    while True:
        mostrar_menu_principal()
        opcion = pedir_opcion_menu(opciones_validas)

        if   opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            submenu_buscar(paises)
        elif opcion == "4":
            submenu_filtrar(paises)
        elif opcion == "5":
            submenu_ordenar(paises)
        elif opcion == "6":
            calcular_estadisticas(paises)
        elif opcion == "7":
            imprimir_lista_paises(paises, titulo="Todos los países")
        elif opcion == "0":
            print("\n Saliendo\n")
            break



#ENTRADA DEL PROGRAMA
def main():
    """
    Función principal que inicia el programa:
    1. Carga los datos desde el CSV.
    2. Lanza el menú interactivo.
    """
    print("\n  Cargando datos desde el archivo CSV...")
    paises = cargar_csv(NOMBRE_ARCHIVO)
    print(f"Se cargaron {len(paises)} países.\n")
    ejecutar_menu_principal(paises)

if __name__ == "__main__":
    main()
