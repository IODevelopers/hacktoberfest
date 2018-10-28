#include <Ultrasonic.h>
#include <BoltIoT-Arduino-Helper.h>

#define ULTRASONIC_TRIG_PIN 12
#define ULTRASONIC_ECHO_PIN 13

Ultrasonic ultrasonic(ULTRASONIC_TRIG_PIN,ULTRASONIC_ECHO_PIN);
int distance=0;

String getDistance(String *arguments){
  distance = ultrasonic.read();
    String returnString=""+String(distance);
    return returnString;
}

void setup() {
  boltiot.begin(Serial);
  // put your setup code here, to run once:
  boltiot.setCommandString("RD\r",getDistance);
  boltiot.setCommandString("GetDistance",getDistance);
}

void loop() {
  boltiot.handleCommand();
  // put your main code here, to run repeatedly:
  
}
