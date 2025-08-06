import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Define hand gestures
gestures = {
    "fist": 0,
    "palm": 1,
    "thumb_up": 2,
    "thumb_down": 3,
    "index_finger_up": 4
}

# Function to recognize hand gestures
def recognize_gesture(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    # Fist gesture
    if (thumb_tip.y > index_tip.y and
        thumb_tip.y > middle_tip.y and
        thumb_tip.y > ring_tip.y and
        thumb_tip.y > pinky_tip.y):
        return gestures["fist"]

    # Palm gesture
    elif (thumb_tip.y < index_tip.y and
          thumb_tip.y < middle_tip.y and
          thumb_tip.y < ring_tip.y and
          thumb_tip.y < pinky_tip.y):
        return gestures["palm"]

    # Thumb up gesture
    elif (thumb_tip.y < index_tip.y and
          thumb_tip.x < index_tip.x):
        return gestures["thumb_up"]

    # Thumb down gesture
    elif (thumb_tip.y > index_tip.y and
          thumb_tip.x < index_tip.x):
        return gestures["thumb_down"]

    # Index finger up gesture
    elif (index_tip.y < middle_tip.y and
          index_tip.y < ring_tip.y and
          index_tip.y < pinky_tip.y):
        return gestures["index_finger_up"]

    else:
        return None

# Capture video from camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Convert image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process hand detection
    results = hands.process(image)

    # Draw hand landmarks and recognize gestures
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = recognize_gesture(hand_landmarks)
            if gesture is not None:
                cv2.putText(image, list(gestures.keys())[list(gestures.values()).index(gesture)], (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display output
    cv2.imshow('Hand Gesture Recognition', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Release resources
hands.close()
cap.release()
cv2.destroyAllWindows()