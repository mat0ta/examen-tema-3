from ejercicio_1.torres import insercion
from ejercicio_2.sarrus import Determinante
from ejercicio_3.starwars import Vehiculos
from ejercicio_5.codificacion import Encriptacion

eleccion = int(input('''
    1. Torres de Hanoi
    2. Determinante de una matriz
    3. Vehiculos de Star Wars
    4. Encriptacion
    5. Salir
    '''))

while eleccion != '5':
    if eleccion == 1:
        insercion()
    elif eleccion == 2:
        Determinante()
    elif eleccion == 3:
        Vehiculos().mostar_info('Millennium Falcon')
        Vehiculos().mostar_info('Death Star')

        Vehiculos().mostrar_mas_pasajeros()

        Vehiculos().mostrar_mas_tripulacion()

        Vehiculos().mostrar_vehiculos_at()

        Vehiculos().mostrar_vehiculos_con_6()

        Vehiculos().mostrar_extremos()
    elif eleccion == 4:
        Encriptacion('Es una trampa').encriptar()
    else:
        print('Opcion incorrecta')
    eleccion = int(input('''
        1. Torres de Hanoi
        2. Determinante de una matriz
        3. Vehiculos de Star Wars
        4. Encriptacion
        5. Salir
        '''))