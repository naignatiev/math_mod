import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

N = 17845
i0 = 199
r0 = 35
s0 = N - i0 - r0


def solve_for_init(a, b, I, fig_name):
    def ode(y, t):
        s, i, r = y
        if i > I:
            return -a * s, a * s - b * i, b * i
        else:
            return 0, -b * i, b * i

    t = np.linspace(0, 200, round(200 / 0.1))

    sol = odeint(ode, [s0, i0, r0], t)
    print(sol)
    last_index = 0
    while sol[last_index][1] >= 1 and last_index + 1 < len(t):
        last_index += 1

    plt.plot(t[:last_index], sol[:last_index, 0], color='blue', label='Еще не болели')
    plt.plot(t[:last_index], sol[:last_index, 1], color='red', label='Инфицированные')
    plt.plot(t[:last_index], sol[:last_index, 2], color='green', label='С иммунитетом')
    plt.legend(loc='best')
    plt.xlabel('Время')
    plt.ylabel('Количество человек')
    plt.savefig(f'source/{fig_name}')
    plt.show()


plt.title('Случай i0>I, a=0.2, b=0.1')
solve_for_init(0.2, 0.1, I=198, fig_name='lab05_bad.png')

plt.title('Случай i0=I, a=0.2, b=0.1')
solve_for_init(0.2, 0.1, I=199, fig_name='lab05_good.png')

plt.title('Случай i0>I, a=0.1, b=1.2')
solve_for_init(0.1, 1.2, I=198, fig_name='lab05_mean.png')
