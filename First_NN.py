import numpy as np


def onestep(x):  # активация
    b = 5
    if x >= b:
        return 1
    else:
        return 0


class Neuron:  # создание класса нейрон
    def __init__(self, w):
        self.w = w

    def y(self, x):  # Сумматор
        s = np.dot(self.w, x)  # сумма входов
        return onestep(s)  # функция активации - (функция Хевисайда(y=f(S))


Xi = np.array([1, 0, 0, 1])  # значение входов
Wi = np.array([5, 4, 1, 1])  # значение весов входов
n = Neuron(Wi)  # создание объекта из класса
print('Y =', n.y(Xi))  # обращение к нейрону
