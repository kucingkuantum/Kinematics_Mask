# -*- coding: utf-8 -*-

"""
Created on Mon Apr  6 23:15:13 2020

@author: syahr
"""

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
# dire = 'C:/ffmpegadd/ffmpeg/bin/ffmpeg.exe'
# plt.rcParams['animation.ffmpeg_path'] = dire # Add the path of ffmpeg here!!


v0 = 4.5
h = 1.6
g = 9.8
theta = 0
def data_gen():
            
    v0y = v0*np.sin(theta)
    v0x = v0*np.cos(theta) 
    

    for cnt in range(70):
        t = cnt / 100
        x = v0x*t
        y =  h +  v0y*t - 0.5*g*t**2
        yield x,y


def init():
    ax.set_ylim(0, 2.5)
    ax.set_xlim(0, 3)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
ax.text(0.22, 2.1, '$v_0 = $'+str(v0)+' m/s', fontsize=14)
ax.set_xlabel('x(m)',fontsize=14)
ax.set_ylabel('high (m)',fontsize=14)
ax.set_title('Without Mask',fontsize=14)
line, = ax.plot([], [],'.', lw=2,color='red')
ax.grid()
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=30,
                              repeat=True, init_func=init)
# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save('Withoutmasker.mp4', writer=writer)
plt.show()
