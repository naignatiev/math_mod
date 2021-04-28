from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np


a = -0.38
b = -0.043
c = -0.36
d = -0.052

t = np.linspace(0, 200, round(200 / 0.1))

def draw_circle(x0, y0):
    def ode(y, t):
        x, y = y
        return -a * x + b * x * y, c * y - d * x * y

    sol = odeint(ode, [x0, y0], t)
    print(sol)
    plt.plot(sol[:, 0], sol[:, 1])
    plt.scatter(x0, y0, color='red')
    return sol[:, 0], sol[:, 1]

x, y = draw_circle(6, 23)
draw_circle(8, 18)
draw_circle(6, 15)
draw_circle(6.5, 12)
draw_circle(7, 10)
draw_circle(c / d, a / b)
plt.xlabel('Число жертв')
plt.ylabel('Число хищников')
plt.title('Модель хищник жертва')
plt.savefig('source/lab04_fig.png')
plt.show()

plt.plot(t, x, color='red', label='Жертва')
plt.plot(t, y, color='green', label='Хищник')
plt.title('Зависимость числа особей от времени')
plt.xlabel('Время')
plt.ylabel('Количество особей')
plt.legend(loc='best')
plt.savefig('source/lab04_graph.png')
plt.show()
