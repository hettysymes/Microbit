#include "MicroBit.h"

//get coordinates of accelerometer
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

/*
#include "MicroBit.h" 
MicroBit uBit; int main() {
 uBit.init();
 //uBit.display.scroll("Hello World");
 uBit.display.scroll("Test 2");
 release_fiber();
}
*/

/*
#include "MicroBit.h"
MicroBit uBit;
int main() {
  uBit.init();
  uBit.display.setDisplayMode(DISPLAY_MODE_GREYSCALE);
  for (int i = 0; i < 5; i++) {
    uBit.display.image.setPixelValue(2, 2, 255);
    uBit.sleep(1000);
    uBit.display.image.setPixelValue(2, 2, 0);
    uBit.sleep(1000);  
  }  
}
*/
