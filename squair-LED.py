from sense_hat import SenseHat
import time
import numpy as np
import time
import ect
from random import randint
import sys

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

#ランダムカラーの動く四角形
for x in range(5):
    ect.square(image, [0,0], [7,0], [7,7],[0,7],[randint(0,255),randint(0,255),randint(0,255)],.01)
    ect.square(image, [1,1], [6,1], [6,6],[1,6],[randint(0,255),randint(0,255),randint(0,255)],.01)
    ect.square(image, [2,2], [5,2], [5,5],[2,5],[randint(0,255),randint(0,255),randint(0,255)],.01)

#赤、ピンク、オレンジの動く四角形になるはず
for x in range(5):
    ect.square(image, [0,0], [7,0], [7,7],[0,7],[255,0,255],.01)
    ect.square(image, [1,1], [6,1], [6,6],[1,6],[255,0,0,],.01)
    ect.square(image, [2,2], [5,2], [5,5],[2,5],[255,128,0],.01)

#単色
sense.clear(255,192,0)