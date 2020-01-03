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
    while True:
        turnEverythingOn()
def act_2():
    while True:
        turnEverythingOff()
def act_3():
    while True:
        flickerOn()
def act_4():
    while True:
        layerstompUpAndDown()
def act_5():
    while True:
        turnOnAndOffAllByColumnSideways()
def act_6():
    while True:
        aroundEdgeDown()
def act_7():
    while True:
        randomflicker()
def act_8():
    while True:
        randomRain()
def act_9():
    while True:
        diagonalRectangle()
def act_10():
    while True:
        goThroughAllLedsOneAtATime()
def act_11():
    while True:
        propeller()
def act_12():
    while True:
        spiralInAndOut()
def act_13():
    while True:
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
all_act()
#act_9()
