# -*- coding: utf-8 -*-

"""
Created on Mon Apr  6 23:15:13 2020

@author: syahr
"""

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
dire = 'C:/ffmpegadd/ffmpeg/bin/ffmpeg.exe'
# dire = 'C:/Users/syahrAnaconda3/pkgs/plotly-orca-1.2.1-1/orca_app'
plt.rcParams['animation.ffmpeg_path'] = dire # Add the path of ffmpeg here!!


v0 = 4.5
h = 1.6
g = 9.8
eres= 0.8
    


def data_gen():
    for cnt in range(80):
        t = cnt / 5000
        theta = 0
        v0x = v0*np.cos(theta) 
        x = v0x*t
        if x<0.03:
            
            v0y = v0*np.sin(theta)
           
            y =  h +  v0y*t - 0.5*g*t**2
            y0 = y.copy()
            x0 = x.copy()
            t0 = t
            # print(x0,y0,t0)
        else:
            theta = -np.radians(180-25)
            v0x = eres*v0*np.cos(theta) 
            v0y = eres*v0*np.sin(theta)
            x = x0 + v0x*(t-t0)
            y = y0 + v0y*(t-t0) - 0.5*g*(t-t0)**2 
            
        yield 100*x,y


def init():
    ax.set_ylim(1, 2)
    ax.set_xlim(0, 3)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
ax.text(0.22, 1.3, '$v_0 = $'+str(v0)+' m/s', fontsize=14)
# ax.text(0.01, 1.75, 'Mulut', fontsize=14)
ax.set_xlabel('x(cm)',fontsize=14)
ax.set_ylabel('high (m)',fontsize=14)
ax.set_title('With Mask',fontsize=14)
line, = ax.plot([], [],'o', lw=1,color='blue')
ax.grid()
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 1.5*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=100,
                              repeat=True, init_func=init)
ani.save('masker.mp4', writer=writer)
plt.show()