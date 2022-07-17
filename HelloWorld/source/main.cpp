#include "MicroBit.h"

//get id of accelerometer
MicroBit uBit;
int main() {
  uBit.init();
  char buf[] = {0x0D};
  uBit.i2c.write(0x3A, buf, 1, true);
  uBit.i2c.read(0x3A, buf, 1);
  uBit.serial.printf("Id: %X\r\n", (int)buf[0]);
  release_fiber();
}

/*
//get coordinates of accelerometer using uBit.accelerometer
MicroBit uBit;
int main() {
  uBit.init();
  for (;;) {
    int xAcc, yAcc;
    xAcc = uBit.accelerometer.getX();
    yAcc = uBit.accelerometer.getY();
    uBit.serial.printf("%d,%d\n", xAcc, yAcc);
    uBit.sleep(100);
  }
}
*/
