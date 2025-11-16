import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


endTime = int(input("How long should the simulation last? "))
time = 0
timeStep = 0.5


planet1 = "mercury"
mercury_theta = 0
mercury_radius = 5
mercury_speed = 0.05

planet2 = "earth"
earth_theta = 0
earth_radius = 10
earth_speed = 0.02

planet3 = "jupiter"
jupiter_theta = 0
jupiter_radius = 15
jupiter_speed = 0.01

#finding positions
positionMercury = []
positionEarth = []
positionJupiter = []

while time < endTime:
    # EARTH
    earthX = earth_radius * math.cos(earth_theta)
    earthY = earth_radius * math.sin(earth_theta)
    positionEarth.append((round(earthX,2), round(earthY,2)))
    earth_theta += earth_speed

    # MERCURY
    mercuryX = mercury_radius * math.cos(mercury_theta)
    mercuryY = mercury_radius * math.sin(mercury_theta)
    positionMercury.append((round(mercuryX,2), round(mercuryY,2)))
    mercury_theta += mercury_speed

    # JUPITER
    jupiterX = jupiter_radius * math.cos(jupiter_theta)
    jupiterY = jupiter_radius * math.sin(jupiter_theta)
    positionJupiter.append((round(jupiterX,2), round(jupiterY,2)))
    jupiter_theta += jupiter_speed

    # advance time
    time += timeStep

x_earth = [i[0] for i in positionEarth]
y_earth = [i[1] for i in positionEarth]
plt.plot(x_earth, y_earth, label = "earth")
plt.scatter(x_earth[-1], y_earth[-1], color='blue', s=50)


x_mercury = [i[0] for i in positionMercury]
y_mercury = [i[1] for i in positionMercury]
plt.plot(x_mercury, y_mercury, label = "mercury")
plt.scatter(x_mercury[-1], y_mercury[-1], color='orange', s=50)

x_jupiter = [i[0] for i in positionJupiter]
y_jupiter = [i[1] for i in positionJupiter]
plt.plot(x_jupiter, y_jupiter, label = "jupiter")
plt.scatter(x_jupiter[-1], y_jupiter[-1], color='green', s=50)

plt.scatter(0, 0, color='yellow', s=200, label='Sun')


plt.axis('equal')
plt.legend()
plt.show()
