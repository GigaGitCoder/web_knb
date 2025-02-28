import cv2
import mediapipe as mp
import os
import logging

# Suppress MediaPipe log messages
logging.getLogger('mediapipe').setLevel(logging.ERROR)
logging.getLogger('absl').setLevel(logging.ERROR)
os.environ['GLOG_minloglevel'] = '2'

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

def detect_gesture(landmarks):
    # Check hand orientation
    wrist_y = landmarks[0].y
    middle_finger_y = landmarks[12].y
    is_inverted = middle_finger_y > wrist_y
    
    finger_count = 0
    # Check thumb
    if (not is_inverted and landmarks[4].x > landmarks[3].x) or \
       (is_inverted and landmarks[4].x < landmarks[3].x):
        finger_count += 1
        
    # Check other fingers
    for tip_id in [8, 12, 16, 20]:
        if (not is_inverted and landmarks[tip_id].y < landmarks[tip_id - 2].y) or \
           (is_inverted and landmarks[tip_id].y > landmarks[tip_id - 2].y):
            finger_count += 1
            
    if finger_count <= 1:
        return "Rock"
    elif 2 <= finger_count <= 3:
        return "Scissors"
    else:
        return "Paper"

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = detect_gesture(hand_landmarks.landmark)
            cv2.putText(image, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Hand Gesture Recognition', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()