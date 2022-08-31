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
DATA_FREQ = 25

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
            x, y, penDown, clear =  [int(ret[0]), int(ret[1]), int(ret[2]), int(ret[3])]
        except:
            return FAILURE
        return (True, (-x, y, penDown, clear))
    
    def close(self):
        self.ser.close()

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle("PyQtGraph")
        self.setGeometry(100, 100, 600, 500)
        self.normalPen = pg.mkBrush(30, 255, 30, 255)
        self.cursorPen = pg.mkBrush(255, 30, 30, 255)
        self.serial = SerialConn()
        self.data = []
        self.UiComponents()

    def UiComponents(self):
        widget = QWidget()
        label = QLabel("Drawing console")
        label.setWordWrap(True)
        plot = pg.plot()
        self.scatter = pg.ScatterPlotItem(size=10, brush=self.normalPen)
        plot.addItem(self.scatter)
        plot.setRange(xRange=[-70, 70], yRange=[-70, 70])
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
        self.scatter.setData(self.data)

    def update_plot_data(self):
        (success, (x, y, penDown, clear)) = self.serial.readData()
        if not success: return
        if clear:
            self.data = []
        elif self.data:
            if penDown:
                self.data[-1]['brush'] = self.normalPen
            else:
                self.data.pop()
        self.data.append({'pos': (x, y), 'brush': self.cursorPen})
        self.updateScatter()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())