import time

import cv2
import mss
import numpy as np
from PIL import Image


with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 40, "left": 0, "width": 800, "height": 640}

    while "Screen capturing":
        last_time = time.time()

        sct_img = sct.grab(monitor)

        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        
        img = np.array(img)
        
        print(img.shape)
        cv2.imshow("OpenCV/Numpy normal", cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
