import cv2
import numpy as np


class VideoReader:
    def __init__(self):
        pass
    """
    Returns an array-like of dimensions (n_images, width, height, channels)
    n_images: the number of images after the video was spliced
    width: width of image
    height: height of image
    channels: # of color channels
    
    This function takes in dictionary (process_dict) which specifies the transforms needed to be applied onto the spliced images.
    
    The possible keys-value pairs of the dictionary are:
    - kernel_transforms : List[str], executed by order
    - colorspace_transform: str
    """
    def process_video(self, process_dict):
        #TODO, implement the function in the docstring