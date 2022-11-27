

# Example

# c = cost_order = 1000
# v = intensity = 500
# K = order_depense = 10
# s = storage_depense = 0.4


import matplotlib.pyplot as plt
import numpy as np


# Модель Уилсона
def Wilson():
    #  Входные данные
    v = float(input('Введите интенсивность (скорость): '))
    s = float(input('Введите затраты на хранение запаса: '))
    K = float(input('Затраты на осуществления заказа: '))
    Td = float(input('Время доставки: '))

    #  Расчетные данные
    Q = ((2 * K * v) / s) ** 0.5
    L = K * (v/Q) + s * Q/2
    Tau = Q / v
    H0 = v * Td

    #  Вывод результатов
    print('Модель Уилсона')
    print('Q = ', Q)
    print('L = ', L)
    print('Tau = ', Tau)
    print('H0 = ', H0)

    print('График зависимости L от Q')

    Q_array = np.arange(0, Q, 0.01*Q)
    L_array = []

    for i in range(len(Q_array)):
        L_array.append(K * (v/Q_array[i]) + s * Q_array[i]/2)

    plt.plot(Q_array, L_array)
    plt.show()
    return Q, L, Tau, H0


# Модель управления запасами, учитывающая скидки
def discount() -> tuple:

    K = float(input('Введите издержку заказа: '))
    v = float(input('Введите интенсивность: '))
    s = float(input('Введите издержку хранения: '))
    c = float(input('Введите издержку заказа: '))

    Q = ((2 * K * v) / s) ** 0.5
    tay = Q / v
    L = K * (v/Q) + s * Q/2 + c*v

    print('Модель Скидок')
    print('Q = ', round(Q, 2))
    print('L = ', round(L, 2))
    print('Tau = ', round(tay, 2))

    print('График зависимости L от Q')
    Q_array = np.arange(0, Q, 0.01*Q)
    L_array = []

    for i in range(len(Q_array)):
        L_array.append(K * (v/Q_array[i]) + s * Q_array[i]/2 + c*v)

    plt.plot(Q_array, L_array)
    plt.show()

    return (round(Q), round(tay), round(L))


print('Модель Уилсона', 'Скидки', "Модель Данияр", sep='\t')
choice = str(input('Выберите модель: '))
    
if choice == 'Скидки':
    discount()
elif choice == 'Модель Уилсона':
    Wilson()
elif choice == "Модель Данияр":
    print(int(input('Input K: ')) * (int(input('Input v: ')) / ((2 * int(input('Input K: ')) * int(input('Input v: '))) / float(input('Input s: '))) ** .5) + float(input('Input s: ')) * (((2 * int(input('Input K: ')) * int(input('Input v: '))) / float(input('Input s: '))) ** .5 / 2) + int(input('Input c: ')) * int(input('Input v: ')))


print('Проверьте введенные данные')










