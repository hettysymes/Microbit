#include "MicroBit.h" 
MicroBit uBit; int main() {
 uBit.init();
 //uBit.display.scroll("Hello World");
 uBit.display.scroll("Test 2");
 release_fiber();
}