#microbitDraw
import serial
import time
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint

COM = 'COM5'
BAUD_RATE = 115200
TIMEOUT = 1
GRAPH_PAUSE = 0.001
DATA_FREQ = 5
MAX_ITERATIONS = 1000

class SerialConn:

    def __init__(self):
        self.ser = serial.Serial(COM, BAUD_RATE, timeout=TIMEOUT)

    def readData(self):
        FAILURE = (False, ())
        try:
            line = self.ser.readline().decode("utf-8")
        except:
            return FAILURE
        if not line:
            return FAILURE
        ret = line.strip().split(",")
        try:
            x, y =  [int(ret[0]), int(ret[1])]
        except:
            return FAILURE
        return (True, (-x, y))
    
    def close(self):
        self.ser.close()

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.serial = SerialConn()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = []
        self.y = []

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(GRAPH_PAUSE)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        (success, data) = self.serial.readData()
        if success:
            self.x.append(data[0])
            self.y.append(data[1])
        self.data_line.setData(self.x, self.y)  # Update the data.

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())




# print("Graphing started")
# s = Serial()
# gui = Gui()
# for i in range(MAX_ITERATIONS):
#     try:
#         line = s.readline()
#     except:
#         continue
#     if not line:
#         time.sleep(GRAPH_PAUSE) # Sleep briefly
#         continue
#     ret = line.strip().split(",")
#     try:
#         x, y =  [int(ret[0]), int(ret[1])]
#     except:
#         time.sleep(GRAPH_PAUSE)
#         continue
#     gui.addPoint((-x, y))
#     time.sleep(GRAPH_PAUSE)
# s.close()