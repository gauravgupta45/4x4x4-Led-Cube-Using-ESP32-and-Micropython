"""-----------------------Connection Establishing-----------------"""

try:
  import usocket as socket
except:
  import socket
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'YOUR SSID'
password = 'WIFI PASSWORD'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())



from random import randint
from time import sleep
from machine import Pin

#initializing and declaring led columns
column=[0,15,2,4,16,17,5,18,19,21,22,23,13,12,14,27]
#column=[27,14,12,13,23,22,21,19,18,5,17,16,4,2,15,0]
#initializing and declaring led layers
layer=[26,25,33,32]
#layer=[32,33,25,26]
time = 250;
columnpin={}
layerpin={}

def setup():
    #setting rows to ouput
    for i in range(0,16):
      columnpin[i]=Pin(column[i],Pin.OUT)
    #print("\nColumn Pins: {} \n".format(columnpin))

    #setting layers to output
    for i in range(0,4):
      layerpin[i]=Pin(layer[i],Pin.OUT)
    #print("Layer Pins: {} \n".format(layerpin))


def all_act():
  print("----------------------Starting the Show!----------------------\n")
  sleep(1) #1sec delay
  turnEverythingOff()
  flickerOn()
  turnEverythingOn()
  turnOnAndOffAllByLayerUpAndDownNotTimed()
  layerstompUpAndDown()
  turnOnAndOffAllByColumnSideways()
  aroundEdgeDown()
  turnEverythingOff()
  randomflicker()
  randomRain()
  diagonalRectangle()
  goThroughAllLedsOneAtATime()
  propeller()
  spiralInAndOut()
  flickerOff()
  print("-------------------------GoodBye, Friend------------------------\n")
  turnEverythingOff()


"""----------------------Acts Defination (For running specific act forever!)------------------- """

def act_1():
    turnEverythingOn()
def act_2():
    turnEverythingOff()
def act_3():
    flickerOn()
def act_4():
    turnEverythingOn()
    layerstompUpAndDown()
def act_5():
    turnOnAndOffAllByColumnSideways()
def act_6():
    aroundEdgeDown()
def act_7():
    randomflicker()
def act_8():
    randomRain()
def act_9():
    diagonalRectangle()
def act_10():
    goThroughAllLedsOneAtATime()
def act_11():
    propeller()
def act_12():
    spiralInAndOut()
def act_13():
    flickerOff()

""" ------------------------------Functions Defination--------------------------"""

def turnEverythingOn():
    for i in range(0,4):
        layerpin[i].value(1)
    for i in range(0,16):
        columnpin[i].value(0)
def turnEverythingOff():
    for i in range(0,4):
        layerpin[i].value(0)
    for i in range(0,16):
        columnpin[i].value(1)
def turnColumnsOff():
    for i in range(0,16):
        columnpin[i].value(1)
def flickerOn():
    print("--->Performing Flicker On\n")
    i=150
    while i!=0:
        turnEverythingOn()
        sleep(i/1000)
        turnEverythingOff()
        sleep(i/1000)
        i-=5
    turnEverythingOn()
def turnOnAndOffAllByLayerUpAndDownNotTimed():
    x=75/1000
    for i in range(5,0,-1):
        turnEverythingOn()
        for i in range(4,0,-1):
            layerpin[i-1].value(0)
            sleep(x/1000)
        for i in range(0,4):
            layerpin[i].value(1)
            sleep(x/1000)
        for i in range(0,4):
            layerpin[i].value(0)
            sleep(x/1000)
        for i in range(4,0,-1):
            layerpin[i-1].value(1)
            sleep(x/1000)
        turnEverythingOn()
