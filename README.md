# 4x4x4-Led-Cube-Using-ESP32-and-Micropython
4x4x4 Led Cube with ESP32 and Micropython. Added a web server to control the cube with Android Application.

![img_cover](/media/cover.jpg)

# Installing Micropython on ESP32
Before running the `main.py` script, you must've install [Micropython Firmare](http://micropython.org/download) on your ESP32 dev kit.
Follow the steps to install MicroPython on your ESP32:
* [Download](http://micropython.org/resources/firmware/esp32-idf3-20200103-v1.12-35-g10709846f.bin) the firmware.
* To flash the firmware on esp32, we''ll need esptool. You can install that by running following pip command `pip install esptool`
* To validate if it is installed, issue the following command in terminal: `esptool`.
* Connect your ESP32 to your pc and get the COM port of ESP32. 
* **While holding the boot button** on esp32 execute `esptool --chip esp32 -p ENTER_YOUR_SERIAL_PORT erase_flash` in the terminal.
* After it's done execute `esptool --chip esp32 -p COM5 write_flash -z 0x1000 "PATH/TO/FIRMARE/esp32-idf3-20191222-v1.12-5-g42e45bd69.bin"`
* Your ESP32 is now ready with Micropython. To get into the python interpreter aka repl, you'll need to download any Serial Console software.
I am using [putty](https://www.putty.org/).

# Running the `main.py` script
:heavy_exclamation_mark: Note: You must edit the `main.py` script and replace the Wi-Fi SSID and Password with your own network.

To upload `.py` files on your esp32, you need to download another tool, called ampy.
* You can install ampy through pip command `pip install adafruit-ampy`.
* To validate the install, type `ampy` in terminal.
* To upload code on esp32, issue the following command in terminal from the folder which contains the script `ampy --port YOUR_PORT_HERE --baud 115200 put main.py`
* You can use putty to see what's happening in the serial terminal.
* After uploading the main.py script open the serial console (for e.g. putty, type serial port and baud rate i.e. 115200), where you can see 
it's being connecting to the wifi network. It will give a private ip address, which you can browse on Chrome (or any other web browser).
* The webpage opened will allow you to control the LED cube. But we are going to make an android application to control it.

# Creating Android App using MIT App Inventor
* [MIT App Inventer](https://appinventor.mit.edu/) is a great platform for developing android applications. It uses visual programming and provides a user friendly
 interface which makes developing the app a cakewalk.
* Go to the website and create your account or use your google account. [Create new project](http://ai2.appinventor.mit.edu/). I'm not going through all the steps for making this application.
  I'll share my project, from where you can download the apk file.
* Click on Import Project(.aia) from My Project tab in top left corner.Browse to the .aia file which is present in this repo.
* After importing .aia file go to the Blocks present at the top right corner. Change the url to the ip address that you got from the terminal.
* Now, click on build and then on Provide QR code to download the apk.
* Install the apk and you are good to go.

### Web Interface
![img1](/media/mit-app.jpg)

### Android Interface
![img2](/media/android_interface.jpg)

# Connection Setup with ESP32
![img3](/connections/connection.jpg)

:heavy_exclamation_mark: GPIO 1,3,6,7,8,9,10,11,34,35,36,39 are not used!
### For Columns:
  
(X,Y)- GPIO pins

(1,1)-0
(1,2)-15
(1,3)-2
(1,4)-4
(2,1)-16
(2,2)-17
(2,3)-5
(2,4)-18
(3,1)-19
(3-2)-21
(3-3)-22
(3,4)-23
(4,1)-13
(4,2)-12
(4,3)-14  
(4,4)-27

### For Layers:

A-26
B-25
C-33
D-32

![img4](/connections/ESP32-DOIT-DEVKIT-V1-Board-Pinout-36-GPIOs-updated.jpg)

# Reference:
Follow this amazing tutorial for constructing the LED Cube: [Instructables](https://www.instructables.com/id/4x4x4-LED-Cube-Arduino-Uno/)
