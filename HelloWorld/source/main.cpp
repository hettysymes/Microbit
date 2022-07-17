#include "MicroBit.h"

#define I2C_ADDR 0x3A
#define ACC_REG 0x01
#define ACC_BYTE_SIZE 4
#define DATA_FREQ 10

//get x and y accelerations
MicroBit uBit;
int main() {
  uBit.init();
  unsigned long timeStart = uBit.systemTime();
  char buf[] = {ACC_REG};
  char buf2[ACC_BYTE_SIZE+1];
  int16_t xAcc;
  int16_t yAcc;

  for (int i=0;;i++) {
    uBit.i2c.write(I2C_ADDR, buf, 1, true);
    uBit.i2c.read(I2C_ADDR, buf2, ACC_BYTE_SIZE);
    xAcc = buf2[0] << 8 | buf2[1];
    yAcc = buf2[2] << 8 | buf2[3];
    unsigned long timeNow = uBit.systemTime();
    uBit.serial.printf("%d,%d,%d,%d\r\n", i, xAcc, yAcc, timeNow - timeStart);
    uBit.sleep(DATA_FREQ);
  }
}

/*
//get coordinates of accelerometer using uBit.accelerometer
MicroBit uBit;
int main() {
  uBit.init();
  unsigned long timeStart = uBit.systemTime();
  int xAcc, yAcc;
  for (int i = 0;;i++) {
    xAcc = uBit.accelerometer.getX();
    yAcc = uBit.accelerometer.getY();
    unsigned long timeNow = uBit.systemTime();
    uBit.serial.printf("%d,%d,%d,%d\r\n", i, xAcc, yAcc, timeNow - timeStart);
    uBit.sleep(DATA_FREQ);
  }
}
*/

/*
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
*/
