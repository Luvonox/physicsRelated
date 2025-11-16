import matplotlib.pyplot as plt
import math

v0 = float(input("What is the initial velocity? "))
a0 = int(input("What is the angle of projectile launch? "))
simulationLength = int(input("How many seconds do you want to see? "))
angle_rad = math.radians(a0)

time = 0
timestep = 0.5
endTime = simulationLength / 2
g = 9.8

dataLogHorizontal = []
dataLogVertical = []

while time < endTime:
	horizontal_motion = v0 * math.cos(angle_rad) * time
	vertical_motion = v0 * math.sin(angle_rad) * time - 0.5 * g * time**2
	rounded_horizontal_motion = round(horizontal_motion, 2)
	rounded_vertical_motion = round(vertical_motion, 2)
	dataLogHorizontal.append(rounded_horizontal_motion)
	dataLogVertical.append(rounded_vertical_motion)
	time += timestep

plt.plot(dataLogHorizontal, dataLogVertical)
plt.title("Projectile motion graph")
plt.xlabel("Projectile distance (x)")
plt.ylabel("Projectile height (y)")
plt.grid(True)
plt.show()
