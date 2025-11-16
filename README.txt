This contains python projects for quantum physics internships.

As of 16/11/2025 There is a Projectile Motion simulator, which graphs a projectile position based on the velocity (taken through input) and the angle (taken through input) It converts the angle to radians, and simulates the motion
for as many seconds as the user wants. It uses the formulas:

horizontal_motion = v0 * math.cos(angle_rad) * time
vertical_motion = v0 * math.sin(angle_rad) * time - 0.5 * g * time**2
