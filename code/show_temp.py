
import time
import board
import adafruit_mcp9600
from adafruit_is31fl3731.matrix import Matrix
import adafruit_imageload

# i2c scan
# [103, 116, 117, 118]
# 0x67 = MCP9600
# 0x74-0x76 = IS31

DIGITS = "digits.bmp"
DELAY = 1

digits = (
    Matrix(board.I2C(), address=0x74),
    Matrix(board.I2C(), address=0x75),
    Matrix(board.I2C(), address=0x76),
)

mcp = adafruit_mcp9600.MCP9600(board.I2C())

bmp, _ = adafruit_imageload.load(DIGITS)

def show_digit(n, s=255):
    d0 = n % 10
    d1 = (n // 10) % 10
    d2 = (n // 100) % 10

    if d2 == 0:
        d2 = 10
    if d2 == 10 and d1 == 0:
        d1 = 10

    for dig in digits:
        dig.fill(0)

    for x in range(16):
        for y in range(9):
            digits[0].pixel(15-x, y, s*bmp[y+9*d0, x])
            digits[1].pixel(15-x, y, s*bmp[y+9*d1, x])
            digits[2].pixel(15-x, y, s*bmp[y+9*d2, x])

while True:
    show_digit(int(32 + 1.8 * mcp.temperature))
    time.sleep(DELAY)
