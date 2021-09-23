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
from datetime import date, datetime as dt
assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(tipo):

    catalogo = {'artist': None,
               'artworks': None,
               'Artw_Nacionalidades': None,}

    catalogo['artist'] = lt.newList(datastructure= tipo)
    catalogo['artworks'] = lt.newList(datastructure= tipo)
    catalogo["Artw_Nacionalidades"] = lt.newList(datastructure= tipo)

    return catalogo

# Funciones para agregar informacion al catalogo

def addArtists(catalog, artist):
    lt.addLast(catalog['artist'], artist) 

def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
def addArtw_Nt(Lista,catalog):
    lt.addLast(Lista["Artw_Nacionalidades"],catalog)

# Funciones para creacion de datos


# Funciones de consulta
def Artistinrange(lista_ordenada,date1,date2):
    size = lt.size(lista_ordenada)
    i = 0 
    numeroArtistas = 0
    Artistinrange = lt.newList()
    while i <= size:
        elemento = lt.getElement(lista_ordenada,i)
        fecha_a_comparar = int(elemento["BeginDate"])
        if  fecha_a_comparar >= date1 and fecha_a_comparar <= date2:
            numeroArtistas +=1
            lt.addLast(Artistinrange,elemento)
        i +=1
    return numeroArtistas, Artistinrange
def Artorksinrange (lista_ordenada,date1,date2):
    fecha1 = time.strptime(date1, "%Y-%m-%d")
    fecha2 = time.strptime(date2, "%Y-%m-%d")
    size = lt.size(lista_ordenada)
    i = 0 
    numeroArtworks = 0
    numeroPurchase = 0
    Artworksinrange = lt.newList()
    while i <= size:
        elemento = lt.getElement(lista_ordenada,i)
        fecha = elemento["DateAcquired"]
        if fecha != "":
            fecha_a_comparar = time.strptime(fecha, "%Y-%m-%d")
            comparacion = fecha_a_comparar >= fecha1 and fecha_a_comparar <= fecha2
            if comparacion == True:
                numeroArtworks += 1
                lt.addLast(Artworksinrange,elemento)

        purchase = elemento["CreditLine"]
        if "urchase" in purchase:
            numeroPurchase +=1
        i +=1
    return Artworksinrange, numeroPurchase, numeroArtworks
def searchConstituentID (Lista_artista,idAw):
    size = lt.size(Lista_artista)
    i = 0 
    id_a_comparar = idAw.strip("[]")
    while i < size:
        elemento = lt.getElement(Lista_artista,i)
        C_id = elemento["ConstituentID"]
        if C_id in id_a_comparar:
            return elemento["DisplayName"]

        i+= 1
def artworkNacionalidad (nacionalidades, lista_artworks, Lista_artist):
    #Diccionario Nacionalidad : Cantidad Artworks
    suma_total = {}
    ArtworksbyNt = {}
    i = 0
    while i <= lt.size(nacionalidades):
        nacionalidad = lt.getElement(nacionalidades,i)
        ArtworksByArtist = lt.newList()
        suma_total[nacionalidad] = 0
        ArtworksbyNt[nacionalidad] = ArtworksByArtist

        j = 0
        while j < lt.size(Lista_artist):

            elemento = lt.getElement(Lista_artist,j)
            nacionalidadArt= elemento["Nationality"]
            if nacionalidad ==nacionalidadArt:
                idA = elemento["ConstituentID"]
                num_art_byArtist = buscarArtworks(lista_artworks,idA,ArtworksByArtist)
                suma_total[nacionalidad] += num_art_byArtist
            j += 1
        i+=1
    return suma_total, ArtworksbyNt
def Buscar_Obras_Departamento ( departamento,lista_artworks):
    Total_obras = 0
    size = lt.size(lista_artworks)
    Lista_departamentos = lt.newList()
    # Comparar si el departamento que me dan es igual 
    i = 1
    while i < size:
        elemento = lt.getElement(lista_artworks,i)
        departamentos = elemento["Department"]
        if departamento == departamentos:
            Total_obras +=1
            lt.addLast(Lista_departamentos,elemento)
        i +=1
    return Total_obras, Lista_departamentos
