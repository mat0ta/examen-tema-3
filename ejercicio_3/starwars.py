import csv
import os

class Vehiculos():
    def __init__(self):
        self.naves = {}
        with open('./ejercicio-3/vehiculos.csv', 'r') as archivo:
            lector = csv.DictReader(archivo, delimiter=';')
            for linea in lector:
                self.naves[linea['Name']] = linea
    def mostar_info(self, nave):
        print(f"Nombre: {self.naves[nave]['Name']}, Longitud: {self.naves[nave]['Length']}, Tripulacion Maxima: {self.naves[nave]['Crew']}, Pasajeros Maximos: {self.naves[nave]['Passengers']}")
    def mostrar_mas_pasajeros(self):
        top_5 = sorted(self.naves.items(), key=lambda x: int(x[1]['Passengers']), reverse=True)[:5]
        returned = []
        for i in top_5:
            returned.append(i[1]['Name'])
        print('Los vehiculos con más capacidad de Pasajeros son: ' + ', '.join(returned))
    def mostrar_mas_tripulacion(self):
        top_5 = sorted(self.naves.items(), key=lambda x: int(x[1]['Crew']), reverse=True)[:5]
        returned = []
        for i in top_5:
            returned.append(i[1]['Name'])
        print('Los vehiculos con más capacidad de Tripulacion son: ' + ', '.join(returned))
    def mostrar_vehiculos_at(self):
        returned = []
        for i in self.naves:
            if 'AT' in self.naves[i]['Name']:
                returned.append(self.naves[i]['Name'])
        print('Los vehiculos con AT en su nombre son: ' + ', '.join(returned))
    def mostrar_vehiculos_con_6(self):
        returned = []
        for i in self.naves:
            if int(self.naves[i]['Passengers']) >= 6:
                returned.append(self.naves[i]['Name'])
        print('Los vehiculos que pueden llevar 6 o mas pasajeros son: ' + ', '.join(returned))
    def mostrar_extremos(self, menor = [], mayor = [], n = 0):
        for i in self.naves:
            if menor == []:
                menor = self.naves[i]
            if mayor == []:
                mayor = self.naves[i]
            if float(self.naves[i]['Length']) <= float(menor['Length']):
                menor = self.naves[i]
            elif float(self.naves[i]['Length']) >= float(menor['Length']):
                mayor = self.naves[i]
        if n == 0:
            Vehiculos.mostrar_extremos(self, menor, mayor, 1)
        print('La nave más grande es: ' + mayor['Name'] + ' y la más pequeña es: ' + menor['Name'])

# Vehiculos().mostar_info('Millennium Falcon')
# Vehiculos().mostar_info('Death Star')

# Vehiculos().mostrar_mas_pasajeros()

# Vehiculos().mostrar_mas_tripulacion()

# Vehiculos().mostrar_vehiculos_at()

# Vehiculos().mostrar_vehiculos_con_6()

# Vehiculos().mostrar_extremos()