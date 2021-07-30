from sense_hat import SenseHat
import time
import random

sense = SenseHat()

# set up the colours (white, red, green, empty)

w = [150, 150, 150]
r = [255, 0, 0]
g = [0, 255, 0]
e = [0, 0, 0]
o = [255,127,0]
y = [150, 150, 0]
b = [0, 0, 150]
i = [75, 0, 130]
v = [159,0,255]
e = [0,0,0]



arrow = [
e,e,e,w,w,e,e,e,
e,e,w,w,w,w,e,e,
e,w,e,w,w,e,w,e,
w,e,e,w,w,e,e,w,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e
]

arrow_red = [
e,e,e,r,r,e,e,e,
e,e,r,r,r,r,e,e,
e,r,e,r,r,e,r,e,
r,e,e,r,r,e,e,r,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e
]

arrow_green = [
e,e,e,g,g,e,e,e,
e,e,g,g,g,g,e,e,
e,g,e,g,g,e,g,e,
g,e,e,g,g,e,e,g,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e
]

full_rainbow = [
e,e,e,e,e,e,e,e,
e,e,e,r,r,e,e,e,
e,r,r,o,o,r,r,e,
r,o,o,y,y,o,o,r,
o,y,y,g,g,y,y,o,
y,g,g,b,b,g,g,y,
b,b,b,i,i,b,b,b,
b,i,i,v,v,i,i,b,
]

half_rainbow = [
e,e,e,e,e,e,e,e,
e,e,e,r,e,e,e,e,
e,r,r,o,e,e,e,e,
r,o,o,y,e,e,e,e,
o,y,y,g,e,e,e,e,
y,g,g,b,e,e,e,e,
b,b,b,i,e,e,e,e,
b,i,i,v,e,e,e,e,
]


pause = 4
lives = 2
score = 0
angle = 0
Life = 2

LifePause = 1

play = True

sense.show_message("Keep the arrow pointing up", scroll_speed=0.05, text_colour=[100,100,100])

while play:
    last_angle = angle
    while angle == last_angle:
        angle = random.choice([0, 90, 180, 270])
    sense.set_rotation(angle)
    sense.set_pixels(arrow)
    time.sleep(pause)

    x, y, z = sense.get_accelerometer_raw().values()   
    x = round(x, 0)
    y = round(y, 0)

    print(angle)
    print(x)
    print(y)

    if x == -1 and angle == 180:
        sense.set_pixels(arrow_green)
        score += 1
    elif x == 1 and angle == 0:
       sense.set_pixels(arrow_green)
       score += 1
    elif y == -1 and angle == 90:
        sense.set_pixels(arrow_green)
        score += 1  	
    elif y == 1 and angle == 270:
        sense.set_pixels(arrow_green)
        score += 1 


    else:
        sense.set_rotation(0)
        sense.set_pixels(arrow_red)
        time.sleep(2)
        sense.set_pixels(full_rainbow)
        time.sleep(2)
        
        Life -= 1

        sense.set_pixels(half_rainbow)
        
        time.sleep(2)

        if Life == 0:
    
            play = False

        
        
    pause = pause * 0.95
    time.sleep(0.5)

msg = "Your score was %s" % score

sense.show_message(msg, scroll_speed=0.05, text_colour=[100,100,100])