def Calcular_Costo_dep (Lista_departamentos):
    Lista_con_costos = lt.newList()
    size = lt.size(Lista_departamentos)
    i = 1
    costo_total = 0
    peso_total = 0.0
    while i <= size:
        costo = 0
        elemento = lt.getElement(Lista_departamentos,i)
        peso = elemento["Weight (kg)"] 
        largo= elemento["Length (cm)"] 
        ancho = elemento["Width (cm)"] 
        alto = elemento["Height (cm)"] 
        if peso != "":
            costo = float(peso)*72.00
            elemento["CostoTransporte (USD)"] = costo
            lt.addLast(Lista_con_costos,elemento)
            costo_total += costo
            peso_total += peso
        elif largo != "" and ancho !="":
            largo = float(largo) / 100
            ancho = float(ancho) / 100
            costo = (largo * ancho) * 72.00
            elemento["CostoTransporte (USD)"] = costo
            lt.addLast(Lista_con_costos,elemento)
            costo_total += costo
            peso_total += 0.0
        elif largo != "" and alto !="":
            alto = float(alto) / 100
            largo = float(largo) / 100
            costo = (largo * alto) * 72.00
            elemento["CostoTransporte (USD)"] = costo
            lt.addLast(Lista_con_costos,elemento)
            costo_total += costo
            peso_total += 0.0
        elif alto != "" and ancho !="":
            alto = float(alto) / 100
            ancho = float(ancho) / 100
            costo = round((alto * ancho) * 72.00, 2)
            elemento["CostoTransporte (USD)"] = costo
            lt.addLast(Lista_con_costos,elemento)
            costo_total += costo
            peso_total += 0.0
        elif largo != "" and ancho !="" and alto != "":
            largo = float(largo) / 100
            alto = float(alto) / 100
            ancho = float(ancho) / 100
            costo = (largo * ancho * alto) * 72.00
            elemento["CostoTransporte (USD)"] = costo
            lt.addLast(Lista_con_costos,elemento)
            costo_total += costo
            peso_total += 0.0
        else:
            costo = 42.00
            elemento["CostoTransporte (USD)"] = costo
            lt.addLast(Lista_con_costos,elemento)
            costo_total += costo
            peso_total += 0.0
        i+=1
    return Lista_con_costos, round(costo_total,2), round(peso_total,2)
def buscarArtworks(lista_artworks,id,lista):
    Num_Artworks = 0
    tamañoArw = lt.size(lista_artworks)
    i = 0
    while i < tamañoArw:
        elemento = lt.getElement(lista_artworks,i)
        artwork = elemento["ConstituentID"]
        C_id = artwork.strip("[]")
        if id in C_id:
            Num_Artworks +=1
            lt.addLast(lista,elemento)

        i+=1 
    return Num_Artworks    
def Nacionalidades(catalog):
    Lista_nacionalidades = lt.newList()
    size = lt.size(catalog["artist"])
    i = 1
    while i < size:
        elemento = lt.getElement(catalog["artist"],i)
        nacionalidad = elemento["Nationality"]
        isIn = lt.isPresent(Lista_nacionalidades,nacionalidad)
        if isIn == 0:
            lt.addLast(Lista_nacionalidades,nacionalidad)
        i +=1
    return Lista_nacionalidades
def catalogoNacionalidadesVSArtworks (nacionalidades,artworks):
    lista = lt.newList()
    size = lt.size(nacionalidades)
    i = 1
    while i <= size:
        nationality = lt.getElement(nacionalidades,i)
        catalogo = {"Nacionalidad": nationality, "Artworks": artworks[nationality]}
        lt.addLast(lista,catalogo)
        i += 1 
    return lista


# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    date1= artwork1["DateAcquired"]
    date2= artwork2["DateAcquired"]
    if date1 != "" and date2 != "":
        fecha1 = time.strptime(date1, "%Y-%m-%d")
        fecha2 = time.strptime(date2, "%Y-%m-%d")
        comparacion = fecha1 < fecha2
        return comparacion
    else:
        return True
    
def cmpArtistByBirthDate(artist1, artist2):
    date1 = artist1["BeginDate"] 
    date2 = artist2["BeginDate"] 
    if date1 < date2:
        return True
    else:
        return False
def cmpArtVsNatByNumber(num1,num2):
    Numero1=num1["Artworks"]
    Numero2=num2["Artworks"]
    if Numero1 > Numero2:
        return True
    else:
        return False
def cmpDepByDate(artwork1, artwork2):
    date1= artwork1["Date"]
    date2= artwork2["Date"]
    if date1 < date2:
        return True
    else:
        return False    
def cmpDepByprice(obra1,obra2):
    costo_ob1 = obra1["CostoTransporte (USD)"]
    costo_ob2 = obra2["CostoTransporte (USD)"]
    if costo_ob1 > costo_ob2:
        return True
    else:
        return False
#Funciones de ordenamiento 
def sortDate(catalog, tipo):
    sub_list1 = lt.subList(catalog['artworks'], 1, lt.size(catalog['artworks']))
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
def sortArtVsNatBynum (catalog, tipo):
    sub_list2 = lt.subList(catalog,1, lt.size(catalog))
    sub_list2 = sub_list2.copy()
    sorted_list = ""
    if tipo == Qc:
        sorted_list = Qc.sort(sub_list2, 1, lt.size(sub_list2), cmpArtVsNatByNumber)
    else:
        sorted_list = tipo.sort(sub_list2, cmpArtVsNatByNumber)
    return sorted_list
def sortDepBydate (lista_Costo, tipo):
    sub_list2 = lt.subList(lista_Costo,1, lt.size(lista_Costo))
    sub_list2 = sub_list2.copy()
    sorted_list = ""
    if tipo == Qc:
        sorted_list = Qc.sort(sub_list2, 1, lt.size(sub_list2), cmpDepByDate)
    else:
        sorted_list = tipo.sort(sub_list2, cmpDepByDate)
    return sorted_list
def sortDepbyCost(lista_costo,tipo):
    sub_list2 = lt.subList(lista_costo,1, lt.size(lista_costo))
    sub_list2 = sub_list2.copy()
    sorted_list = ""
    if tipo == Qc:
        sorted_list = Qc.sort(sub_list2, 1, lt.size(sub_list2), cmpDepByprice)
    else:
        sorted_list = tipo.sort(sub_list2, cmpDepByprice)
    return sorted_list
    
    
   

