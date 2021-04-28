import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


X0 = 100000
Y0 = 10000

t0 = 0
t_max = 1.5
dt = 0.05


def solve_for_init(x0, y0, a, b, c, h, p, q, plt_name, ode_case, tmax):
    """
    :param x0: Кол-во первого войска
    :param y0: Кол-во второго войска
    :param a: Коэф-т естественных потерь первого в.
    :param b: Коэф-т эффективности второго в.
    :param c: Коэф-т естественных потерь второго в.
    :param h: Коэф-т эфективности первого в.
    :param p: Функция подкрепления 1-го
    :param q: Функция подкрепления 2-го
    :param plt_name: Имя файла
    :return:
    """
    t = np.linspace(t0, t_max, round((t_max - t0) / dt))
    if ode_case == 1:
        def ode(y, t):
            x, y = y
            return -a * x - b * y + p(t), -h * x - c * y + q(t)

    else:
        def ode(y, t):
            x, y = y
            return -a * x - b * y + p(t), -h * x * y - c * y + q(t)

    sol = odeint(ode, [x0, y0], t)
    print(sol)
    last_index = 0
    while sol[last_index][0] > 0 and sol[last_index][1] > 0 and last_index + 1 < len(sol):
        last_index += 1

    plt.plot(t[:last_index], sol[:last_index, 0], color='blue', label='Первая армия')
    plt.plot(t[:last_index], sol[:last_index, 1], color='red', label='Вторая армия')
    plt.legend(loc='best')
    plt.ylabel('Численность армии')
    plt.xlabel('Время')
    plt.savefig(f'source/lab02_{plt_name}')
    plt.show()


plt.title('Модель боевых действий №1 Случай победы синих')
solve_for_init(x0=X0, y0=Y0, a=0.12, b=0.9, c=0.1, h=0.3,
               p=lambda t: abs(np.sin(t)),
               q=lambda t: abs(np.cos(t)), plt_name='model1.png', ode_case=1, tmax=t_max)


plt.title('Модель боевых действий №1 Случай победы красных')
solve_for_init(x0=X0, y0=Y0, a=0.5, b=10, c=0.01, h=0.1,
               p=lambda t: abs(np.sin(t)),
               q=lambda t: abs(np.cos(t)), plt_name='model2.png', ode_case=1, tmax=t_max)

plt.title('Модель боевых действий №2 Случай победы синих')
solve_for_init(x0=X0, y0=Y0, a=0.25, b=0.96, c=0.3, h=0.25,
               p=lambda t: np.sin(2 * t) + 1,
               q=lambda t: np.cos(20 * t) + 1, plt_name='model3.png', ode_case=2, tmax=t_max)

t_max = 10
plt.title('Модель боевых действий №2 Случай победы красных')
solve_for_init(x0=X0, y0=Y0, a=0.2, b=10, c=0.0000001, h=0.0000001,
               p=lambda t: np.sin(2 * t) + 1,
               q=lambda t: np.cos(20 * t) + 1, plt_name='model4.png', ode_case=2, tmax=t_max)


# plt.title('Модель боевых действий из примера')
# solve_for_init(x0=20000, y0=9000, a=0.4, b=0.8, c=0.5, h=0.7,
#                p=lambda t: np.sin(t) + 1,
#                q=lambda t: np.cos(t) + 1, plt_name='test.png')

