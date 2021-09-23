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

def printSortResults2(ord_artists,number_artist,date1,date2):
    print("Hay " + str(number_artist) + " artistas nacidos entre " + str(date1) + " y " + str(date2))
    size = lt.size(ord_artists)
    rango = 3
    print("Los primeros y ultimos 3 son: ")
    #Primeros 3 
    i = 0
    while i < rango:
        primeros = lt.getElement(ord_artists,i)
        print("Nombre: " + primeros["DisplayName"] + "; Año de Nacimiento: " + primeros["BeginDate"] + "; Año de Fallecimiento: " + primeros["EndDate"] + "; Nationality: " + primeros["Nationality"] + "; Gender: " + primeros["Gender"])
        i+=1
    #Uiltimos 3
    j = 2
    while j >= 0:
        ultimos = lt.getElement(ord_artists,size-j)
        print("Nombre: " + ultimos["DisplayName"] + "; Año de Nacimiento: " + ultimos["BeginDate"] + "; Año de Fallecimiento: " + ultimos["EndDate"] + "; Nationality: " + ultimos["Nationality"] + "; Gender: " + ultimos["Gender"])
        j -=1
def printSortResults(ord_artworks, numPurch,numAdq,date1,date2,lista_artistas):
    print("Hay " + str(numAdq) + " adquisiciones hechas entre " + str(date1) + " y " + str(date2))
    print("El MoMA adquirió " + str(numPurch) + " piezas unicas entre " + str(date1) + " y " + str(date2) )
    size = lt.size(ord_artworks)
    rango = 3
    print("Los primeros y ultimos 3 son: ")
    #Primeros 3 
    i = 0
    while i < rango:
        primeros = lt.getElement(ord_artworks,i)
        C_id = primeros["ConstituentID"]
        nombre = searchConstituentID(lista_artistas,C_id)
        print("Titulo: " + primeros["Title"] + "; Nombre: " + str(nombre) + "; Fecha: " + primeros["Date"] + "; Medio: " + primeros["Medium"] + "; Dimensiones: " + primeros["Dimensions"])
        i+=1
    #Uiltimos 3
    j = 2
    while j >= 0:
        ultimos = lt.getElement(ord_artworks,size-j)
        C_idu = ultimos["ConstituentID"]
        nombreU = searchConstituentID(lista_artistas,C_idu)
        print("Titulo: " + ultimos["Title"] + "; Nombre: " + nombreU + "; Fecha: " + ultimos["Date"] + "; Medio: " + ultimos["Medium"] + "; Dimensiones: " + ultimos["Dimensions"])
        j -=1
def PrintResults5(lista,lista2,lista_artistas):
    print( "El top 10 paises en MoMA son :")
    i = 1
    range = 10
    while i < range:
        elemento = lt.getElement(lista,i)
        print("Nacionalidad: " + str(elemento["Nacionalidad"]) + " Artworks: " + str(elemento["Artworks"]))
        i+=1
    Mejor_pais = lt.getElement(lista,1)
    pais = Mejor_pais["Nacionalidad"]
    #Primeros 3 
    d = 0
    while d < 3:
        primeros = lt.getElement(lista2[pais],d)
        C_id = primeros["ConstituentID"]
        nombre = searchConstituentID(lista_artistas,C_id)
        print("Titulo: " + primeros["Title"] + "; Nombre: " + str(nombre) + "; Fecha: " + primeros["Date"] + "; Medio: " + primeros["Medium"] + "; Dimensiones: " + primeros["Dimensions"])
        d+=1
    #Uiltimos 3
    j = 2
    while j >= 0:
        ultimos = lt.getElement(lista2[pais],lt.size(lista2[pais])-j)
        C_idu = ultimos["ConstituentID"]
        nombreU = searchConstituentID(lista_artistas,C_idu)
        print("Titulo: " + ultimos["Title"] + "; Nombre: " + nombreU + "; Fecha: " + ultimos["Date"] + "; Medio: " + ultimos["Medium"] + "; Dimensiones: " + ultimos["Dimensions"])
        j -=1
