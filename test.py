import mss
import mss.tools
import time
import cv2
import numpy


# 1024x640 windowed mode
mon = {"top": 30, "left": 0, "width": 970, "height": 550}

title = "[MSS] FPS benchmark"
fps = 0
sct = mss.mss()
last_time = time.time()

while (True):
    img = numpy.asarray(sct.grab(mon))
    print(img.shape)
    #fps += 1
    #print(fps)
    cv2.imshow(title, img)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

