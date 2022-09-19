# MicroBit Drawing project
 Uses the MicroBit accelerometer information to draw images, with button A used to clear the canvas and button B used to switch between 'pen up' and 'pen down' modes. The information from the microbit is sent across via a serial connection, and to start drawing run the microbitDraw.py program. The initial template used for this MicroBit V1 C/C++ project was taken from the book "Micro:Bit Iot in C" by Harry Fairhead.

## How to use
### Prerequisites
1. Install the arm-none-eabi-gcc compiler
2. Install Cmake
3. Install ninja
4. Have a V1 Micro:bit
5. Install the VS code Cmake extension (if using instructions below)

### Build project (with VS code)
1. Replace any occurrence of the absolute path **/home/hettysymes/Microbit** with your own path to the Microbit directory.
2. Clean reconfigure all projects (using Cmake extension).
3. When asked to select a kit on configuring the project for the first time choose the **GCC arm-none-eabi** kit.
4. When asked to locate the **CMakeLists.txt** file choose the one in the **MicrobitDraw/build/bbc-microbit-classic-gcc** directory.
5. Build the project (using Cmake extension).
6. Find **build/source/MicrobitDraw-combined.hex** and transfer this file to your Micro:bit.
Your Micro:bit is now ready to use for drawing.

### Run drawing application
1. Connect the Micro:bit to a computer via serial port.
2. Run the microbitDraw.py python program on your computer. Install any relevant packages needed to do so.
3. A window will pop up and you can use the Micro:bit tilt and buttons for drawing on the window.
