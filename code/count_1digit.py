import time
import board
from adafruit_is31fl3731.matrix import Matrix
import adafruit_imageload

DIGITS = "digits.bmp"
DELAY = 0.2

disp = Matrix(board.I2C())

bmp, _ = adafruit_imageload.load(DIGITS)

def show_digit(n, s=255):
    disp.fill(0)
    for x in range(disp.width):
        for y in range(disp.height):
            disp.pixel(15-x, y, s*bmp[y+9*n, x])

while True:
    for i in range(10):
        show_digit(i)
        time.sleep(DELAY)
