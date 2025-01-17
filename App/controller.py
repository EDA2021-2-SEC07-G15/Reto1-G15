﻿"""
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
 """

import config as cf
import model
import csv
from DISClib.Algorithms.Sorting import shellsort as Sa
from DISClib.Algorithms.Sorting import mergesort as Mg
from DISClib.Algorithms.Sorting import insertionsort as In
from DISClib.Algorithms.Sorting import quicksort as Qc


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(tipo):
    catalog = model.newCatalog(tipo)
    return catalog

# Funciones para la carga de datos
def loadData(catalog,artists,artworks):

    loadArtists(catalog,artists)
    loadArtworks(catalog,artworks)

def loadArtists(catalog,filename):
    """
    Carga los artistas del archivo.  
    """
    artsfile = cf.data_dir + filename
    lectura = csv.DictReader(open(artsfile, encoding="utf-8"))
    for artist in lectura:
        model.addArtists(catalog,artist)

def loadArtworks(catalog,filename):
    """
    Carga las obras de arte del archivo.  
    """
    artworksfile = cf.data_dir + filename
    lectura = csv.DictReader(open(artworksfile, encoding="utf-8"))
    for artwork in lectura:
        model.addArtworks(catalog, artwork)
def LoadArtNat (catalogo,lista):
    model.addArtw_Nt(lista,catalogo)
    

# Funciones de ordenamiento
def sortDate(catalog,ordenamiento):
    tipo = Sa
    if ordenamiento == "Mg":
        tipo = Mg
    elif ordenamiento == "In":
        tipo = In
    elif ordenamiento == "Qc":
        tipo = Qc
    return model.sortDate(catalog,tipo)
def sortArtistByDate(catalog, ordenamiento):
    tipo = Sa
    if ordenamiento == "Mg":
        tipo = Mg
    elif ordenamiento == "In":
        tipo = In
    elif ordenamiento == "Qc":
        tipo = Qc
    return model.sortArtistbyDate(catalog, tipo)

def sortArtistByName (catalog, ordenamiento):
    tipo = Sa
    if ordenamiento == "Mg":
        tipo = Mg
    elif ordenamiento == "In":
        tipo = In
    elif ordenamiento == "Qc":
        tipo = Qc
    return model.sortArtistByName(catalog, tipo)

def sortArtVsNatByMedium (lista, ordenamiento):
    tipo = Sa
    if ordenamiento == "Mg":
        tipo = Mg
    elif ordenamiento == "In":
        tipo = In
    elif ordenamiento == "Qc":
        tipo = Qc
    return model.sortArtistByMedium(lista,tipo)

def sortArtVsNatBynum (catalog, ordenamiento):
    tipo = Sa
    if ordenamiento == "Mg":
        tipo = Mg
    elif ordenamiento == "In":
        tipo = In
    elif ordenamiento == "Qc":
        tipo = Qc
    return model.sortArtVsNatBynum(catalog,tipo)
def sortDepabydate(lista_c,ordenamiento):
    tipo = Sa
    if ordenamiento == "Mg":
        tipo = Mg
    elif ordenamiento == "In":
        tipo = In
    elif ordenamiento == "Qc":
        tipo = Qc
    return model.sortDepBydate(lista_c,tipo)
def sortDepbyprice(listac,ordenamiento):
    tipo = Sa
    if ordenamiento == "Mg":
        tipo = Mg
    elif ordenamiento == "In":
        tipo = In
    elif ordenamiento == "Qc":
        tipo = Qc
    return model.sortDepbyCost(listac,tipo)

    
# Funciones de consulta sobre el catálogo
def ArtistinRange (lista_ordenada, date1,date2):
    return model.Artistinrange(lista_ordenada,date1,date2)

def ArtworksinRange(lista,date1,date2):
    return model.Artorksinrange(lista,date1,date2)

def Busqueda_id(lista,id):
    return model.searchConstituentID(lista,id)

def ArtistbyTech (lista, name):
    return model.ArtistByTech(lista, name)

def BusquedaArtistaPorConstituentID (lista, id):
    return model.searchArtistConstituentID(lista, id)

def listaNacionalidades(catalog):
    return model.Nacionalidades(catalog)

def ArtworkPorNacionalidad(nacionalidades, lista_artworks, Lista_artist):
    return model.artworkNacionalidad(nacionalidades,lista_artworks,Lista_artist)

def busquedaArtworksPorMedium(ArtistsArtworksByName):
    return model.busquedaArtworksPorMedium (ArtistsArtworksByName)

def artVSnat(nacionalidades,artworks):
    return model.catalogoNacionalidadesVSArtworks(nacionalidades,artworks)

def Busqueda_depa(departamento,lista_artworks):
    return model.Buscar_Obras_Departamento(departamento,lista_artworks)
    
def Calculo_costos(lista_departamentos):
    return model.Calcular_Costo_dep(lista_departamentos)