def printResults6(total_obras,departamento,costo_total,lista_costos,lista_olds,peso,lista_artistas):
    print("--------------------------------------------------------------------------------")
    print("El MoMA transportará " + str(total_obras) + " artefactos de " + str(departamento) )
    print("Peso estimado de carga (kg): " + str(peso))
    print("Costo estimado en carga (USD): " + str(costo_total) + " USD")
    print("------------El top 5 items más caros transportados son: ----------------")
    #Primeros 5 mas caros
    d = 0
    while d <= 4:
        primeros = lt.getElement (lista_costos,d)
        C_id = primeros["ConstituentID"]
        nombre = searchConstituentID(lista_artistas,C_id)
        print("Titulo: " + primeros["Title"])
        print("Nombre: " + str(nombre))
        print("Clasificación: " + str(primeros["Classification"]))
        print("Fecha: " + str(primeros["Date"]))
        print("Medio: " + primeros["Medium"])
        print("Dimensiones: " + primeros["Dimensions"])
        print("Costo transporte: " + str(primeros["CostoTransporte (USD)"]))        
        d+=1
    #Más viejos 
    print("----------El top 5 items mas antiguos son:     -----------------------")
    i = 0
    while i <= 4:
        primeros = lt.getElement (lista_olds,i)
        C_id = primeros["ConstituentID"]
        nombre = searchConstituentID(lista_artistas,C_id)
        print("Titulo: " + primeros["Title"])
        print("Nombre: " + str(nombre))
        print("Clasificación: " + str(primeros["Classification"]))
        print("Fecha: " + str(primeros["Date"]))
        print("Medio: " + str(primeros["Medium"]))
        print("Dimensiones: " + str(primeros["Dimensions"]))
        print("Costo transporte: " + str(primeros["CostoTransporte (USD)"]))        
        i+=1
def printMenu():
    print("Bienvenido")
    print("1 - Cargar información en el catálogo.")
    print("2 - Listar cronológicamente los artistas.")
    print("3 - Listar cronológicamente las adquisiciones.")
    print("4 - Clasificar las obras de un artista por técnica.")
    print("5 - Clasificar las obras por la nacionalidad de sus creadores.")
    print("6 - Transportar obras de un departamento.")
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
def consulta_rango_edad(lista_ordenada,date1,date2):
    return controller.ArtistinRange(lista_ordenada,date1,date2)
def consultar_adquisiciones_rango(lista,date1,date2):
    return controller.ArtworksinRange(lista,date1,date2)
def searchConstituentID(lista,id):
    return controller.Busqueda_id(lista,id)
def listaNacionalidades (catalog):
    return controller.listaNacionalidades(catalog)
def ArtworksByNationality (nacionalidades, lista_artworks, Lista_artist):
    return controller.ArtworkPorNacionalidad(nacionalidades, lista_artworks, Lista_artist)
def ArtVsNationality(nacionalidades,artworks):
    return controller.artVSnat(nacionalidades,artworks)
def LoadArtNat(lista,catalog):
    return controller.LoadArtNat(lista,catalog)
def Busqueda_Dep(departamento,lista_artworks):
    return controller.Busqueda_depa(departamento,lista_artworks)
def Calculo_costo(lista_departamentos):
    return controller.Calculo_costos(lista_departamentos)
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
        Artistinrange = consulta_rango_edad(result1[1],date1,date2)
        printSortResults2(Artistinrange[1], Artistinrange[0],date1,date2)    
    elif int(inputs[0]) == 3:
        date1 = input("Indique el año inicial de la búsqueda en formato AAAA-MM-DD: ")
        date2 = input("Indique el año final de la búsqueda en formato AAAA-MM-DD: ")
        tipo = seleccion_ordenamiento()
        result2 = controller.sortDate(catalog,tipo)
        Artowrkinrange = consultar_adquisiciones_rango(result2[1],date1,date2)
        printSortResults(Artowrkinrange[0],Artowrkinrange[1],Artowrkinrange[2],date1,date2,catalog["artist"])
    elif int(inputs[0]) == 5:
        lista_nacionalidades = listaNacionalidades(catalog)
        Artworks_por_Nacionalidad = ArtworksByNationality(lista_nacionalidades,catalog["artworks"],catalog["artist"])
        Catalogo_Art_Nacionalidad = ArtVsNationality (lista_nacionalidades,Artworks_por_Nacionalidad[0])
        LoadArtNat(Catalogo_Art_Nacionalidad,catalog)
        tipo = seleccion_ordenamiento()
        result5 = controller.sortArtVsNatBynum(catalog["Artw_Nacionalidades"],tipo)
        PrintResults5(lt.getElement(result5,1),Artworks_por_Nacionalidad[1],catalog["artist"])
    elif int(inputs[0]) == 6:
        departamento = input("Ingrese el departamento que desea consultar: ")
        tipo = seleccion_ordenamiento()
        lista_departamentos = Busqueda_Dep(departamento,catalog["artworks"])
        Lista_costos = Calculo_costo(lista_departamentos[1])
        orden_fecha = controller.sortDepabydate(Lista_costos[0],tipo)
        orden_costos= controller.sortDepbyprice(Lista_costos[0],tipo)
        printResults6(lista_departamentos[0],departamento,Lista_costos[1],orden_costos,orden_fecha,Lista_costos[2],catalog["artist"])    
    else:
        sys.exit(0)
sys.exit(0)
