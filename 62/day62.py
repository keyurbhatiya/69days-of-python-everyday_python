
# AI Hand Tracking: Controlling Mouse with Gestures 🖐️ (Day 62)
# pip install opencv-python mediapipe pyautogui

import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["GLOG_minloglevel"] = "3"       # suppress MediaPipe logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"   # suppress TensorFlow logs

import cv2
import mediapipe as mp
import pyautogui
import math
import time

# --- Setup ---
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles

# Screen size for mapping hand position to cursor
screen_w, screen_h = pyautogui.size()
pyautogui.FAILSAFE = False  # allow cursor to reach edges

# Smoothing variables (reduces jitter)
smooth_x, smooth_y = 0, 0
smoothing = 5  # higher = smoother but slower

# Click debounce
last_click_time = 0
click_cooldown = 0.5  # seconds between clicks

print("🖐️ AI Hand Tracking Mouse | Day 62")
print("👆 Move index finger = Move cursor")
print("🤏 Pinch (index + thumb) = Click")
print("Press 'q' to quit\n")

# Webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ ERROR: Could not open webcam!")
    print("   Make sure your webcam is connected and not used by another app.")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cam_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Padding for movement area (don't need to reach edges of frame)
frame_margin = 100

# Initialize Hands detector inside a context manager
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while True:
        success, frame = cap.read()
        if not success:
            print("⚠️ Failed to read frame, retrying...")
            continue

        # Flip for mirror effect & convert to RGB
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb.flags.writeable = False  # performance boost

        # Process hand landmarks
        results = hands.process(rgb)
        rgb.flags.writeable = True

        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(
                frame, hand, mp_hands.HAND_CONNECTIONS,
                mp_styles.get_default_hand_landmarks_style(),
                mp_styles.get_default_hand_connections_style()
            )

            landmarks = hand.landmark

            # Index finger tip (landmark 8) & Thumb tip (landmark 4)
            index_tip = landmarks[8]
            thumb_tip = landmarks[4]

            # Convert to pixel coordinates
            ix = int(index_tip.x * cam_w)
            iy = int(index_tip.y * cam_h)
            tx = int(thumb_tip.x * cam_w)
            ty = int(thumb_tip.y * cam_h)

            # Draw circles on fingertips
            cv2.circle(frame, (ix, iy), 12, (0, 255, 255), cv2.FILLED)  # Index = Cyan
            cv2.circle(frame, (tx, ty), 12, (255, 0, 255), cv2.FILLED)  # Thumb = Magenta

            # --- Map index finger to screen coordinates ---
            move_x = max(frame_margin, min(ix, cam_w - frame_margin))
            move_y = max(frame_margin, min(iy, cam_h - frame_margin))

            target_x = int(((move_x - frame_margin) / (cam_w - 2 * frame_margin)) * screen_w)
            target_y = int(((move_y - frame_margin) / (cam_h - 2 * frame_margin)) * screen_h)

            # Smooth movement
            smooth_x += (target_x - smooth_x) / smoothing
            smooth_y += (target_y - smooth_y) / smoothing

            pyautogui.moveTo(int(smooth_x), int(smooth_y))

            # --- Pinch Detection (Click) ---
            distance = math.hypot(ix - tx, iy - ty)

            if distance < 35:
                # Pinch detected = Click! (with cooldown)
                current_time = time.time()
                cv2.circle(frame, ((ix + tx) // 2, (iy + ty) // 2), 20, (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, "CLICK!", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

                if current_time - last_click_time > click_cooldown:
                    pyautogui.click()
                    last_click_time = current_time
            else:
                cv2.putText(frame, "MOVE", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 3)

            # Draw line between thumb and index (visual feedback)
            cv2.line(frame, (ix, iy), (tx, ty), (255, 255, 0), 2)

        else:
            cv2.putText(frame, "No Hand Detected", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # UI overlay
        cv2.putText(frame, "Day 62 | Hand Tracking Mouse", (10, cam_h - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

        cv2.imshow("AI Hand Tracking - Day 62", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
print("✅ Hand tracking stopped.")
