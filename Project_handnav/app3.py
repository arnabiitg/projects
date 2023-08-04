import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)
hands = mp.solutions.hands
hand = hands.Hands(static_image_mode = True)
draw = mp.solutions.drawing_utils

while True:
    check, frame = cam.read()


    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = hand.process(img)

    if image.multi_hand_landmarks:
        for i in image.multi_hand_landmarks:
            draw.draw_landmarks(frame, i, hands.HAND_CONNECTIONS)
    
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()