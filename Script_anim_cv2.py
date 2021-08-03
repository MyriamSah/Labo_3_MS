# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 19:28:18 2021

@author: Myriam
"""
import numpy as np
import pandas as pd
#import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2
#from IPython import display

#Importer les coordonnées
Coord = pd.read_csv (r'C:\Users\Myriam\Excel_pr_python\New_Coord.csv')
Coord = np.array(Coord)
X = Coord[:,0]
Y = Coord[:,1]
print(Y.shape)

X2 = [60,60,250,450,450]
Y2 = [60,310,190,60,310]

fig= plt.figure()
dots = plt.plot(X2,Y2, "bo", markersize=30)
plt.axis("scaled")
plt.xlim(0,700)
plt.ylim(0,500)


fig.canvas.draw() # Draw the image on the canvas (i.e. apply the functions above), without displaying it
img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='') # Not sure how, but it sends the pixel values of the canvas to an array (called img)
img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,)) # Reshape the array so it's 3d (height X width X layer(color))
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR) # Convert color to opencv's default BGR

frame = img
height, width, layers = frame.shape
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter(r'C:/Users/Myriam/Desktop/Université_Myriam/8esession/PSY3009/Anim_Nouv_2.mp4', fourcc, 100, (width,height))

x_data = []
y_data = []

fig= plt.figure()
for i in range(30000):
        x_data.append(X[i])
        y_data.append(Y[i])
        if x_data[-1] == 0 and y_data[-1] == 0:
            x_data.clear()
            y_data.clear()
        
        lines = plt.plot(x_data, y_data, color = "orange", linewidth = 5)
        line = lines[0]
        dots = plt.plot(X2,Y2, "bo", markersize=30)
        plt.axis("scaled")
        plt.xlim(0,700)
        plt.ylim(0,500)
        
 
        fig.canvas.draw() # Draw the image on the canvas (i.e. apply the functions above), without displaying it
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='') # Not sure how, but it sends the pixel values of the canvas to an array (called img)
        img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,)) # Reshape the array so it's 3d (height X width X layer(color))
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        
        video.write(img)  
        fig.clear()
        
cv2.destroyAllWindows()
video.release()
