#include <Arduino.h>
#include <Servo.h>

Servo servo;
int incomingByte = 0;
int servoPos = 90;

void setup()
{
  Serial.begin(9600);
  servo.attach(9);
  // pinMode(9, OUTPUT);
}

void loop()
{
  if (Serial.available() > 0)
  {
    incomingByte = Serial.read();

    if (incomingByte == 102)
      servoPos = 97;

    if (incomingByte == 115)
      servoPos = 90;
  }

  servo.write(servoPos);
  // analogWrite(9, map(servoPos, 0, 180, 0, 255));
  Serial.println(servoPos);
}
