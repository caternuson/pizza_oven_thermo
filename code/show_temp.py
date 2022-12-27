
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

# setup IS31FL3731 matrix displays
digits = (
    Matrix(board.I2C(), address=0x74), # ones place
    Matrix(board.I2C(), address=0x75), # tens place
    Matrix(board.I2C(), address=0x76), # hundreds place
)

# setup MCP9600 thermocouple
mcp = adafruit_mcp9600.MCP9600(board.I2C())

# load sprite sheet
bmp, _ = adafruit_imageload.load(DIGITS)

# clear displays and set draw frame
for dig in digits:
    dig.fill(0)
last_frame = 1

def show_digit(n, s=255):
    """
    Show the integer value on the matrices.

    :param n: The digit to show, 0-999.
    :param s: Brightness, 0-255.
    """

    # compute sprite sheet index for each digit
    d0 = n % 10
    d1 = (n // 10) % 10
    d2 = (n // 100) % 10

    # blank left padding
    if d2 == 0:
        d2 = 10
    if d2 == 10 and d1 == 0:
        d1 = 10

    # draw into background frame
    for i in range(3):
        digits[i].frame(last_frame, show=False)

    # clear display
    for dig in digits:
        dig.fill(0)

    # draw sprite sheet graphic onto display
    for x in range(16):
        for y in range(9):
            digits[0].pixel(15-x, y, s*bmp[y+9*d0, x])
            digits[1].pixel(15-x, y, s*bmp[y+9*d1, x])
            digits[2].pixel(15-x, y, s*bmp[y+9*d2, x])

    # show frame on display
    for i in range(3):
        digits[i].frame(last_frame, show=True)

    # toggle background frame and return
    return 0 if last_frame else 1

while True:
    last_frame = show_digit(int(32 + 1.8 * mcp.temperature))
    time.sleep(DELAY)
