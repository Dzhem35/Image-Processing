
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)


img = cv2.imread('apple.jpeg')
gammaImg1 = gammaCorrection(img, 3.0)
gammaImg2 = gammaCorrection(img, 4.0)
gammaImg3 = gammaCorrection(img, 5.0)

cv2.putText(gammaImg1, "g={3.0}", (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
cv2.putText(gammaImg2, "g={4.0}", (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
cv2.putText(gammaImg3, "g={5.0}", (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

cv2_imshow(np.hstack((img,gammaImg1,gammaImg2,gammaImg3)))
