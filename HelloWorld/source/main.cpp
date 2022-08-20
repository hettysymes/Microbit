#include "MicroBit.h"

#define I2C_ADDR 0x3A
#define WHO_AM_I_REG 0x0D
#define CTRL_REG1 0x2A
#define CTRL_REG2 0x2B
#define XACC_MSB_REG 0x01
#define YACC_MSB_REG 0x03
#define ZACC_MSB_REG 0x05
#define ACC_DIM 3
#define DATA_FREQ 500
#define AXIS_LIM 600
MicroBit uBit;

// int main() {
//   uBit.init();
//   for (int i=0;;i++) {
//     uBit.serial.printf("%d,%d\n\r", uBit.accelerometer.getX(), uBit.accelerometer.getY());
//     uBit.sleep(DATA_FREQ);
//   }
// }

int byteToInt(char byte) {
  if ((byte & 0x80) == 0){
    return byte;
  }
  else {
    return (char)(~(byte - 0x01)) * -1;
  }     
}

int readReg(uint8_t reg) {
    uint8_t buf;
    uBit.i2c.write(I2C_ADDR, (const char *)&reg, 1, true);
    uBit.i2c.read(I2C_ADDR, (char *)&buf, 1);
    return byteToInt((char) buf);
}

int main() {
  uBit.init();
  for (int i=0;;i++) {
    uBit.serial.printf("%d,%d\n\r", readReg(XACC_MSB_REG), readReg(YACC_MSB_REG));
    uBit.sleep(DATA_FREQ);
  }
}

// int main() {
//   uBit.init();
//   for (int i=0;;i++) {
//     int x = uBit.i2c.readRegister(I2C_ADDR, XACC_MSB_REG);
//     int y = uBit.i2c.readRegister(I2C_ADDR, YACC_MSB_REG);
//     if (x > AXIS_LIM) {
//       uBit.serial.printf("%c\n\r", 'R');
//     } else if (x < -AXIS_LIM) {
//       uBit.serial.printf("%c\n\r", 'L');
//     } else if (y > AXIS_LIM) {
//       uBit.serial.printf("%c\n\r", 'D');
//     } else if (y < -AXIS_LIM) {
//       uBit.serial.printf("%c\n\r", 'U');
//     } else {
//       uBit.serial.printf("%c\n\r", 'S');
//     }
//     uBit.sleep(DATA_FREQ);
//   }
// }

// int main() {
//   uBit.init();
//   //uBit.serial.printf("CtrlReg1: %x\n\r", readReg(CTRL_REG1));
//   int *accs = (int*) malloc(ACC_DIM * sizeof(int));
//   long timeStart = uBit.systemTime();
//   for (int i=0;;i++) {
//     long timeNow = uBit.systemTime();
//     getAllAccs(accs);
//     //uBit.serial.printf("%d,%d,%d,%d,%ld\n\r", i, accs[0], accs[1], accs[2], timeNow - timeStart);
//     uBit.serial.printf("%d,%d,%d,%d,%ld\n\r", i,uBit.accelerometer.getX(), uBit.accelerometer.getY(), uBit.accelerometer.getZ(), timeNow - timeStart);
//     uBit.sleep(DATA_FREQ);
//   }
// }

/*
int main() {
  uBit.init();
  uBit.serial.printf("WhoAmI: %x\n\r", (int)readByte(WHO_AM_I_REG));
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
