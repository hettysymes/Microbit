#microbitDraw
import serial

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from PyQt5.QtGui import *
import sys

COM = 'COM5'
BAUD_RATE = 115200
TIMEOUT = 1
DATA_FREQ = 0.001

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

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle("PyQtGraph")
        self.setGeometry(100, 100, 600, 500)
        self.serial = SerialConn()
        self.xs = []
        self.ys = []
        self.UiComponents()

    def UiComponents(self):
        widget = QWidget()
        label = QLabel("Drawing console")
        label.setWordWrap(True)
        plot = pg.plot()
        self.scatter = pg.ScatterPlotItem(size=10, brush=pg.mkBrush(30, 255, 35, 255))
        plot.addItem(self.scatter)
        layout = QGridLayout()
        label.setMinimumWidth(130)
        widget.setLayout(layout)
        layout.addWidget(label, 1, 0)
        layout.addWidget(plot, 0, 1, 3, 1)
        self.setCentralWidget(widget)
        self.updateScatter()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(DATA_FREQ)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def updateScatter(self):
        self.scatter.setData(self.xs, self.ys)

    def update_plot_data(self):
        (success, data) = self.serial.readData()
        if success:
            self.xs.append(data[0])
            self.ys.append(data[1])
        self.updateScatter()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())