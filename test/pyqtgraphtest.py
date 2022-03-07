"""
Various methods of drawing scrolling plots.
"""

from time import perf_counter

import numpy as np

import pyqtgraph as pg

win = pg.GraphicsLayoutWidget(show=True)
win.setWindowTitle('pyqtgraph example: Scrolling Plots')


# 1) Simplest approach -- update data in the array such that plot appears to scroll
#    In these examples, the array size is fixed.
p1 = win.addPlot()
p2 = win.addPlot()
data1 = np.random.normal(size=300)
curve1 = p1.plot(data1)
curve2 = p2.plot(data1)
ptr1 = 0
def update1():
    global data1, ptr1
    data1[:-1] = data1[1:]  # shift data in the array one sample left
                            # (see also: np.roll)
    data1[-1] = np.random.normal()
    curve1.setData(data1)
    
    ptr1 += 1
    curve2.setData(data1)
    curve2.setPos(ptr1, 0)
    

# 2) Allow data to accumulate. In these examples, the array doubles in length
#    whenever it is full. 



# update all plots
def update():
    update1()
timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(20)

if __name__ == '__main__':
    pg.exec()