def turnOnAndOffAllByColumnSideways():
    print("--->Performing Turn On and Off All By Column Sideways\n")
    x=75
    turnEverythingOff()
    #turn on all layers
    for i in range(0,4):
        layerpin[i].value(1)
    for y in range(0,3):
        #turn on 0-3
        for i in range(0,4):
            columnpin[i].value(0)
            sleep(x/1000)
        #turn on 4-7
        for i in range(4,8):
            columnpin[i].value(0)
            sleep(x/1000)
        #turn on 8-11
        for i in range(8,12):
            columnpin[i].value(0)
            sleep(x/1000)
        #turn on 12-15
        for i in range(12,15):
            columnpin[i].value(0)
            sleep(x/1000)
        #turn off 0-3
        for i in range(0,4):
            columnpin[i].value(1)
            sleep(x/1000)
        #turn off 4-7
        for i in range(4,8):
            columnpin[i].value(1)
            sleep(x/1000)
        #turn off 8-11
        for i in range(8,12):
            columnpin[i].value(1)
            sleep(x/1000)
        #tun off 12-15
        for i in range(12,16):
            columnpin[i].value(1)
            sleep(x/1000)
        #turn on 12-15
        for i in range(12,16):
            columnpin[i].value(0)
            sleep(x/1000)
        #turn on 8-11
        for i in range(8,12):
            columnpin[i].value(0)
            sleep(x/1000)
        #turn on 4-7
        for i in range(4,8):
            columnpin[i].value(0)
            sleep(x/1000)
        #turn on 0-3
        for i in range(0,4):
            columnpin[i].value(0)
            sleep(x/1000)
        #tun off 12-15
        for i in range(12,16):
            columnpin[i].value(1)
            sleep(x/1000)
        #tun off 8-11
        for i in range(8,12):
            columnpin[i].value(1)
            sleep(x/1000)
        #tun off 4-7
        for i in range(4,8):
            columnpin[i].value(1)
            sleep(x/1000)
        #tun off 0-3
        for i in range(0,4):
            columnpin[i].value(1)
            sleep(x/1000)
def layerstompUpAndDown():
    print("--->Performing Layers to Up and Down\n")
    x=75
    for i in range(0,4):
        layerpin[i].value(0)
    for y in range(0,5):
        for count in range(0,1):
            for i in range(0,4):
                layerpin[i].value(1)
                sleep(x/1000)
                layerpin[i].value(0)
            for i in range(4,0,-1):
                layerpin[i-1].value(1)
                sleep(x/1000)
                layerpin[i-1].value(0)
        for i in range(0,4):
            layerpin[i].value(1)
            sleep(x/1000)
        for i in range(4,0,-1):
            layerpin[i-1].value(0)
            sleep(x/1000)
def aroundEdgeDown():
    print("--->Performing Around Edge Down\n")
    for x in range(200,0,-50):
        turnEverythingOff()
        for i in range(4,0,-1):
            layerpin[i-1].value(1)
            columnpin[5].value(0)
            columnpin[6].value(0)
            columnpin[9].value(0)
            columnpin[10].value(0)
            columnpin[0].value(0)
            sleep(x/1000)
            columnpin[0].value(1)
            columnpin[4].value(0)
            sleep(x/1000)
            columnpin[4].value(1)
            columnpin[8].value(0)
            sleep(x/1000)
            columnpin[8].value(1)
            columnpin[12].value(0)
            sleep(x/1000)
            columnpin[12].value(1)
            columnpin[13].value(0)
            sleep(x/1000)
            columnpin[13].value(1)
            columnpin[15].value(0)
            sleep(x/1000)
            columnpin[15].value(1)
            columnpin[14].value(0)
            sleep(x/1000)
            columnpin[14].value(1)
            columnpin[11].value(0)
            sleep(x/1000)
            columnpin[11].value(1)
            columnpin[7].value(0)
            sleep(x/1000)
            columnpin[7].value(1)
            columnpin[3].value(0)
            sleep(x/1000)
            columnpin[3].value(1)
            columnpin[2].value(0)
            sleep(x/1000)
            columnpin[2].value(1)
            columnpin[1].value(0)
            sleep(x/1000)
            columnpin[1].value(1)
def randomflicker():
    print("--->Performing Random Flicker\n")
    turnEverythingOff()
    x=10
    for i in range(0,750,2):
        randomLayer = randint(0,3)
        randomColumn = randint(0,15)

        layerpin[randomLayer].value(1)
        columnpin[randomColumn].value(0)
        sleep(x/1000)
        layerpin[randomLayer].value(0)
        columnpin[randomColumn].value(1)
        sleep(x/1000)
