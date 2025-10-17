import cv2
import numpy as np
from skimage.morphology import closing, disk
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from scipy import ndimage as ndi

def watershed_segmentation(image, footprint=3, closing_radius=0):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    distance = ndi.distance_transform_edt(binary)

    coords = peak_local_max(distance, labels=binary, footprint=np.ones((footprint, footprint)))
    local_max = np.zeros_like(distance, dtype=bool)
    if coords.size > 0:
        local_max[tuple(coords.T)] = True

    markers = ndi.label(local_max)[0]

    labels = watershed(-distance, markers, mask=binary)

    mask = (labels > 0).astype(np.uint8)

    if closing_radius > 0:
        mask = closing(mask, disk(closing_radius)).astype(np.uint8)

    return mask