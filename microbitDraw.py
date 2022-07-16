#microbitDraw
import serial
import time
import matplotlib.pyplot as plt 

class SerialIn:
    def __init__(self):
        self.ser = serial.Serial('COM5', 115200, timeout=1)
        self.ser.reset_input_buffer()
        time.sleep(2)

    def getNext(self):
        while True:
            # gets acceleration readings
            line = self.ser.readline()
            if line:
                [xStr, yStr] = (line.decode().split(" ")[0]).split(",")
                return [int(xStr), int(yStr)]
    
    def close(self):
        self.ser.close()

class Gui:
    def __init__(self):
        self.xs = []
        self.ys = []
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title('Microbit acceleration') 
        self.refreshDrawing()
    
    def addPoint(self, x, y):
        self.xs.append(x)
        self.ys.append(y)
        self.refreshDrawing()

    def refreshDrawing(self):
        plt.plot(self.xs, self.ys)
        plt.pause(0.05)


si = SerialIn()
gui = Gui()
for i in range(100):
    data = si.getNext()
    print(f"{data[0]}, {data[1]}")
    gui.addPoint(data[0], data[1])
    time.sleep(0.2)