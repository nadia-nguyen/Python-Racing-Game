overshape = 0
screen = 0
xposS = 0
xposP = 0
time = 4
def setup():
    size (960,720)

def draw ():
    global xposS
    global xposP
    global overshape
    global screen
    global t
    global time
    if screen == 0:
        pic = loadImage("krusty krab.jpg")
        background (pic)
        fill (0)
        t = createFont ("Comic Sans MS",100)
        textFont (t,36)
        textAlign(CENTER)
        text("The",300,100)
        text ("Krusty Krab", 305, 150)
        text ("Race",300,200)
        t = createFont ("Arial",100)
        textFont (t,75)
        textAlign (LEFT)
        noFill()
        noStroke()
        rect (0,325,200,100)
        if 0<=mouseX<=200 and 325<= mouseY <= 425:
            overshape = 1
            fill (255)
        text ("Start",0,400)
        if mousePressed and overshape == 1:
            screen = 1
    if screen == 1:
        background (0,100,200)
        textAlign (CENTER)
        textFont (t,50)
        text ("HOW TO PLAY",width/2,100)
        textFont (t,40)
        text ("Patrick: press 'm' to move",width/2,200)
        text ("Spongebob: press 'a' to move",width/2,250)
        if time > 0:
            time = time - 1
            textFont (t,60)
            fill (255)
            text (time,width/2,height/2)
            delay (1000)
        if time == 0:
            textFont (t,60)
            text ("Go!",width/2,height/2)
        textFont (t,35)
        text ("Be the first one to reach the krabby patty!", width/2,450)
        Patrick = loadImage ("patrick.png")
        Patrick.resize (100,100)
        Spongebob = loadImage ("spongebob.png")
        Spongebob.resize (100,100)
        kb = loadImage ("krabby patty.jpg")
        kb.resize (200,200)
        image (kb,700,500)
        image (Patrick, xposP,600)
        image (Spongebob,xposS,500)
        textAlign (CENTER)
        if xposS > 550 and xposP <=550:
            fill (0,100,200)
            rect(0,0,960,500)
            fill (255)
            textFont (t,60)
            text ("Spongebob wins!",width/2,height/2)
            textFont (t,30)
            text ("Click the mouse to play again", width/2,250)
            if mousePressed:
                screen = 0
                xposS = 0
                xposP = 0
                time = 4
                overshape = 0
        if xposP > 550 and xposS <=550:
            fill (0,100,200)
            rect(0,0,960,500)
            fill (255)
            textFont (t,60)
            text ("Patrick wins!",width/2,height/2)
            textFont (t,30)
            text ("Click the mouse to play again",width/2,250)
            if mousePressed:
                screen = 0
                xposS = 0
                xposP = 0
                time = 4
                overshape = 0
        if xposP == 650 and xposS == 650:
            textFont (t,60)
            text ("Tie!",width/2,height/2)
            textFont (t,30)
            text ("Click the mouse to play again",width/2,250)
            if mousePressed:
                screen = 0
                xposS = 0
                xposP = 0
                time = 4
                overshape = 0

def keyReleased ():
    global xposS
    global xposP
    global value
    if xposS <= 550 and xposP <= 550 and time == 0:
        if key == "a":
            xposS = xposS + 25
        if key == "m":
            xposP = xposP + 25
    if xposS >= 550 or xposP >= 550:
        xposS = xposS
        xposP = xposP

    
    