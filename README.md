# CoffeeBot

## Overview
The intent behind this project is to prepare high quality cold brew coffee with accurate measurements with a click of a button. Hence, CoffeeBot is designed for users to customize their coffee drinks using remote assistance to save time and effort. The bot is portable and includes delivery options with interactive lighting. 

## Parts List:
1 x mBed LPC1768 microcontroller<br/>
1 x Raspberry Pi Model 3 B<br/>
1 x 8-channel Relay board<br/>
4 x Perastaltic pumps<br/>
1 x LED Strip<br/>
1 x DC 12V Motor Driver<br/>
1 x Toy DC Motor Set<br/>


## System Architecture
The Architecture is divided into two sections: Motor Control and Pumping. Raspberry Pi handles the pumping while the mBed controls the Motor Driver. Raspberry Pi interfaces with the mBed serially via USB cable. A 12V/5A Power Supply supplies power to the motor dirver, perastaltic pumps, and LED strip. 
![SysArch Diagram](https://github.com/praneetheddu/CoffeeBot/blob/master/Untitled%20Diagram.jpg)

### Motor Control
The mBed sends encoded signals to the Motor Driver to control the speed and direction of the motors. Since the driver is only dual channel and there are four motors, the front and back motor of each side are connected in series to both channels.

### Pumping
8-channel relay board controls the pump motors by completing the circuit with the power supply. Since there are only 4 pumps, only 4 relay connections are needed abut they can be extendable to control 8 pumps. 

### Added Effect
There is an LED strip attached to the mBed which acts as an indicator for pumping status. The color changes to Red when the pumps are in Idle mode and switched to Green if the pumps are active.

## Physical Enclosure
The enclosure is made from MDF board. The enclosure composes of electrical control section (left panel) where the PCBs and circuit elements are mounted, dedicated liquid storage (top right section) for storing liquified sugar, creamer, and flavors, and coffee pumping  station (front right section) where the coffee and other liquids are flowing into a cup. The peristaltic pumps, mounted on the bottom panel as displayed in the image, are attached to surgical tubing routed from liquid containers to coffee cup. A funnel mount is placed above the coffee cup for filteration. Wodden support beams are placed along the edges for durabiltiy.


## GUI

## Parts Used

## Schematics

## Functionality

## Demo
