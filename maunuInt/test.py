import numpy as np
import matplotlib.pyplot as plt

N = 5 

a = 0
b = 10

X = np.random.uniform(a, b, size=N)
Y = np.random.uniform(a, b, size=N)
X_PLUS_Y = X + Y

print(X)
print(Y)
print(X_PLUS_Y)

colors = []
for n in X_PLUS_Y:
    n = int(n)
    if n % 2 == 0:
        colors.append('g')
    else:
        colors.append('b')
print(colors)

# my first guess e' zero
max_d = 0
X_12 = [0] * 2
Y_12 = [0] * 2
for i in range(N):
    for j in range(N):
        dx = X[i] - X[j]
        dy = Y[i] - Y[j]
        dist = np.sqrt(dx**2 + dy**2)
        if dist > max_d: # se la mia first guess e' sbagliato la cambio e aggiorno i punti 
            max_d = dist
            X_12[0] = X[i]
            Y_12[0] = Y[i]
            X_12[1] = X[j]
            Y_12[1] = Y[j]

print(X_12)
print(Y_12)


# plot just the points 
for i in range(N):
    plt.scatter(X[i], Y[i], c = colors[i])

# plot the line, se rimane 0,0 comq sarebbe la distanza massima e la plotti)
plt.plot(X_12, Y_12, "r:o")

# show  
plt.show()

