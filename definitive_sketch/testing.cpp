#include <iostream>
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
using namespace std;

//Instruction-keeping variables
string ins = "";
string current_instruction = "";
char direction = 'H';
long int speed = 0;
long int angle = 90;
long double ttime = 0;
long int movement_duration = 0;
double long elapsed_time = 0;

//Result
bool forwards = 1;
int fspeed = 0;
int fangle = 0;

void print_instruction()
{
    cout << "ins: " << ins << endl;
    cout << "current_instruction: " << current_instruction << endl;
    cout << endl;
}

void print_info()
{
    cout << "ins: " << ins << endl;
    cout << "current_instruction: " << current_instruction << endl;
    cout << "direction: " << direction << endl;
    cout << "speed: " << speed << endl;
    cout << "angle: " << angle << endl;
    cout << "ttime: " << ttime << endl;
    cout << "movement_duration: " << movement_duration << endl;
    cout << "elapsed_time: " << elapsed_time << endl;
    cout << "F?: " << forwards << endl;
    cout << "fspeed: " << fspeed << endl;
    cout << "fangle: " << fangle << endl;
    cout << endl;
}

int millis()
{
    int n = rand() % 100 + 1;
    return n + elapsed_time;
}

bool loop()
{
    elapsed_time = millis();

    if(elapsed_time >= movement_duration)
    {
        //Check end of movement
        if(ins == "") return false;
        
        //Read previous movement
        long int instruction_end = ins.find('/');
        current_instruction = ins.substr(0, instruction_end);
        ins.erase(0, instruction_end + 1);
        print_instruction();

        //Read direction
        direction = current_instruction[0];
        long int locator = current_instruction.find(",");
        current_instruction.erase(0, locator + 1);
        print_instruction();

        //Read speed
        locator = current_instruction.find(",");
        speed = stoi(current_instruction.substr(0, locator));
        if(direction == 'B' and speed > 0) speed -= 2*speed;
        current_instruction.erase(0, locator + 1);
        print_instruction();
        
        //Read angle
        locator = current_instruction.find(",");
        angle = stoi(current_instruction.substr(0, locator));
        if(direction == 'L' and angle > 0) angle -= 2*angle;
        else if(direction == 'F' or direction == 'B') angle = 0;
        current_instruction.erase(0, locator + 1);
        print_instruction();

        //Read time
        ttime = stold(current_instruction) * 1000;

        //Set new movement
        //Set speed
        if(speed >= 0) forwards = 1;
        else forwards = 0;
        fspeed = abs(speed);
        //Set angle
        fangle = angle + 90;
        //Set the amount of time
        movement_duration += ttime;
        print_info();
        cout << endl << endl;
    }
    return true;
}

int main()
{
    srand(time(NULL));
    cin >> ins;

    print_instruction();

    while(loop()) continue;

    return 0;
}