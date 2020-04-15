import cv2

SEUIL_COUPURE = 1.7
SEUIL_FONDU = 2.4

histogram1 = None
currentFade = False
start = 0
end = 0


def getHistogram(image):
    result = []
    # Histogramme pour le bleu
    hBlue = cv2.calcHist([image], [0], None, [256], [0, 256])
    # Histogramme pour le vert
    hGreen = cv2.calcHist([image], [1], None, [256], [0, 256])
    # Histogramme pour le rouge
    hRed = cv2.calcHist([image], [2], None, [256], [0, 256])
    # Mise en commun des histogrammes
    result.append(hBlue)
    result.append(hGreen)
    result.append(hRed)
    return result


def calculateDistance(hist1=None, hist2=None):
    distance = 0
    for i in range(3):
        # Correlation des histogrammes de chaque couleur
        distance += cv2.compareHist(hist1[i],
                                    hist2[i], cv2.HISTCMP_CORREL)
    return distance


def methodHistogram(frame, frameNb):
    global histogram1, currentFade, start, end
    if frameNb == 1:
        histogram1 = getHistogram(frame)
    else:
        histogram2 = getHistogram(frame)
        # Distance pour comparer les deux histogrammes
        distance = calculateDistance(histogram1, histogram2)
        # Critere pour la coupure
        if distance <= SEUIL_COUPURE and not currentFade:
            print("CUT " + str(frameNb))
        # Critere pour le fondu
        elif distance <= SEUIL_FONDU:
            if not currentFade:
                currentFade = True
                start = frameNb
        else:
            if currentFade:
                currentFade = False
                end = frameNb
                print("fade " + str(start) + " - " + str(end))
        histogram1 = histogram2
