#include "mbed.h"
#include "Motor.h"
#include "rtos.h"

//Pi mbed USB Slave function
// connect mbed to Pi USB
RawSerial  pi(USBTX, USBRX);
 

DigitalOut led1(LED1);
DigitalOut led2(LED2);

//LED strip setup
PwmOut blue(p23);
PwmOut red(p22);
PwmOut green(p21);

// Motor Driver setup
Motor Forward_Rev(p24, p19, p20);
Motor Turning(p25, p17, p18);

// Parse value setup
char motorValue;
char LEDToggle;

// Thread Setup
Thread t1;
Thread t2;
Thread t3;

// Motor one Control which controls the left two motors
void motorOneControl() {
    while(1) {
        switch(motorValue) {
            case '1': //Forward             
                Forward_Rev.speed(0.35);
                wait(0.02);
                break;
            case '2': //Reverse
                wait(0.02);
                break;
            case '3': //Left
                Forward_Rev.speed(0.9);
                wait(0.02);
                break;
            case'4': //Right
                Forward_Rev.speed(-0.9);
                wait(0.02);
                break;
            default: //Stop
                Forward_Rev.speed(0.0);
                wait(0.02);
                break;
                
        } 
    }
}
//

// Motor two Control which controls the right two motors
void motorTwoControl() {
    while(1) {
        switch(motorValue) {
            case '1': //Forward
                Turning.speed(0.35);
                wait(0.02);
                break;
            case '2': //Reverse
                Turning.speed(-0.35);
                wait(0.02);
                break;
            case '3': //Left
                Turning.speed(-0.9);
                break;
            case'4': //Right
                Turning.speed(0.9);
                wait(0.02);
                break;
            default: //Stop
                Turning.speed(0.0);
                wait(0.02);
                break;
                
        } 
    }
}

// LED strip turns green when the pumps are active and turn red when they are idle
void LEDControl() {
    while(1){
        if (LEDToggle == '1') {
            green = 0.6f;
            red  = 0.0f;
            
        } else {
            red  = 0.5f;
            green = 0.0f;
        }
    }
}

//Raspberry Pi to mBed parsing
void dev_recv()
{

    led1 = !led1;
    while(pi.readable()) {
        LEDToggle = pi.getc();
        motorValue = pi.getc();
        pi.putc(motorValue);
        pi.putc(LEDToggle);
    }
}

int main()
{    
    // Serial Setup
    pi.baud(9600);
    pi.attach(&dev_recv, Serial::RxIrq);
    
    // Run three threads for higher throughput
    t1.start(motorOneControl);
    t2.start(motorTwoControl);
    t3.start(LEDControl);

    while(1) {
        sleep();
    }

}
