import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands(max_num_hands = 1)
mpDraw = mp.solutions.drawing_utils

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print('Не удалось получить кадр с web-камеры')