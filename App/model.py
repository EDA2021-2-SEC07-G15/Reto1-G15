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


import config as cf
from DISClib.ADT import list as lt
from DISClib.DataStructures import arraylist as array
from DISClib.DataStructures import singlelinkedlist as singlelink
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(tipo):

    catalogo = {'artist': None,
               'artworks': None,}

    catalogo['artist'] = lt.newList(datastructure= tipo)
    catalogo['artworks'] = lt.newList(datastructure= tipo)

    return catalogo

# Funciones para agregar informacion al catalogo

def addArtists(catalog, artist):
    lt.addLast(catalog['artist'], artist)
    authors = book['authors'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for author in authors:
        addBookAuthor(catalog, author.strip(), book)
    

def addArtworks(catalog, artwork):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['artworks'], artwork)
    # Se obtienen los autores del libro
    Dateacquired = artwork["DateAcquired"].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for Date in Dateacquired:
        addDateacquired(catalog, Date.strip(), artwork)
def addDateacquired(catalog,fecha,artwork):
    authors = catalog['authors']
    posauthor = lt.isPresent(authors, authorname)
    if posauthor > 0:
        author = lt.getElement(authors, posauthor)
    else:
        author = newAuthor(authorname)
        lt.addLast(authors, author)
    lt.addLast(author['books'], book)

    

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    if artwork1 
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    art
    # Funciones de ordenamiento