import turtle as t
import math

t.tracer(5)
# A=base B=right side C=hypotenuse
# Works out the top right angle form the side lengths
def angles(aLen, bLen, cLen):
    aLenSquare = aLen**2
    bLenSquare = bLen**2
    cLenSquare = cLen**2
    
    divTop = bLenSquare+cLenSquare-aLenSquare
    divBottom = 2*bLen*cLen
    
    unCos = divTop/divBottom
    
    angle = math.degrees(math.acos(unCos))
    
    return angle

def drawHouse(height=50):
    hypotenuse = math.sqrt(height**2+(height*2)**2)
    angleA = angles(height*2, height, hypotenuse)
    angleB = 180-90-angleA
    
    t.pendown()
    t.setheading(-60)
    t.fd(height*2)
    
    t.setheading(angleB+180)
    t.fd(hypotenuse) # Pythagoras :D
    
    t.setheading(0)
    t.fd(height*2)
    
    t.setheading(180) # No don't worry, i'm *not* cheating
    t.fd(height*2)
    
    
    t.setheading(90)
    t.fd(height)
    
    t.setheading(angleA+270)
    t.fd(hypotenuse) # Pythagoras :D
    
    t.setheading(90)
    t.fd(height)
    
    t.setheading(180)
    t.fd(height*2)
    
    t.setheading(60)
    t.fd(height*2)


drawHouse(100)
t.update()
t.Screen().exitonclick()