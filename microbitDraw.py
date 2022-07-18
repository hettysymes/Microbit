#microbitDraw
import serial
import time
import matplotlib.pyplot as plt
import re

GRAPH_PAUSE = 0.01
DATA_FREQ = 0.02

class SerialIn:
    def __init__(self):
        self.ser = serial.Serial('COM5', 115200, timeout=1)
        time.sleep(GRAPH_PAUSE)

    def getNext(self):
        while True:
            # gets acceleration readings
            line = self.ser.readline()
            if line:
                ret = re.split(",|\r\n", line.decode())
                return [int(ret[0]), int(ret[1]), int(ret[2]), int(ret[3])]
    
    def close(self):
        self.ser.close()

class Graph:
    def __init__(self, graph, title, xLabel, yLabel):
        self.graph = graph
        self.graph.set_title(title)
        self.graph.set_xlabel(xLabel)
        self.graph.set_ylabel(yLabel)
        self.xs = []
        self.ys = []
    
    def addPoint(self, x, y):
        self.xs.append(x)
        self.ys.append(y)

    def replot(self):
        self.graph.plot(self.xs, self.ys)

class Gui:
    def __init__(self):
        _, axis = plt.subplots(2, 1)
        self.xAccGraph = Graph(axis[0], "X acceleration", "time", "x acceleration")
        self.yAccGraph = Graph(axis[1], "Y acceleration", "time", "y acceleration")
        plt.tight_layout()
        self.refreshDrawing()
    
    def addPoints(self, xAccPoint, yAccPoint):
        self.xAccGraph.addPoint(xAccPoint[0], xAccPoint[1])
        self.yAccGraph.addPoint(yAccPoint[0], yAccPoint[1])
        self.refreshDrawing()

    def refreshDrawing(self):
        self.xAccGraph.replot()
        self.yAccGraph.replot()
        plt.pause(GRAPH_PAUSE)

si = SerialIn()
gui = Gui()
while True:
    data = si.getNext()
    print(data)
    _, xAcc, yAcc, t = data
    gui.addPoints((t, xAcc), (t, yAcc))
    time.sleep(DATA_FREQ)

"""
class Gui:
    def __init__(self):
        self.xs = [0]
        self.ys = [0]
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title('Microbit drawing') 
        self.refreshDrawing()
    
    def addPoint(self, x, y):
        self.xs.append(x)
        self.ys.append(y)
        self.refreshDrawing()

    def refreshDrawing(self):
        plt.plot(self.xs, self.ys)
        plt.pause(GRAPH_PAUSE)
"""

"""
coord = [0, 0]
s = [0, 0]
u = [0, 0]
v = [0, 0]
a = [0, 0]
tPrev = -1
si = SerialIn()
gui = Gui()
while True:
    [i, a[0], a[1], tNow] = si.getNext()
    print(i, a)
    if (tPrev == -1):
        tPrev = tNow
        time.sleep(DATA_FREQ)
        continue
    print(i, a)
    t = tNow-tPrev
    tPrev = tNow
    v[0] = u[0] + a[0]*t
    v[1] = u[1] + a[1]*t
    s[0] = ((v[0] + u[0])/2) * t
    s[1] = ((v[1] + u[1])/2) * t
    u = list(v)
    coord[0] += s[0]
    coord[1] += s[1]
    gui.addPoint(coord[0], coord[1])
    time.sleep(DATA_FREQ)
"""

"""
si = SerialIn()
gui = Gui()
for i in range(100):
    data = si.getNext()
    print(f"{data[0]}, {data[1]}")
    gui.addPoint(data[0], data[1])
    time.sleep(0.2)
"""