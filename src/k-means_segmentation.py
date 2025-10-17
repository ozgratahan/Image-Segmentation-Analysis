import cv2
import numpy as np
from skimage.morphology import closing, disk
from sklearn.cluster import KMeans


def k_means(image, k=2, closing_radius=5):
    Z = image.reshape((-1, 3)).astype(np.float32)
    labels = KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(Z)
    labels = labels.reshape(image.shape[:2])


    vals, counts = np.unique(labels, return_counts=True)
    fg_label = vals[np.argmax(counts)]
    mask = (labels == fg_label).astype(np.uint8)

    if closing_radius > 0:
        mask = closing(mask, disk(closing_radius)).astype(np.uint8)

    return mask