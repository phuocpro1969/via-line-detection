import os
import sys
py_file_location = "/content/line_detect/src"
if os.path.abspath(py_file_location) not in sys.path:
    sys.path.append(os.path.abspath(py_file_location))

import numpy as np
import cv2
import math
from parameters import Parameters
# from src.parameters import Parameters

p = Parameters()

def warp_image(img):
    
    image_size = (img.shape[1], img.shape[0])
    warped_img = cv2.warpPerspective(img, p.perspective_transform, image_size, flags=cv2.INTER_LINEAR)

    return warped_img




################## find line avaiable ######################
