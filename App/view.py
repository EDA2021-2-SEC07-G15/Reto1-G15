﻿"""
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

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        controller.loadArtists('Artists-utf8-small.csv')
        artists = controller.loadArtists('Artists-utf8-small.csv')
        print('Total de artistas cargados: ' + str(lt.size(artists)))
        print("Los últimos tres elementos de la lista total de artistas cargados son: El último es " + str(lt.lastElement(artists)) + " ; el penúltimo es : " + str(lt.getElement(artists, (int(lt.size(artists)-1)))) + " y el antepenúltimo es : " + str(lt.getElement(artists, (int(lt.size(artists)-2)))))

        controller.loadArtworks('Artworks-utf8-small.csv')
        artworks = controller.loadArtworks('Artworks-utf8-small.csv')
        print('Total de obras de arte cargadas: ' + str(lt.size(artworks)))
        print("Los últimos tres elementos de la lista total de obras de arte cargadas son: La última es " + str(lt.lastElement(artworks)) + " ; la penúltima es : " + str(lt.getElement(artworks, (int(lt.size(artists)-1)))) + " y la antepenúltima es : " + str(lt.getElement(artworks, (int(lt.size(artists)-2)))))

    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