def randomRain():
    print("--->Performing Random Rain\n")
    turnEverythingOff()
    x=100
    for i in range(0,80,2):
        randomColumn=randint(0,15)
        columnpin[randomColumn].value(0)
        layerpin[3].value(1)
        sleep((x+50)/1000)
        layerpin[3].value(0)
        layerpin[2].value(1)
        sleep(x/1000)
        layerpin[2].value(0)
        layerpin[1].value(1)
        sleep(x/1000)
        layerpin[1].value(0)
        layerpin[0].value(1)
        sleep((x+50)/1000)
        layerpin[0].value(0)
        columnpin[randomColumn].value(1)
def diagonalRectangle():
    print("--->Performing Diagonal Rectangle\n")
    x=350
    turnEverythingOff()
    for count in range(0,5):
        #top left
        for i in range(0,8):
            columnpin[i].value(0)
        layerpin[3].value(1)
        layerpin[2].value(1)
        sleep(x/1000)
        turnEverythingOff()
        #middle
        for i in range(4,12):
            columnpin[i].value(0)
        layerpin[1].value(1)
        layerpin[2].value(1)
        sleep(x/1000)
        turnEverythingOff()
        #bottom right
        for i in range(8,16):
            columnpin[i].value(0)
        layerpin[0].value(1)
        layerpin[1].value(1)
        sleep(x/1000)
        turnEverythingOff()
        #bottom middle
        for i in range(4,12):
            columnpin[i].value(0)
        layerpin[0].value(1)
        layerpin[1].value(1)
        sleep(x/1000)
        turnEverythingOff()
        #bottom left
        for i in range(0,8):
            columnpin[i].value(0)
        layerpin[0].value(1)
        layerpin[1].value(1)
        sleep(x/1000)
        turnEverythingOff()
        #middle middle
        for i in range(4,12):
            columnpin[i].value(0)
        layerpin[1].value(1)
        layerpin[2].value(1)
        sleep(x/1000)
        turnEverythingOff()
        #top right
        for i in range(8,16):
            columnpin[i].value(0)
        layerpin[2].value(1)
        layerpin[3].value(1)
        sleep(x/1000)
        turnEverythingOff()
        #top middle
        for i in range(4,12):
            columnpin[i].value(0)
        layerpin[2].value(1)
        layerpin[3].value(1)
        sleep(x/1000)
        turnEverythingOff()
        #top left
        for i in range(0,8):
            columnpin[i].value(0)
        layerpin[3].value(1)
        layerpin[2].value(1)
        sleep(x/1000)
        turnEverythingOff()
def goThroughAllLedsOneAtATime():
    print("--->Performing Go through all leds one at a time\n")
    x=15
    turnEverythingOff()
    for y in range(0,5):
        #0-3
        for count in range(4,0,-1):
            layerpin[count-1].value(1)
            for i in range(0,4):
                columnpin[i].value(0)
                sleep(x/1000)
                columnpin[i].value(1)
                sleep(x/1000)
            layerpin[count-1].value(0)
        #4-7
        for count in range(0,4):
            layerpin[count].value(1)
            for i in range(4,8):
                columnpin[i].value(0)
                sleep(x/1000)
                columnpin[i].value(1)
                sleep(x/1000)
            layerpin[count].value(0)
        #8-11
        for count in range(4,0,-1):
            layerpin[count-1].value(1)
            for i in range(8,12):
                columnpin[i].value(0)
                sleep(x/1000)
                columnpin[i].value(1)
                sleep(x/1000)
            layerpin[count-1].value(0)
        #12-15
        for count in range(0,4):
            layerpin[count].value(1)
            for i in range(12,16):
                columnpin[i].value(0)
                sleep(x/1000)
                columnpin[i].value(1)
                sleep(x/1000)
            layerpin[count].value(0)
