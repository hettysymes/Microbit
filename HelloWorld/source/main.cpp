#include "MicroBit.h"

#define I2C_ADDR 0x3A
#define WHO_AM_I_REG 0x0D
#define CTRL_REG1 0x2A
#define CTRL_REG2 0x2B
#define XACC_MSB_REG 0x01
#define YACC_MSB_REG 0x03
#define ZACC_MSB_REG 0x05
#define ACC_DIM 3
#define DATA_FREQ 50
#define AXIS_LIM 600
#define LIGHT_BRIGHTNESS 10
MicroBit uBit;
bool buttonBclicked = false;
bool buttonAclicked = false;

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

void updateDisplayLight() {
  if (buttonBclicked) {
    uBit.display.image.setPixelValue(2, 2, LIGHT_BRIGHTNESS);
  } else {
    uBit.display.image.setPixelValue(2, 2, 0);
  }
}

void buttonBClickEvent(MicroBitEvent e) {
  buttonBclicked = !buttonBclicked;
  updateDisplayLight();
}

void buttonAClickEvent(MicroBitEvent e) {
  buttonAclicked = true;
}

void setUpButtons() {
  uBit.buttonB.setEventConfiguration(MICROBIT_BUTTON_ALL_EVENTS);
  uBit.messageBus.listen(MICROBIT_ID_BUTTON_B, MICROBIT_BUTTON_EVT_CLICK, buttonBClickEvent);
  uBit.buttonA.setEventConfiguration(MICROBIT_BUTTON_ALL_EVENTS);
  uBit.messageBus.listen(MICROBIT_ID_BUTTON_A, MICROBIT_BUTTON_EVT_CLICK, buttonAClickEvent);
}

int main() {
  uBit.init();
  uBit.display.setDisplayMode(DISPLAY_MODE_GREYSCALE);
  setUpButtons();
  for (int i=0;;i++) {
    uBit.serial.printf("%d,%d,%d,%d\n\r", readReg(XACC_MSB_REG), readReg(YACC_MSB_REG), buttonBclicked, buttonAclicked);
    if (buttonAclicked) buttonAclicked = false;
    uBit.sleep(DATA_FREQ);
  }
}