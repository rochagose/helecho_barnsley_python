import matplotlib.pyplot as plt
import random

#CONSTANTES DE TRANSFORMACION
TRANSFORMACIONES = [
    (0.00, 0.00, 0.00, 0.16, 0.00, 0.00, 0.01),  
    (0.85, 0.04, -0.04, 0.85, 0.00, 1.60, 0.85), 
    (0.20, -0.26, 0.23, 0.22, 0.00, 1.60, 0.07), 
    (-0.15, 0.28, 0.26, 0.24, 0.00, 0.44, 0.07)  
]

#Variables
x = 0
y = 0
pts = []

#Calcular los puntos del fractal
for _ in range (20000):
    r = random.random()
    for(a, b, c, d, e, f, p) in TRANSFORMACIONES:
        if r < p:
            x, y = a * x + b * y + e, c * x + d * y + f
            break
        r -= p
    pts.append((x, y))

#Dibujar el fractal
x_vals, y_vals = zip(*pts)
plt.figure(figsize=(6, 8))
plt.scatter(x_vals, y_vals, s=0.2, color="green")
plt.axis("off")
plt.show()
