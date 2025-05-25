#include <HCSR04.h>
#include <Servo.h>
#include <L298NX2.h>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

/*
  ___                   _      _                   
 |_ _|_ __  _ __  _   _| |_   | |__   ___ _ __ ___ 
  | || '_ \| '_ \| | | | __|  | '_ \ / _ \ '__/ _ \
  | || | | | |_) | |_| | |_   | | | |  __/ | |  __/
 |___|_| |_| .__/ \__,_|\__|  |_| |_|\___|_|  \___|
           |_|                                   
*/

String instruction = "L,17,6,1.3185/F,102,0,2.0000/L,40,5,1.3854/R,102,5,2.2166/B,34,0,4.0000/";

//Initialize motors

const unsigned int EN_A = 11;
const unsigned int IN1_A = 13;
const unsigned int IN2_A = 12;

const unsigned int IN1_B = 8;
const unsigned int IN2_B = 7;
const unsigned int EN_B = 5;

L298NX2 motors(EN_A, IN1_A, IN2_A, EN_B, IN1_B, IN2_B);

//Initialize servos

Servo servo;

//Initialize distance sensor
const byte triggerPin = 2;
const byte echoPin = 3;
UltraSonicDistanceSensor distanceSensor(triggerPin, echoPin);

void setup() {
  // Used to display information
  Serial.begin(9600);

  // Wait for Serial Monitor to be opened
  delay(2500);
  //Initialize motors
  motors.setSpeed(0); //Remember it's a 0-255 range
  motors.forward();
  //Initialize servos (for some reason, the person who made this library made it so that servos can oly attach to pins 9 and 10. Fucking dickhead)
  servo.attach(9);
  servo.write(90);

  //L,170,15,1.3185
  motors.setSpeed(170);
  servo.write(75);
  delay(1318);
  //F,102,0,2.0000
  motors.setSpeed(102);
  servo.write(90);
  delay(2000);
  //L,120,8,1.3854
  motors.setSpeed(120);
  servo.write(82);
  delay(1385);
  //R,102,25,2.2166
  motors.setSpeed(102);
  servo.write(115);
  delay(2216);
  //B,115,0,4.0000
  motors.backward();
  motors.setSpeed(115);
  servo.write(90);
  delay(4000);

  motors.stop();
}

void loop() {
  motors.stop();
}
