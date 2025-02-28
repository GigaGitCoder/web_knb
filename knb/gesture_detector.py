import cv2
import mediapipe as mp
import os
import logging

# Suppress MediaPipe log messages
logging.getLogger('mediapipe').setLevel(logging.ERROR)
# Suppress absl log messages
logging.getLogger('absl').setLevel(logging.ERROR)

class GestureDetector:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=1,
            min_detection_confidence=0.5
        )

    def detect_gesture(self, image):
        # Convert to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image_rgb)

        if results.multi_hand_landmarks:
            landmarks = results.multi_hand_landmarks[0]
            wrist_y = landmarks.landmark[0].y
            middle_finger_y = landmarks.landmark[12].y
            is_inverted = middle_finger_y > wrist_y
            
            finger_count = 0
            
            if (not is_inverted and landmarks.landmark[4].x > landmarks.landmark[3].x) or \
               (is_inverted and landmarks.landmark[4].x < landmarks.landmark[3].x):
                finger_count += 1
                
            for tip_id in [8, 12, 16, 20]:
                if (not is_inverted and landmarks.landmark[tip_id].y < landmarks.landmark[tip_id - 2].y) or \
                   (is_inverted and landmarks.landmark[tip_id].y > landmarks.landmark[tip_id - 2].y):
                    finger_count += 1
            
            if finger_count <= 1:
                return "Камень"
            elif 2 <= finger_count <= 3:
                return "Ножницы"
            else:
                return "Бумага"
        
        return "Рука не обнаружена"

    def process_images(self):
        for filename in os.listdir(self.folder_path):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(self.folder_path, filename)
                try:
                    image = cv2.imread(image_path)
                    result = self.detect_gesture(image)
                    print(f"Файл: {filename}, Определенный жест: {result}")
                except Exception as e:
                    print(f"Подробности ошибки для файла {filename}: {str(e)}")
                    import traceback
                    traceback.print_exc()
