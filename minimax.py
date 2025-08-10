import random
import os

print('Bienvenido al juego del Gato y el Raton')

input('PRESIONE ENTER PARA COMENZAR')

#generador de mapa 
def generar_mapa(numerode_filas,numerode_columnas):
    mapa=[]
    for _ in range(numerode_filas):#genera filas
        columnas=['.'] * numerode_columnas #genera columnas
        mapa.append(columnas)
    return mapa

#funcion para mostrar el mapa
def mostrar_mapa(mapaso):
    os.system('clear')
    for fila in mapaso:
        print('  '.join(fila))

#funcion para colocar un personaje
def colocar_personaje(agregar_mapa, posicion, simbolo):
    fila,columna=posicion
    agregar_mapa[fila][columna]=simbolo


#bloque que posicionan al gato y al raton en su posicion inicial

mapa_de_juego =generar_mapa(5,5)

posicion_raton=(0,0)

posicion_gato=(4,4)

colocar_personaje(mapa_de_juego,posicion_raton,'🐀')

colocar_personaje(mapa_de_juego,posicion_gato,'😼')

mostrar_mapa(mapa_de_juego)

input('presione enter para comenzar')

#bloque que realiza movimientos  

direcciones_gato=[(-1,0),(1,0),(0,-1),(0,1)] 

direcciones_raton=[
     (-1,0),(1,0),(0,-1),(0,1),   #movimientos normales 
     (-1,-1),(-1,1),(1,-1),(1,1)  #movimientos diagonales
     ]
def movimiento_aleatorio(tablero,posicion_actual,simbolo2,lista_direcciones):

    tablero_dimension_fila=len(tablero)

    tablero_dimension_columna=len(tablero[0])

    posicion = posicion_actual

    for _ in range(1):
            
            posicion_original_fila, posicion_original_columna=posicion_actual

            tablero[posicion_original_fila][posicion_original_columna]='.'

            while True:
                nueva_direccion=random.choice(lista_direcciones)

                movimiento_actualizado_fila = posicion_original_fila + nueva_direccion[0]

                movimiento_actualizado_columna = posicion_original_columna + nueva_direccion[1]

                if movimiento_actualizado_fila >= 0 and movimiento_actualizado_fila < tablero_dimension_fila:

                    if movimiento_actualizado_columna >= 0 and movimiento_actualizado_columna < tablero_dimension_columna:
                        break
            posicion=(movimiento_actualizado_fila,movimiento_actualizado_columna)

            colocar_personaje(tablero,posicion,simbolo2)

            mostrar_mapa(tablero)

            input('Presione ENTER para continuar')

    return posicion

movimientos_random=3

for _ in range(movimientos_random):
        
        posicion_raton = movimiento_aleatorio(mapa_de_juego,posicion_raton,'🐀',direcciones_raton)
        
        posicion_gato=movimiento_aleatorio(mapa_de_juego,posicion_gato,'😼',direcciones_gato)











        

            
