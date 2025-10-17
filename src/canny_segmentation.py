import cv2
import numpy as np
from skimage.morphology import closing, disk

def canny(img, sigma=0.5, closing_radius=0):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    v = np.median(gray)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edges = cv2.Canny(gray, lower, upper)
    
    if closing_radius > 0:
        edges = closing(edges.astype(bool), disk(closing_radius)).astype(np.uint8)
    return edges