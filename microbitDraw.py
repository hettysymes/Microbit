#microbitDraw
import serial
import time
import matplotlib.pyplot as plt

COM = 'COM5'
BAUD_RATE = 115200
TIMEOUT = 1
GRAPH_PAUSE = 0.001
DATA_FREQ = 5
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
        #self.graph.set_ylim([-100, 300])
        self.xs = []
        self.ys = []
    
    def addPoint(self, x, y):
        self.xs.append(x)
        self.ys.append(y)

    def replot(self):
        self.graph.plot(self.xs, self.ys)

class Gui:
    def __init__(self):
        _, axis = plt.subplots(1, 1)
        self.graph = Graph(axis, "Plot", "x-axis", "y-axis")
        plt.tight_layout()
        self.refreshDrawing()
    
    def addPoints(self, point):
        self.graph.addPoint(point[0], point[1])
        self.refreshDrawing()

    def refreshDrawing(self):
        self.graph.replot()
        plt.pause(GRAPH_PAUSE)

print("Graphing started")
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
    ret = line.strip().split(",")
    #print(ret)
    x, y =  [int(ret[0]), int(ret[1])]
    gui.addPoints((x, -y))
    time.sleep(GRAPH_PAUSE)
s.close()