import streamlit as st
import cv2
import mediapipe as mp
import os
import time
import webbrowser


st.set_page_config(page_title="✋ Computer Vision - Gesture Control", layout="centered")


st.markdown("""
<style>
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(to bottom right, #23074d, #cc5333);
        color: white;
        animation: fadeSlideIn 1.2s ease-in-out;
    }
    section[data-testid="stSidebar"] .css-1d391kg {
        color: #ffdd57 !important;
        font-size: 20px;
        font-weight: bold;
        padding-bottom: 10px;
    }
    section[data-testid="stSidebar"] a {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 0.6rem 1rem;
        margin: 5px 0;
        color: #fff !important;
        font-weight: 500;
        border: 1px solid #aaa;
        transition: all 0.3s ease-in-out;
        display: block;
        text-align: center;
    }
    section[data-testid="stSidebar"] a:hover {
        background-color: #fcd303;
        color: #1b1b1b !important;
        transform: scale(1.05);
        border-color: #fcd303;
        box-shadow: 0 0 10px rgba(0,0,0,0.3);
    }
    @keyframes fadeSlideIn {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
</style>
""", unsafe_allow_html=True)

st.title("✋ Computer Vision - Gesture Control")
st.write("Raise **1–5 fingers** to trigger different actions.")


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

last_finger_count = -1
last_action_time = time.time()

def detect_fingers(hand_landmarks, hand_label):
    tips_ids = [4, 8, 12, 16, 20]
    fingers = []

  
    if hand_label == "Left":
        fingers.append(1 if hand_landmarks.landmark[tips_ids[0]].x < hand_landmarks.landmark[tips_ids[0] - 1].x else 0)
    else:  
        fingers.append(1 if hand_landmarks.landmark[tips_ids[0]].x > hand_landmarks.landmark[tips_ids[0] - 1].x else 0)

    for id in range(1, 5):
        fingers.append(1 if hand_landmarks.landmark[tips_ids[id]].y < hand_landmarks.landmark[tips_ids[id] - 2].y else 0)

    return sum(fingers)


frame_placeholder = st.empty()

while True:
    ret, frame = cap.read()
    if not ret:
        st.error("Camera not found!")
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks and result.multi_handedness:
        for hand_landmarks, hand_handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            hand_label = hand_handedness.classification[0].label  
            finger_count = detect_fingers(hand_landmarks, hand_label)

            cv2.putText(frame, f"Fingers Up: {finger_count}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

            if finger_count != last_finger_count and (time.time() - last_action_time > 1.5):
                last_finger_count = finger_count
                last_action_time = time.time()

                if finger_count == 1:
                    os.system("notepad")
                elif finger_count == 2:
                    os.system("calc")
                elif finger_count == 3:
                    webbrowser.open("https://www.google.com")
                elif finger_count == 4:
                    os.system("mspaint")
                elif finger_count == 5:
                    os.system("Exit")
                    cap.release()
                    cv2.destroyAllWindows()
                    st.success("Exited Camera")
                    st.stop()


    frame_placeholder.image(frame, channels="BGR")


page_sequence = [
    "Homepage",
    "Registration",
    "Payment",
    "Ticket_Check",
    "My_AI_Bot",
    "Web_Scrapping",
    "Prompt",
    "AI_Agents",
    "AI_Disease_Assistant",
    "Python_Task",
    "Menu_CLI",
    "JavaScript_Task",
    "Machine_Learning_project",
    "Titanic",
    "Salary_Prediction",
    "Computer_Vision",
    "Project_Links",
    "Task_Link",
]
current_title = "Computer_Vision"

if current_title in page_sequence:
    current_index = page_sequence.index(current_title)
    if current_index < len(page_sequence) - 1:
        next_page = page_sequence[current_index + 1]
        st.markdown(
            f"""
            <div style='position: fixed; bottom: 30px; right: 30px; z-index: 9999;'>
                <form action='/{next_page}'>
                    <button style='
                        background-color: #ffcc00;
                        color: #000;
                        border: none;
                        padding: 10px 20px;
                        font-size: 16px;
                        border-radius: 8px;
                        cursor: pointer;
                        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);'>
                        Next →
                    </button>
                </form>
            </div>
            """,
            unsafe_allow_html=True
        )
