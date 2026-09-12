import cv2
import mediapipe as mp

# read image
img_path = 'data/faceImage.jpg'
img = cv2.imread(img_path)

# detect faces
mp_face_detections = mp.solutions.face_detection

with mp_face_detections.FaceDetection(model_selection=0,min_detection_confidence=0.5) as face_detection:
    pass