import os

class Determinante():
    def __init__(self):
        self.matriz = [[[], [], []], [[], [], []], [[], [], []]]
        for x in range(3):
            for y in range(3):
                os.system('cls')
                for i in self.matriz:
                    print(*i)
                self.matriz[x][y] = int(input(f'Ingrese el valor de la posición {x+1}, {y+1}: '))
        print(f'El determinante de la matriz es: {self.calcular()}')
    def calcular(self):
        os.system('cls')
        for i in self.matriz:
            print(*i)
        print('\n')
        return self.matriz[0][0] * self.matriz[1][1] * self.matriz[2][2] + self.matriz[0][1] * self.matriz[1][2] * self.matriz[2][0] + self.matriz[0][2] * self.matriz[1][0] * self.matriz[2][1] - self.matriz[0][2] * self.matriz[1][1] * self.matriz[2][0] - self.matriz[0][1] * self.matriz[1][0] * self.matriz[2][2] - self.matriz[0][0] * self.matriz[1][2] * self.matriz[2][1]

# Determinante()