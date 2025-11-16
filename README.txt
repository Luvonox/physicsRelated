This contains python projects for quantum physics internships. (basic physics for now)

As of 16/11/2025 There is a Projectile Motion simulator, which graphs a projectile position based on the velocity (taken through input) and the angle (taken through input) It converts the angle to radians, and simulates the motion
for as many seconds as the user wants. It uses the formulas:

horizontal_motion = v0 * math.cos(angle_rad) * time
vertical_motion = v0 * math.sin(angle_rad) * time - 0.5 * g * time**2

There is Also an orbit simulator. It includes 3 planets, jupiter, mars, and earth. These each have different distances from the sun, different speeds, and different theta values. Using the formulas:
r * cos(theta) (x value)
r * sin(theta) (y value)

I was able to plot the position of the planets after a certain time period of revolving around the sun (input taken for position)



