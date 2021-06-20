import matplotlib.pyplot as plt
import numpy as dt
import pylab

V = 1e+6
r = 8.5
R = 18
L = 26
E_m = 1.6/9.1 * 1e12
E = E_m * V**2 /L**2 * (R-r)
l = dt.linspace(0, 11, 100)
x = dt.linspace(0, 10, 100)
t = l / V
Y_x = (R - r) /2 +  E * E_m * x**2 / (2.0 * V**2)
v_y_t = E * E_m * t
y_t = (R-r)/2 + E * E_m * t**2 / 2.0
a_t = [E * E_m for _ in t]

pylab.subplot (2, 2, 1)
pylab.title ("Y(x)")
pylab.plot(x, Y_x)

pylab.subplot (2, 2, 3)
pylab.title ("V_y(t)")
pylab.plot(t, v_y_t, alpha=0.8)

pylab.subplot (2, 2, 2)
pylab.title ("Y(t)")
pylab.plot(t, y_t)

pylab.subplot (2, 2, 4)
pylab.title ("A(t)")
pylab.plot(t, a_t)

plt.show()
