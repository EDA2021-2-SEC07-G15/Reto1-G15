"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.liststructure import subList
import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.DataStructures import arraylist as array
from DISClib.DataStructures import singlelinkedlist as singlelink
from DISClib.Algorithms.Sorting import shellsort as Sa
from DISClib.Algorithms.Sorting import mergesort as Mg
from DISClib.Algorithms.Sorting import insertionsort as In
from DISClib.Algorithms.Sorting import quicksort as Qc
from datetime import datetime as dt
assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(tipo):

    catalogo = {'artist': None,
               'artworks': None,
               'artistsByDate': None,}

    catalogo['artist'] = lt.newList(datastructure= tipo)
    catalogo['artworks'] = lt.newList(datastructure= tipo)
    catalogo['artistsByDates'] = lt.newList(datastructure= tipo)

    return catalogo

# Funciones para agregar informacion al catalogo

def addArtists(catalog, artist):
    lt.addLast(catalog['artist'], artist)    

def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)

# Funciones para creacion de datos


# Funciones de consulta





# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    fecha_1 = artwork1["DateAcquired"]
    fecha_2= artwork2["DateAcquired"]
    date_1 = fecha_1.split("-")
    date_2 = fecha_2.split("-")
    if len(date_1) != 1 and len(date_2) != 1:
        if date_1[0] < date_2[0]:
            return True
            
        elif date_1[1] < date_2[1]:
            return True
        elif date_1[2] < date_2[2]:
            return True
        else:
            return False
    else:
        return False

def cmpArtistByBirthDate(artist1, artist2):
    date1 = artist1["BeginDate"] 
    date2 = artist2["BeginDate"] 
    if date1 != "0" and date2 != "0":
        if date1 < date2:
            return True
        else:
            return False
    else:
        return False
    
#Funciones de ordenamiento 
def sortDate(catalog, size, tipo):
    sub_list1 = lt.subList(catalog['artworks'], 1, size)
    sub_list1 = sub_list1.copy()
    start_time = time.process_time()
    sorted_list = ""
    if tipo == Qc:
        sorted_list = Qc.sort(sub_list1, 1, lt.size(sub_list1), cmpArtworkByDateAcquired)
    else:
        sorted_list = tipo.sort(sub_list1, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def sortArtistbyDate (catalog, tipo):
    sub_list2 = lt.subList(catalog["artist"],1, lt.size(catalog["artist"]))
    sub_list2 = sub_list2.copy()
    start_time = time.process_time()
    sorted_list = ""
    if tipo == Qc:
        sorted_list = Qc.sort(sub_list2, 1, lt.size(sub_list2), cmpArtistByBirthDate)
    else:
        sorted_list = tipo.sort(sub_list2, cmpArtistByBirthDate)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

    
   