def propeller():
    print("--->Performing Propeller\n")
    turnEverythingOff()
    x=90
    for y in range(4,0,-1):
        for i in range(0,16):
            #turn on all layers
            layerpin[y-1].value(1)
            #a1
            turnColumnsOff()
            columnpin[0].value(0)
            columnpin[5].value(0)
            columnpin[10].value(0)
            columnpin[15].value(0)
            sleep(x/1000)
            #b1
            turnColumnsOff()
            columnpin[4].value(0)
            columnpin[5].value(0)
            columnpin[10].value(0)
            columnpin[11].value(0)
            sleep(x/1000)
            #c1
            turnColumnsOff()
            columnpin[6].value(0)
            columnpin[7].value(0)
            columnpin[8].value(0)
            columnpin[9].value(0)
            sleep(x/1000)
            #d1
            turnColumnsOff()
            columnpin[3].value(0)
            columnpin[6].value(0)
            columnpin[9].value(0)
            columnpin[12].value(0)
            sleep(x/1000)
            #d2
            turnColumnsOff()
            columnpin[2].value(0)
            columnpin[6].value(0)
            columnpin[9].value(0)
            columnpin[13].value(0)
            sleep(x/1000)
            #d3
            turnColumnsOff()
            columnpin[1].value(0)
            columnpin[5].value(0)
            columnpin[10].value(0)
            columnpin[14].value(0)
            sleep(x/1000)
    #d4
    turnColumnsOff()
    columnpin[0].value(0)
    columnpin[5].value(0)
    columnpin[10].value(0)
    columnpin[15].value(0)
    sleep(x/1000)
def spiralInAndOut():
    print("--->Performing Spiral In and Out\n")
    turnEverythingOn()
    x=60
    for i in range(0,6):

        #spiral in CW
        columnpin[0].value(1)
        sleep(x/1000)
        columnpin[1].value(1)
        sleep(x/1000)
        columnpin[2].value(1)
        sleep(x/1000)
        columnpin[3].value(1)
        sleep(x/1000)
        columnpin[7].value(1)
        sleep(x/1000)
        columnpin[11].value(1)
        sleep(x/1000)
        columnpin[15].value(1)
        sleep(x/1000)
        columnpin[14].value(1)
        sleep(x/1000)
        columnpin[13].value(1)
        sleep(x/1000)
        columnpin[12].value(1)
        sleep(x/1000)
        columnpin[8].value(1)
        sleep(x/1000)
        columnpin[4].value(1)
        sleep(x/1000)
        columnpin[5].value(1)
        sleep(x/1000)
        columnpin[6].value(1)
        sleep(x/1000)
        columnpin[10].value(1)
        sleep(x/1000)
        columnpin[9].value(1)
        sleep(x/1000)

        #spiral out CCW
        columnpin[9].value(0)
        sleep(x/1000)
        columnpin[10].value(0)
        sleep(x/1000)
        columnpin[6].value(0)
        sleep(x/1000)
        columnpin[5].value(0)
        sleep(x/1000)
        columnpin[4].value(0)
        sleep(x/1000)
        columnpin[8].value(0)
        sleep(x/1000)
        columnpin[12].value(0)
        sleep(x/1000)
        columnpin[13].value(0)
        sleep(x/1000)
        columnpin[14].value(0)
        sleep(x/1000)
        columnpin[15].value(0)
        sleep(x/1000)
        columnpin[11].value(0)
        sleep(x/1000)
        columnpin[7].value(0)
        sleep(x/1000)
        columnpin[3].value(0)
        sleep(x/1000)
        columnpin[2].value(0)
        sleep(x/1000)
        columnpin[1].value(0)
        sleep(x/1000)
        columnpin[0].value(0)
        sleep(x/1000)

        #spiral in CCW
        columnpin[0].value(1)
        sleep(x/1000)
        columnpin[4].value(1)
        sleep(x/1000)
        columnpin[8].value(1)
        sleep(x/1000)
        columnpin[12].value(1)
        sleep(x/1000)
        columnpin[13].value(1)
        sleep(x/1000)
        columnpin[14].value(1)
        sleep(x/1000)
        columnpin[15].value(1)
        sleep(x/1000)
        columnpin[11].value(1)
        sleep(x/1000)
        columnpin[7].value(1)
        sleep(x/1000)
        columnpin[3].value(1)
        sleep(x/1000)
        columnpin[2].value(1)
        sleep(x/1000)
        columnpin[1].value(1)
        sleep(x/1000)
        columnpin[5].value(1)
        sleep(x/1000)
        columnpin[9].value(1)
        sleep(x/1000)
        columnpin[10].value(1)
        sleep(x/1000)
        columnpin[6].value(1)
        sleep(x/1000)

        #spiral out CW
        columnpin[6].value(0)
        sleep(x/1000)
        columnpin[10].value(0)
        sleep(x/1000)
        columnpin[9].value(0)
        sleep(x/1000)
        columnpin[5].value(0)
        sleep(x/1000)
        columnpin[1].value(0)
        sleep(x/1000)
        columnpin[2].value(0)
        sleep(x/1000)
        columnpin[3].value(0)
        sleep(x/1000)
        columnpin[7].value(0)
        sleep(x/1000)
        columnpin[11].value(0)
        sleep(x/1000)
        columnpin[15].value(0)
        sleep(x/1000)
        columnpin[14].value(0)
        sleep(x/1000)
        columnpin[13].value(0)
        sleep(x/1000)
        columnpin[12].value(0)
        sleep(x/1000)
        columnpin[8].value(0)
        sleep(x/1000)
        columnpin[4].value(0)
        sleep(x/1000)
        columnpin[0].value(0)
        sleep(x/1000)
