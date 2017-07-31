UP_ARROW="up"
LEFT_ARROW="left"
DOWN_ARROW="down"
RIGHT_ARROW="right" b
SPACEBAR="space"
UP=0
DOWN=2
LEFT=1
RIGHT=3



direction=UP
def up ():
    global direction
    direction=UP
    print('you pressed up')
def down():
    global direction
    direction=DOWN

def left():
    global direction
    direction=LEFT
    
def right():
    global direction
    direction=RIGHT
    
print(UP)
