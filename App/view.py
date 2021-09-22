"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def iniciarCatalogo(tipo):
    return controller.initCatalog(tipo)
def loadData(catalog,artist,artworks):
    controller.loadData(catalog,artist,artworks)

def printSortResults2(ord_artists,date1,date2,sample =10 ):
    size = lt.size(ord_artists)
    if size > sample:
        print("Los primeros ", sample, " artistas ordenados por fecha de nacimiento son:")
        i = 0
        contador = 0
        while i <= size:
            work= lt.getElement(ord_artists,i)
            fecha_a_comparar = int(work["BeginDate"])
            if  fecha_a_comparar >= date1 and fecha_a_comparar <= date2:
                if contador <= sample:
                    print ("Nombre: " + work["DisplayName"] + "; Año de Nacimiento: " + work["BeginDate"] + "; Año de Fallecimiento: " + work["EndDate"] + "; Nationality: " + work["Nationality"] + "; Año de Nacimiento: " + work["Gender"])
                    contador +=1                 
            i +=1

def printSortResults(ord_artworks, sample=10):
    size = lt.size(ord_artworks)
    if size > sample:
        print("los primeros ", sample, " artworks ordenados por fecha de adquisición son:")

        i = 1
        while i <= sample:
            work= lt.getElement(ord_artworks,i)
            print ("Titulo: " + work["Title"] + " DateAcquired: " + work["DateAcquired"])
            i +=1


def printMenu():
    print("Bienvenido")
    print("1 - Cargar información en el catálogo.")
    print("2 - Listar cronológicamente los artistas.")
    print("3 - Listar cronológicamente las adquisiciones.")
    print("4 - Clasificar las obras de un artista por técnica.")
    print("5 - Clasificar las obras por la nacionalidad de sus creadores.")
    print("6 - Transportar obras de un departamento.")
    print("7 - Proponer una nueva exposición en el museo.")
    print("0- Salir")
def selección_estructura()-> str:
    estructura = ""
    print("¿Cual estructura de datos desea usar para cargar la información?")
    print("1---- ARRAY_LIST")
    print("2---- LINKED_LIST")
    tipo = input("Seleccione una opción: ")
    if tipo == 1:
        estructura = "ARRAY_LIST"
    elif tipo ==2:
        estructura = "SINGLE_LINKED_LIST"
    return estructura
def seleccion_ordenamiento():
    ordenamiento = ""
    print("¿Con que tipo de ordenamiento desea organizar los artistas o los artworks?")
    print("1) Insertion sort ")
    print("2) Shell sort ")
    print("3) Merge sort ")
    print("4) Quick sort ")
    tipo = input("Seleccione una opción: ")
    if tipo == 1:
        ordenamiento = "In"
    elif tipo == 2:
        ordenamiento = "Sa"
    elif tipo == 3:
        ordenamiento = "Mg"
    elif tipo == 4:
        ordenamiento = "Qc"
    return ordenamiento

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipo_estructura = selección_estructura()
        print("Cargando información de los archivos ....")
        catalog = iniciarCatalogo(tipo_estructura)
        loadData(catalog,'Artists-utf8-small.csv','Artworks-utf8-small.csv')
        print("Se cargó exitosamente la información")
        print("Artistas cargados: " + str(lt.size(catalog["artist"])))
        print("Artworks cargados: " + str(lt.size(catalog["artworks"])))

    elif int(inputs[0]) == 2:
        date1 = int(input("Indique el año inicial de la búsqueda en formato YYYY: "))
        date2 = int(input("Indique el año final de la búsqueda en formato YYYY: "))
        tipo = seleccion_ordenamiento()
        result1 = controller.sortArtistByDate(catalog,tipo)
        print("Para la muestra entre", date1 , " y " , date2, ", el tiempo (mseg) es: ", str(result1[0]))
        printSortResults2(result1[1],date1,date2)
        
    elif int(inputs[0]) == 3:
        size = input("Indique tamaño de la muestra: ")
        tipo = seleccion_ordenamiento()
        result2 = controller.sortDate(catalog, int(size), tipo)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
        str(result2[0]))
        printSortResults(result2[1])
        
    else:
        sys.exit(0)
sys.exit(0)
