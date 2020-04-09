import cv2
import numpy as np

"""
This function should process the video file.
Input: 
- file: the path to the video
Output:
- cut: vector of frame indices where cuts are detected
- grad: vector of tuples (start, end) of frame indices where gradations are detected
"""
def process_video(file: str):
	cut=[]
	grad=[]
	cap = cv2.VideoCapture(file)
	while(True):
		ret, frame = cap.read()
		if ret:
			#TODO : frame processing algorithm

			cv2.imshow('frame', frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		else:
			break
	cap.release()
	cv2.destroyAllWindows()
	return cut, grad

"""
This function provides the ground truth for a given video file.
Input: 
- file: the path to the video
Output:
- cut: vector of frame indices where cuts happen
- grad: vector of tuples (start, end) of frame indices where gradations happen
"""
def read_groundtruth(file: str):
	cut=[]
	grad=[]
	f = open(file, "r")
	line = f.readline().split()
	while(line != []):
		if len(line)==1:
			cut.append(int(line[0]))
		elif len(line)==2:
			grad.append([int(line[0]), int(line[1])])
		line = f.readline().split()
	return cut, grad

cut, grad = process_video('anni005.mpg')
gt_cut, gt_grad = read_groundtruth('anni005.txt')

#TODO : results analysis
