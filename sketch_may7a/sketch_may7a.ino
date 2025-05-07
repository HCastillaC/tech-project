#include <HCSR04.h>
#include <Servo.h>
#include <L298NX2.h>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

//Initialize motors

const unsigned int EN_A = 11;
const unsigned int IN1_A = 13;
const unsigned int IN2_A = 12;

const unsigned int IN1_B = 8;
const unsigned int IN2_B = 7;
const unsigned int EN_B = 5;

L298NX2 motors(EN_A, IN1_A, IN2_A, EN_B, IN1_B, IN2_B);

//Initialize servos

Servo left_servo;
Servo right_servo;

//Initialize distance sensor
const byte triggerPin = 2;
const byte echoPin = 3;
UltraSonicDistanceSensor distanceSensor(triggerPin, echoPin);

//Testing only
const unsigned int testing_time = 10000;

int rng(int limit)
{
  return random() % (limit + 1);
}

void setup() {
  // Used to display information
  Serial.begin(9600);
  srand(time(NULL));

  // Wait for Serial Monitor to be opened
  while (!Serial)
  {
    //do nothing
  }
  //Initialize motors
  motors.setSpeed(100); //Remember it's a 0-255 range
  motors.forward();
  delay(testing_time);
  //Initialize servos (for some reason, the person who made this library made it so that servos can oly attach to pins 9 and 10. Fucking dickhead)
  left_servo.attach(9);
  left_servo.write(90);
  right_servo.attach(10);
  right_servo.write(90);
}

void loop() {
  // put your main code here, to run repeatedly:
  motors.setSpeedA(rng(255));
  motors.setSpeedB(rng(255));
  left_servo.write(rng(180));
  right_servo.write(rng(180));
  if(distanceSensor.measureDistanceCm() < 5)
  {
    motors.backward();
  }
  delay(testing_time);
}
