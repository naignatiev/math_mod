from scipy.integrate import odeint
from scipy.constants import pi
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


n = 5.1
k = 20.2
fi = pi / 4

f = lambda r, theta: r / np.sqrt(25.01)
f2 = lambda t: np.tan(fi) * t


def solve_for_init(r0, theta0, times=20, plt_name='untitled'):
    thetas = np.linspace(theta0, theta0 + 2 * pi, 100)
    rs = odeint(f, r0, thetas)
    plt.polar([fi] * times, [f2(t) for t in range(0, times)], color='red')
    plt.plot(thetas, rs, color='blue')
    plt.savefig(f'source/lab01_{plt_name}.png')
    plt.show()


plt.title('Первый случай')
solve_for_init(k / 6.1, 0, 10, plt_name='plt1')

plt.title('Второй случай')
solve_for_init(k / 4.1, -pi, 20, plt_name='plt2')