def flickerOff():
    print("--->Performing Flicker Off\n")
    turnEverythingOn()
    for i in range(0,150,5):
        turnEverythingOff()
        sleep((i+50)/1000)
        turnEverythingOn()
        sleep(i/1000)

setup()
"""-----------------------------Web Page-----------------------"""

actval=8668
def web_page():

    html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1>
    <p><a href="/?actval=0"><button class="button">All Act</button></a></p>
    <p><a href="/?actval=1"><button class="button button1">Act 1</button></a></p>
    <p><a href="/?actval=2"><button class="button button2">Act 2</button></a></p>
    <p><a href="/?actval=3"><button class="button button3">Act 3</button></a></p>
    <p><a href="/?actval=4"><button class="button button4">Act 4</button></a></p>
    <p><a href="/?actval=5"><button class="button button5">Act 5</button></a></p>
    <p><a href="/?actval=6"><button class="button button6">Act 6</button></a></p>
    <p><a href="/?actval=7"><button class="button button7">Act 7</button></a></p>
    <p><a href="/?actval=8"><button class="button button8">Act 8</button></a></p>
    <p><a href="/?actval=9"><button class="button button9">Act 9</button></a></p>
    <p><a href="/?actval=10"><button class="button button10">Act 10</button></a></p>
    <p><a href="/?actval=11"><button class="button button11">Act 11</button></a></p>
    <p><a href="/?actval=12"><button class="button button12">Act 12</button></a></p>
    <p><a href="/?actval=13"><button class="button button13">Act 13</button></a></p>
    </body></html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  all_act_req = request.find('/?actval=0')
  act_1_req = request.find('/?actval=1')
  act_2_req = request.find('/?actval=2')
  act_3_req = request.find('/?actval=3')
  act_4_req = request.find('/?actval=4')
  act_5_req = request.find('/?actval=5')
  act_6_req = request.find('/?actval=6')
  act_7_req = request.find('/?actval=7')
  act_8_req = request.find('/?actval=8')
  act_9_req = request.find('/?actval=9')
  act_10_req = request.find('/?actval=10')
  act_11_req = request.find('/?actval=11')
  act_12_req = request.find('/?actval=12')
  act_13_req = request.find('/?actval=13')

  if all_act_req == 6:
    print('All Act')
    all_act()
  if act_1_req == 6:
    print('Act 1')
    act_1()
  if act_2_req == 6:
    print('Act 2')
    act_2()
  if act_3_req == 6:
    print('Act 3')
    act_3()
  if act_4_req == 6:
    print('Act 4')
    act_4()
  if act_5_req == 6:
    print('Act 5')
    act_5()
  if act_6_req == 6:
    print('Act 6')
    act_6()
  if act_7_req == 6:
    print('Act 7')
    act_7()
  if act_8_req == 6:
    print('Act 8')
    act_8()
  if act_9_req == 6:
    print('Act 9')
    act_9()
  if act_10_req == 6:
    print('Act 10')
    act_10()
  if act_11_req == 6:
    print('Act 11')
    act_11()
  if act_12_req == 6:
    print('Act 12')
    act_12()
  if act_13_req == 6:
    print('Act 13')
    act_13()

  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
