import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


p_cr = 42
N = 45
q = 1
t1 = 28
t2 = 22
p1 = 8.1
p2 = 10.5

a1 = p_cr / (t1 * t1 * p1 * p1 * N * q)
a2 = p_cr / (t2 * t2 * p2 * p2 * N * q)
b = p_cr / (t1 * t1 * t2 * t2 * p1 * p1 * p2 * p2 * N * q)
c1 = (p_cr - p1) / (t1 * p1)
c2 = (p_cr - p2) / (t2 * p2)

def solve_for_init(x0, fig_name):
    def ode(x, t):
        m1, m2, ps = x
        new_m0 = m1 - (b / c1 + ps) * m1 * m2 - a1 / c1 * m1 * m1
        new_m1 = c2 / c1 * m2 - (b / c1) * m1 * m2 - a2 / c1 * m2 * m2
        return new_m0, new_m1, ps

    t = np.linspace(0, 30, round(30 / 0.01))

    sol = odeint(ode, x0, t)
    print(sol)
    plt.plot(t, sol[:, 0], color='red', label='Первая фирма')
    plt.plot(t, sol[:, 1], color='blue', label='Вторая фирма')
    plt.xlabel('Время')
    plt.ylabel('Деньги')
    plt.legend(loc='best')
    plt.savefig(f'source/lab07_{fig_name}')
    plt.show()

plt.title('Случай 1')
solve_for_init([7.2, 9.1, 0], fig_name='case1.png')

plt.title('Случай 2')
solve_for_init([7.2, 9.1, 0.00048], fig_name='case2.png')



