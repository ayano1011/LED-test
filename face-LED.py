from sense_hat import SenseHat
# from faces import normal, happy, sad
from time import sleep

sense = SenseHat()

r = (255, 0, 0)     # red
o = (255, 128, 0)   # orange
y = (255, 255, 0)   # yellow
g = (0, 255, 0)     # green
c = (0, 255, 255)   # cyan
b = (0, 0, 255)     # blue
p = (255, 0, 255)   # purple
n = (255, 128, 128) # pink
w = (255, 255, 255) # white
k = (0, 0, 0)       # blank


sense.set_pixels(sad)
sleep(1)
sense.set_pixels(normal)
sleep(1)
sense.set_pixels(happy)

#set-pixelsでLED1つずつを制御して顔を出力
happy = [
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, r, w, w, r, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, r, w, w, w, w, r, w,
w, w, r, r, r, r, w, w,
w, w, w, w, w, w, w, w
]

sad = [
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, r, w, w, r, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, r, r, r, r, w, w,
w, r, w, w, w, w, r, w,
w, w, w, w, w, w, w, w
]

normal = [
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, r, w, w, r, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, r, r, r, r, r, r, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w
]

sense.set_pixels(sad)
sleep(1)
sense.set_pixels(normal)
sleep(1)
sense.set_pixels(happy)
