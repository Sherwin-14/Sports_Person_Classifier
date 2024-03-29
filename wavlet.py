import pywt
import cv2
import numpy as np

def w2d(img,mode='haar',level=1):
    imArray= img
    # Datatype conversions
    # Convert to grayscale
    imArray=cv2.cvtColor(imArray,cv2.COLOR_BGR2GRAY)
    #convert to float
    imArray= np.float32(imArray)
    imArray/=255;
    # compute coefficents
    coeffs=pywt.wavedec2(imArray,mode,level=level)

    #process coefficients
    coeffs_H=list(coeffs)
    coeffs_H[0] *=0;

    #restruction
    imArray_H=pywt.waverec2(coeffs_H,mode)
    imArray_H *=255;
    imArray_H=np.uint8(imArray_H)

    return imArray_H