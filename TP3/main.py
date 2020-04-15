import cv2
import histograms
import edges

FILE_NAME = "anni009.mpg"


def process_video(file: str, option):
    frameNb = 0
    cap = cv2.VideoCapture(file)
    print("Methode " + str(option))
    print("Name " + file)
    while(True):
        frameNb += 1
        ret, frame = cap.read()
        if ret:
            if option == 1:
                histograms.methodHistogram(frame, frameNb)
            if option == 2:
                edges.methodEdges(frame, frameNb)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


process_video(FILE_NAME, 2)
