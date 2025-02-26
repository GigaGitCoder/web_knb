import cv2
import mediapipe as mp


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
        
        # Подсчет поднятых пальцев
        finger_count = 0
        
        # Проверяем большой палец
        if landmarks.landmark[4].x > landmarks.landmark[3].x:
            finger_count += 1
            
        # Проверяем остальные пальцы
        for tip_id in [8, 12, 16, 20]:  # Индексы кончиков пальцев
            if landmarks.landmark[tip_id].y < landmarks.landmark[tip_id - 2].y:
                finger_count += 1
        
        # Определение жеста
        if finger_count <= 1:
            return "Камень"
        elif 2 <= finger_count <= 3:
            return "Ножницы"
        else:
            return "Бумага"
        
    return "Рука не обнаружена"

def main():
    # Путь к изображению
    image_path = "hand.jpg"
    
    try:
        image = cv2.imread(image_path)
        result = detect_gesture(image)
        # Добавляем кодировку для корректного отображения русских букв
        print(f"Определенный жест: {result}".encode('utf-8').decode(encoding='cp1251'))
        
    except Exception as e:
        print(f"Подробности ошибки: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()