import mss
import mss.tools
from PIL import Image
import numpy as np
with mss.mss() as sct:
    # Use the 1st monitor
    monitor = sct.monitors[1]

    # Capture a bbox using percent values
    left = monitor["left"] + monitor["width"] * 5 // 100  # 5% from the left
    top = monitor["top"] + monitor["height"] * 5 // 100  # 5% from the top
    right = left + 400  # 400px width
    lower = top + 400  # 400px height
    bbox = (left, top, right, lower)

    # Grab the picture
    # Using PIL would be something like:
    # im = ImageGrab(bbox=bbox)
    sct_img = sct.grab(bbox)
    #im = np.array(im)
    #print(im.shape)
    # Save it!
    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    #print(screenshot)
    #img = Image.open("screenshot.png")
    #img.show()
    img = np.array(img)
    print(img.shape)
