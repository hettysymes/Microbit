#microbitDraw
import serial
import time
import matplotlib.pyplot as plt
import re

COM = 'COM5'
BAUD_RATE = 115200
TIMEOUT = 1
GRAPH_PAUSE = 0.001
DATA_FREQ = 0.01
MAX_ITERATIONS = 1000

class Serial:
    def __init__(self):
        self.ser = serial.Serial(COM, BAUD_RATE, timeout=TIMEOUT)
    
    def readline(self):
        return self.ser.readline().decode("utf-8")
    
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

print("Prog started")
s = Serial()
gui = Gui()
for i in range(MAX_ITERATIONS):
    try:
        line = s.readline()
    except:
        continue
    if not line:
        time.sleep(GRAPH_PAUSE) # Sleep briefly
        continue
    ret = re.split(",|\n", line)
    print(ret)
    _, xAcc, yAcc, t =  [int(ret[0]), int(ret[1]), int(ret[2]), int(ret[3])]
    gui.addPoints((t, xAcc), (t, yAcc))
    time.sleep(GRAPH_PAUSE)
s.close()