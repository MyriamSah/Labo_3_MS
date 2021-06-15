# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:22:16 2021

@author: Myriam
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython import display

Coord = pd.read_csv (r'C:\Users\Myriam\Excel_pr_python\Coord_pv.csv')
Coord = np.array(Coord)
print(Coord.shape)

X = Coord[:,0]
Y = Coord[:,1]
print(X[1])

X2 = [100,100,350,600,600]
Y2 = [100,420,260,100,420]

fig= plt.figure()
lines = plt.plot([], color = "orange", linewidth = 5)
line = lines[0]
dots = plt.plot(X2,Y2, "bo", markersize=30)
plt.axis("scaled")
plt.xlim(0,700)
plt.ylim(0,500)

x_data = []
y_data = []

def animate(i):
    x_data.append(X[i])
    y_data.append(Y[i])
    if x_data[-1] == 0 and y_data[-1] == 0:
        x_data.clear()
        y_data.clear()
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    dots
    return line
          
anim = FuncAnimation(fig, animate, frames=2925, interval=1, repeat=False)
anim.save("FileanimT.mp4", fps=36, bitrate = -1)