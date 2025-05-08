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
const unsigned int testing_time = 1000;

int rng(int limit)
{
  return random() % (limit + 1);
}

void printSomeInfo()
{
  Serial.print("Motor A is moving = ");
  Serial.print(motors.isMovingA() ? "YES" : "NO");
  Serial.print(" at speed = ");
  Serial.println(motors.getSpeedA());
  Serial.print("Motor B is moving = ");
  Serial.print(motors.isMovingB() ? "YES" : "NO");
  Serial.print(" at speed = ");
  Serial.println(motors.getSpeedB());
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
  motors.setSpeed(255); //Remember it's a 0-255 range
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
  motors.setSpeed(255);
  motors.forward();
  left_servo.write(0);
  right_servo.write(0);
  if(distanceSensor.measureDistanceCm() < 5)
  {
    //motors.backward();
  }
  delay(testing_time);
  left_servo.write(180);
  right_servo.write(180);
  printSomeInfo();
  delay(testing_time);
}
