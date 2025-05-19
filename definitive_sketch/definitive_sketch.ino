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
const bool active_servo = false;

//Instruction-keeping variables
char direction = 'H';
unsigned long speed = 0;
unsigned long angle = 90;
unsigned long movement_duration = 0;
unsigned long elapsed_time = 0;




void setup() {
  // Used to display information
  Serial.begin(9600);

  // Wait for Serial Monitor to be opened
  while (!Serial)
  {
    //do nothing
  }
  //Initialize motors
  motors.setSpeed(0); //Remember it's a 0-255 range
  motors.forward();
  //Initialize servos (for some reason, the person who made this library made it so that servos can oly attach to pins 9 and 10. Fucking dickhead)
  servo.attach(9);
  servo.write(90);
}

void loop() {
  // put your main code here, to run repeatedly:

  //First check time
  elapsed_time = millis();
  if(elapsed_time >= movement_duration)
  {
    //Read previous movement
    long int instruction_end = instruction.indexOf("/");
    String current_instruction = instruction.substring(0, instruction_end);
    instruction.remove(0, instruction_end);

    //Read direction
    direction = current_instruction[0];
    long int locator = current_instruction.indexOf(",");
    current_instruction.remove(0, locator + 1);

    //Read speed
    locator = current_instruction.indexOf(",");
    speed = current_instruction.substring(0, locator).toInt();
    if(direction == 'B' and speed > 0) speed -= 2*speed;
    current_instruction.remove(0, locator + 1);
    
    //Read angle
    locator = current_instruction.indexOf(",");
    angle = current_instruction.substring(0, locator).toInt();
    if(direction == 'L' and angle > 0) angle -= 2*angle;
    else if(direction == 'F' or direction == 'B') angle = 0;
    current_instruction.remove(0, locator + 1);
    
    //Read time
    long double ttime = current_instruction.toDouble() * 1000;

    //Set new movement
    //Set speed
    if(speed >= 0) motors.forward();
    else motors.backward();
    motors.setSpeed(speed);
    //Set angle
    servo.write(angle + 90);
    //Set the amount of time
    movement_duration += ttime;
  }
  while(distanceSensor.measureDistanceCm() < 30 or instruction == "")
  {
    motors.stop();
  }
  if(direction == 'B') motors.backward();
  else motors.forward();
}
