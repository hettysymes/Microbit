#include "MicroBit.h"

#define I2C_ADDR 0x3A
#define WHO_AM_I_REG 0x0D
#define CTRL_REG1 0x2A
#define CTRL_REG2 0x2B
#define XACC_MSB_REG 0x01
#define YACC_MSB_REG 0x03
#define ZACC_MSB_REG 0x05
MicroBit uBit;

char readByte(char regAddr) {
  char buf[] = {regAddr};
  uBit.i2c.write(I2C_ADDR, buf, 1, true);
  uBit.i2c.read(I2C_ADDR, buf, 1);
  return buf[0];
}

int main() {
  uBit.init();
  uBit.serial.printf("WhoAmI: %x\n\r", (int)readByte(WHO_AM_I_REG));
  release_fiber();
  return 0;
}

/*
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
    xAcc = (buf2[0] << 8) | buf2[1];
    yAcc = (buf2[2] << 8) | buf2[3];
    unsigned long timeNow = uBit.systemTime();
    uBit.serial.printf("%d,%d,%d,-1,%ld\n", i, xAcc, yAcc, timeNow - timeStart);
    uBit.sleep(DATA_FREQ);
  }
}
*/



/*
MicroBit uBit;
int main() {
  uBit.init();
  char buf[] = {WHO_AM_I_REG};
  uBit.i2c.write(I2C_ADDR, buf, 1, true);
  uBit.i2c.read(I2C_ADDR, buf, 1);
  uBit.serial.printf("WhoAmI: %x\n\r", (int)buf[0]);
  release_fiber();
  return 0;
}
*/

/*
//get x and y accelerations - DIRECT
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
    xAcc = (buf2[0] << 8) | buf2[1];
    yAcc = (buf2[2] << 8) | buf2[3];
    unsigned long timeNow = uBit.systemTime();
    uBit.serial.printf("%d,%d,%d,-1,%ld\n", i, xAcc, yAcc, timeNow - timeStart);
    uBit.sleep(DATA_FREQ);
  }
}
*/

/*
//get x and y accelerations - INDIRECT
MicroBit uBit;
int main() {
  uBit.init();
  unsigned long timeStart = uBit.systemTime();
  int16_t xAcc, yAcc, zAcc;
  for (int i=0;;i++) {
    xAcc = uBit.accelerometer.getX();
    yAcc = uBit.accelerometer.getY();
    zAcc = uBit.accelerometer.getZ();
    unsigned long timeNow = uBit.systemTime();
    uBit.serial.printf("%d,%d,%d,%d,%ld\n", i, xAcc, yAcc, zAcc, timeNow - timeStart);
    uBit.sleep(DATA_FREQ);
  }
}
*/
