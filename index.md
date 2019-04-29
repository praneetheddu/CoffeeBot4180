# CoffeeBot 
<div style="text-align:center"><img src="images/newImage.jpg" alt="alt text" width="450" height="450"><br/>

  
#### Team members: <br/> Praneeth Eddu <br/> Jonathan Fernandez <br/> Zeinab Ostadabbas <br/> Jessica Hernandez
## Overview
The intent behind this project is to prepare high quality cold brew coffee with accurate measurements with a click of a button. Hence, CoffeeBot is designed for users to customize their coffee drinks using remote assistance to save time and effort. The bot is portable and includes delivery options with interactive lighting. 

## Parts List:
1 x [mBed LPC1768 microcontroller](https://os.mbed.com/platforms/mbed-LPC1768/)<br/>
1 x [Raspberry Pi Model 3 B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)<br/>
1 x [8-channel Relay board](https://www.amazon.com/JBtek-Channel-Module-Arduino-Raspberry/dp/B00KTELP3I)<br/>
4 x [Peristaltic pumps](https://www.amazon.com/MqbY-Dosing-Peristaltic-Aquarium-Analytical/dp/B07QB3NX8K/ref=sr_1_1?crid=191M85H2CJKWY&keywords=peristaltic+pump+12v&qid=1556389996&s=electronics&sprefix=peristalti%2Celectronics%2C139&sr=1-1)<br/>
1 x [RGB LED Strip](https://www.amazon.com/NZXT-HUE-LED-Strips-Accessory/dp/B07GF4K7XB/ref=sr_1_11?keywords=LED+strip&qid=1556390046&s=electronics&sr=1-11)<br/>
1 x [DC 12V Motor Driver](https://www.amazon.com/DROK-Controller-Regulator-Industrial-Optocoupler/dp/B06XGD5SCB?ref_=fsclp_pl_dp_8)<br/>
1 x [Toy DC Motor Set](https://www.amazon.com/dp/B07DRGTCTP/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B07DRGTCTP&pd_rd_w=o3sgj&pf_rd_p=733540df-430d-45cd-9525-21bc15b0e6cc&pd_rd_wg=425d1&pf_rd_r=VBMDQVAQPT2Q7KMDJTNJ&pd_rd_r=b4686a1f-5186-11e9-aa3a-534f289d7dcb)<br/>


## System Architecture
The Architecture is divided into two sections: Motor Control and Pumping. Raspberry Pi handles the pumping while the mBed controls the Motor Driver. Raspberry Pi interfaces with the mBed serially via USB cable. A 12V/5A Power Supply supplies power to the motor dirver, perastaltic pumps, and LED strip.<br/><br/>

![Schematic](/SystemArch.jpg)

### Motor Control
The mBed sends encoded signals to the Motor Driver to control the speed and direction of the motors. Since the driver is only dual channel and there are four motors, the front and back motor of each side are connected in series to both channels.

### Pumping
8-channel relay board controls the pump motors by completing the circuit with the power supply. Since there are only 4 pumps, only 4 relay connections are needed abut they can be extendable to control 8 pumps. 

### Added Effect
There is an LED strip attached to the mBed which acts as an indicator for pumping status. The color changes to Red when the pumps are in Idle mode and switched to Green if the pumps are active.

## Physical Enclosure
The enclosure is made from MDF board. The enclosure composes of electrical control section (left panel) where the PCBs and circuit elements are mounted, dedicated liquid storage (top right section) for storing liquified sugar, creamer, and flavors, and coffee pumping  station (front right section) where the coffee and other liquids are flowing into a cup. The peristaltic pumps, mounted on the bottom panel as displayed in the image, are attached to surgical tubing routed from liquid containers to coffee cup. A funnel mount is placed above the coffee cup for filteration. Wodden support beams are placed along the edges for durabiltiy.

For in-depth list of dimensions, please click [here](https://github.com/praneetheddu/CoffeeBot/blob/master/Dimensions/4180%20Final%20Measurements.pdf)


## Schematics
### Full Schematic

![CoffeBot Schematic](/CoffeeBot_Schematic.png)

### Raspberry Pi Schematic


![Raspi_copy](/Raspi_copy.png)

### mBed Schematic


![mBed_copy](/mbed_copy.png)


## Wiring Guide
### Raspberry Pi Setup
The pinout for Raspberry Pi Model 3 can be found [here](https://www.raspberrypi-spy.co.uk/2014/07/raspberry-pi-b-gpio-header-details-and-pinout/)
<br/>

| Raspberry Pi  | Relay Board |
| ------------- | ------------- |
| +5V  | VCC  |
| GPIO 16  | IN 1  |
| GPIO 20  | IN 2  |
| GPIO 21  | IN 3  |
| GPIO 12  | IN 4  |
| GND  | GND  |

### Mbed Setup
The pinout for mBed can be found [here](https://os.mbed.com/platforms/mbed-LPC1768/)
<br/>

| mBed  | Motor Driver |
| ------------- | ------------- |
| VOut  | +5V  |
| p25  | ENA 1  |
| p26  | ENA 2  |
| p19 | IN 1  |
| p20  | IN 2  |
| p21 | IN 3  |
| p22  | IN 4  |
| GND  | GND  |

### Power Supply Pinout

| Power Supply  | Connection |
| ------------- | ------------- |
| +12V  | Motor Driver Vin <br/> Relay Switches|
| GND  | Motor Driver GND <br/> Peristaltic Pumps GND  |


## GUI
The GUI's are created using Adafruit IO Dashboards. There are two GUI's utilized for this project: CoffeeBot and Motor Control. 
### CoffeBot GUI 
![Coffee Bot GUI](/CoffeeBotGUI.png)

### Motor Control GUI 
![Motor Control GUI](/MotorControlGUI.png)

The frontend for the GUI is manually designed by placing sliders, buttons, and text. Each element of the GUI is linked to a feed which is useful when writing a backend program using Python3  on Raspberry Pi. In our case, each pushbutton (CoffeeBot uses Start, Motor Control uses Up, Stop, Left, Right) sends a 1 or 0 to indicate that the user has pressed the button. For sliders (Sugar, Creamer, and Sweetner), a value between 0 and 5 is sent to the backend Python3 program. Since each element is utilized by its own feed, there is no interference between the values.

**Caution: The Adafruit IO free subscription is only limited to 30 feeds per minute which means there should be a time delay of 1 sec to cycle between the feeds. Also, there are limited number of feeds and dashboards that the user can create. To ensure faster and more responsive update rate, the user can pay $9.99 subscription fee which extends the feed update rate to  60 feeds/min and unlimited dashboards and feeds.**

For an in-depth Adafruit IO tutorial, Please click [here](https://learn.adafruit.com/adafruit-io/getting-started)

## Raspberry Pi Backend
Raspberry Pi recieves the values that are sent from the GUI to initiate the functionality process. There are three programs written on Raspberry Pi: CoffeeBot.py (Python), MotorControl.py (Python), RaspiToMbed.cc (C++). 

**CoffeeBot.py:** The values that are received from the CoffeBot GUI are used here. The slider values control the flow rate of the liquid by tablespoon increments by turning on the relay switch. For example: 2 tablespoons of sugar turns the relay switch for 2 x one table spoon time seconds. The one table spoon time can vary between different pumps and variable voltages which can be measured and set to the appropriate time. Also, the LED strip value of 1 is passed to RaspiToMbed.cc program when the pumps are active.

**MotorControl.py:** The program receives the input from Motor Control GUI and passes a value between 0 and 4 to RaspiToMbed.cc.

| GUI Command  | Value passed to Mbed |
| ------------- | ------------- |
| No button pressed  | 0  |
| Up  | 1  |
| Stop  | 2  |
| Left | 3  |
| Right | 4  |

**RaspiToMbed.cc**: The values(LED Strip and Motor Control) that are updated in the python programs are passed to mBed serially. 

Raspberry Pi files are available [here](https://github.com/praneetheddu/CoffeeBot/tree/master/Raspberry%20Pi%20Code)

## mBed Backend
There is only one program written in mBed named CoffeeBot.cc which uses RTOS to run threads to control the motors and LED. Serial library is used to recieve the commands from Raspberry Pi.

mBed files are available [here](https://github.com/praneetheddu/CoffeeBot/blob/master/CoffeeBot/main.cpp)
## Demo

## Improvements
1. Having a battery that supplies enough power to run the motors and pumps
2. More peristaltic pumps to add flavors and custom drinks
3. Create one GUI that can support Motor Control and Pumping and add some custom drinks pushbutton
4. Better Motors and reliable tires 
