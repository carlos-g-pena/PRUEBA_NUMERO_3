import numpy as np
import time

menu = ['Comprar Entrada', 'Ver boletas', 'Salir']
num_boleta = 0


class Pelicula:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.asientos = np.full((10, 15), fill_value='.')

    def __str__(self):
        return f"{self.nombre}\n Valor de la entrada: {self.precio}"


p1 = Pelicula('Avatar', 6000)
peliculas = [p1]


def listaPeliculas():
    for index, pelicula in enumerate(peliculas, start=1):
        print(f'{index}- {pelicula}')
        time.sleep(1)


def boucher(mensaje):
    f = open('boletas.txt', 'a')
    f.write(f"{mensaje}\n")
    f.close()


def comprador():
    while True:
        nombre = input('Ingresa tu nombre: ')
        duoc = input('Eres alumno duoc: ')
        if duoc== 'SI':
            alumno = {
                'nombre': nombre,
                'DUOC': duoc,
                'descuento':0.3
            }
        else:
            alumno = {
                'nombre': nombre,
                'DUOC': duoc,
                'descuento':0
            }
        return alumno


def comprarEntrada():
    listaPeliculas()
    global num_boleta
    num_boleta += 1
    seleccion = int(input('Que pelicula quieres ver: '))
    pelicula_elegida = peliculas[seleccion-1]
    print('Selecciona tu asiento: ')
    asientos_sala = pelicula_elegida.asientos
    print(asientos_sala)
    while True:
        filas, columnas = asientos_sala.shape
        fila = int(input('Elige la fila de tu asiento: '))
        columna = int(input('Elige la columna de tu asiento: '))
        if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
            print('asiento invalido')
        elif asientos_sala[fila][columna] == 'X':
            print('Asiento ocupado')
        else:
            asientos_sala[fila][columna] = 'X'
            b_fila = fila
            b_columna = columna
            break
    cliente = comprador()
    descuento_alumno=cliente['descuento']
    descuento_final=pelicula_elegida.precio*descuento_alumno
    precio_final=pelicula_elegida.precio-descuento_final
    boleta = f""" ************************
***    CINEDUOC  #1  ***
************************
N° BOLETA {num_boleta}
PELICULA: {pelicula_elegida.nombre}
Precio Normal - ${pelicula_elegida.precio}
COMPRADOR:{cliente['nombre']}
DESCUENTO:{cliente['descuento']*100}
NUMERO ASIENTO: FILA {b_fila}, COLUMNA {b_columna}
PRECIO FINAL: {round(precio_final)}
"""
    boucher(boleta)


def verBoletas():
    try:
        f = open('boletas.txt', 'r')
        boletas_importadas = f.read()
        print(boletas_importadas)
    except FileNotFoundError:
        print('Archivo no encontrado')


while True:
    for index, opcion in enumerate(menu, start=1):
        print(f"[{index}] {opcion}")
    opc = int(input('Que deseas hacer: '))
    match opc:
        case 1:
            comprarEntrada()
        case 2:
            verBoletas()
        case 3:
            break


# esto era por si pedian la cantidad de compras totales
asientos_ocupados = np.count_nonzero(p1.asientos == 'X')
