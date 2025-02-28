import cv2
import mediapipe as mp
import os
import logging

# Suppress MediaPipe log messages
logging.getLogger('mediapipe').setLevel(logging.ERROR)
# Suppress absl log messages
logging.getLogger('absl').setLevel(logging.ERROR)
os.environ['GLOG_minloglevel'] = '2'


# Suppress MediaPipe log messages
logging.getLogger('mediapipe').setLevel(logging.ERROR)
# Suppress absl log messages
logging.getLogger('absl').setLevel(logging.ERROR)



def detect_gesture(image): 

    # Инициализация MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.5
    )
    
    # Конвертация в RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Определение руки на изображении
    results = hands.process(image_rgb)
    
    if results.multi_hand_landmarks:
        landmarks = results.multi_hand_landmarks[0]
        
        # Определяем ориентацию руки
        wrist_y = landmarks.landmark[0].y
        middle_finger_y = landmarks.landmark[12].y
        is_inverted = middle_finger_y > wrist_y
        
        # Подсчет поднятых пальцев
        finger_count = 0
        
        # Проверяем большой палец с учетом ориентации
        if (not is_inverted and landmarks.landmark[4].x > landmarks.landmark[3].x) or \
           (is_inverted and landmarks.landmark[4].x < landmarks.landmark[3].x):
            finger_count += 1
            
        # Проверяем остальные пальцы с учетом ориентации
        for tip_id in [8, 12, 16, 20]:  # Индексы кончиков пальцев
            if (not is_inverted and landmarks.landmark[tip_id].y < landmarks.landmark[tip_id - 2].y) or \
               (is_inverted and landmarks.landmark[tip_id].y > landmarks.landmark[tip_id - 2].y):
                finger_count += 1
        
        # Определение жеста
        if finger_count <= 1:
            return "Камень"
        elif 2 <= finger_count <= 3:
            return "Ножницы"
        else:
            return "Бумага"
        
    return "Рука не обнаружена"

import sys
from gesture_detector import GestureDetector

def main():
    # Путь к папке с изображениями
    if len(sys.argv) < 2:
        print("Использование: python hand_gesture_game.py <путь_к_папке>")
        return
    folder_path = sys.argv[1]  # Укажите путь к папке с изображениями
    detector = GestureDetector(folder_path)
    detector.process_images()

if __name__ == "__main__":
    main()
