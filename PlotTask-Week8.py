import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array(range(0,4))
gpoints = np.array(range(0,4))
ypoints = np.array(range(0,4))

xpoints = xpoints
gpoints = gpoints * gpoints 
ypoints = ypoints * ypoints * ypoints

Fx= xpoints
Gx= gpoints
Yx= ypoints

plt.plot(Fx, Gx, Yx)
plt.show()
