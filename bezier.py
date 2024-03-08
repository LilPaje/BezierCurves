import numpy as np
import matplotlib.pyplot as plt
import lib

N_POINTS = 4

t_points = np.arange(0, 1, 0.01)
control_points = np.random.rand(N_POINTS, 3)

curve = lib.curve(t_points, control_points)

figure = plt.figure(figsize=(10, 10), dpi=128)

ax = figure.add_subplot(111, projection='3d')
ax.plot(curve[:, 0], curve[:, 1], curve[:, 2])
ax.plot(control_points[:, 0], control_points[:, 1], control_points[:, 2], 'o:')

plt.show()
