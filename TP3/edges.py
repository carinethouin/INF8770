import cv2
import numpy as np

SEUIL_EFFET = 8

edges1 = None
dilatedE1 = None
prevP = 0
highP = 0
currentEffect = False
start = 0
end = 0


def getEdges(image):
    # Image en gris
    imageGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Lignes et colonnes additionnelles
    col = imageGrey[:, 0]
    imageGrey = np.column_stack((col, imageGrey))
    col = imageGrey[:, len(imageGrey[0])-1]
    imageGrey = np.column_stack((imageGrey, col))
    row = imageGrey[0, :]
    imageGrey = np.row_stack((row, imageGrey))
    row = imageGrey[len(imageGrey)-1, :]
    imageGrey = np.row_stack((imageGrey, row))
    # Filtres de Sobel
    sX = cv2.Sobel(imageGrey, cv2.CV_64F, 1, 0, ksize=3)
    sY = cv2.Sobel(imageGrey, cv2.CV_64F, 0, 1, ksize=3)
    ForceGradient = np.sqrt(np.power(sX, 2) + np.power(sY, 2))
    ret, edges = cv2.threshold(ForceGradient, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    dilatedE = cv2.dilate(edges, kernel, iterations=1)
    return edges, dilatedE


def calculateInOutEdges(edges1, dilatedE1, edges2, dilatedE2):
    # Aretes entrantes
    eIn = 1 - ((np.sum(np.multiply(dilatedE1, edges2))) / (np.sum(edges2)))
    # Aretes sortantes
    eOut = 1 - ((np.sum(np.multiply(edges1, dilatedE2))) / (np.sum(edges1)))
    return eIn, eOut


def methodEdges(frame, frameNb):
    global edges1, dilatedE1, prevP, highP, currentEffect, start, end
    if frameNb == 1:
        edges1, dilatedE1 = getEdges(frame)
    else:
        edges2, dilatedE2 = getEdges(frame)
        # Calcul des aretes pour comparer les deux images
        eIn, eOut = calculateInOutEdges(
            edges1, dilatedE1, edges2, dilatedE2)
        p = max(eIn, eOut)
        # Effet
        if abs(p - prevP) >= SEUIL_EFFET:
            start = frameNb
            highP = p
            currentEffect = True
        else:
            if currentEffect and abs(p - highP) >= 1:
                currentEffect = False
                end = frameNb
                if (end - start) == 1:
                    print("CUT " + str(frameNb))
                else:
                    print("fade " + str(start) + " - " + str(end))
        prevP = p
        edges1 = edges2
        dilatedE1 = dilatedE2
