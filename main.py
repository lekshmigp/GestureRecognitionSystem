import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Define your fixed ROI box (adjust coordinates as needed)
x1, y1, x2, y2 = 200, 100, 450, 350  # (left, top, right, bottom)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    
    # Draw the ROI rectangle (green)
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    # Extract ROI for processing
    roi = frame[y1:y2, x1:x2]
    
    # Process only the ROI with MediaPipe
    rgb_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_roi)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks (optional, in ROI coordinates)
            mp_drawing.draw_landmarks(roi, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Count fingers
            finger_tips = [8, 12, 16, 20]  # Tip IDs for index, middle, ring, pinky
            finger_mcp = [6, 10, 14, 18]   # MCP joint IDs
            finger_count = 0

            # Check fingers (except thumb)
            for tip, mcp in zip(finger_tips, finger_mcp):
                if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[mcp].y:
                    finger_count += 1

            # Check thumb (right hand)
            if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
                finger_count += 1

            # Display custom text on the main frame
            cv2.putText(frame, f"The finger shows: {finger_count}", (x1, y1 - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Gesture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
