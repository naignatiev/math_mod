import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


x0 = 0.1
y0 = 1.1


def solve_for_init(w0, g, f, fig_name, n_time):
    t = np.linspace(0, n_time, round(n_time / 0.05))

    def ode(y, t):
        x, y = y
        return y, -w0 * w0 * x - g * y - f(t)
    sol = odeint(ode, [x0, y0], t)
    print(sol)
    plt.xlabel('x показатель осциллятора')
    plt.ylabel('Скорость (y)')
    plt.plot(sol[:, 0], sol[:, 1])
    plt.savefig(f'source/lab03_{fig_name}')
    plt.show()


plt.title('Колебания без затуханий и без действий внешней силы')
solve_for_init(w0=3.7, g=0, f=lambda x: 0, fig_name='plot1.png', n_time=63)

plt.title('Колебания с затуханиями, но без действия внешней силы')
solve_for_init(w0=3, g=10, f=lambda x: 0, fig_name='plot2.png', n_time=63)

plt.title('Колебания с затуханиями и действием внешней силы')
solve_for_init(w0=3, g=11, f=lambda x: 0.9 * np.sin(0.9 * x), fig_name='plot3.png', n_time=63)

# plt.title('Колебания с затуханиями и действием хорошей внешней силы')
# solve_for_init(w0=3, g=11, f=lambda x: -0.9 * np.sin(0.9 * x), fig_name='plot4.png', n_time=400)
