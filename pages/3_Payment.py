import streamlit as st
from PIL import Image
import os


st.set_page_config(page_title="🔒 Payment Window", page_icon="💳")

st.markdown("""
<style>
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

st.title("🔒 Payment Window")
st.subheader("Scan the QR Code below to complete your payment")


qr_path = os.path.join("pages", "images", "Qr.jpg")


if os.path.exists(qr_path):
    st.image(qr_path, caption="📸 Scan to Pay", use_column_width=True)
else:
    st.error("QR scanner image not found at: " + qr_path)


screenshot = st.file_uploader("📤 Upload your payment screenshot here", type=["jpg", "jpeg", "png"])

if screenshot is not None:
    st.success("Screenshot uploaded successfully ✅")

    if st.button("✅ Submit Payment"):
        st.success("🎉 Payment Verified! Your registration is complete.")

       
        st.write("📌 Booking ID:", st.session_state.get("booking_id", "N/A"))
        st.write("👤 Name:", st.session_state.get("user_name", "N/A"))
        st.write("📧 Email:", st.session_state.get("email", "N/A"))
        st.write("📞 Phone:", st.session_state.get("phone", "N/A"))
        st.write("📅 Date:", st.session_state.get("date", "N/A"))
        st.write("🎟️ Tickets:", st.session_state.get("tickets", "N/A"))

        phone = st.session_state.get("phone", "")
        message = "🎉 Your registration is successful for the Musical Festival!"
        encoded_message = message.replace(" ", "%20")
        if phone:
            whatsapp_url = f"https://wa.me/91{phone}?text={encoded_message}"
            st.markdown(f"[📲 Click here to send WhatsApp Confirmation]({whatsapp_url})", unsafe_allow_html=True)
        else:
            st.warning("Phone number not found in session. Cannot generate WhatsApp link.")


st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Back to Home Page"):
        st.switch_page("pages/1_Homepage.py")

with col2:
    if st.button("🔊 Click here!!"):
        import pyttsx3
        text = "Congratulations! You have completed your registration."
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()


import streamlit_extras.switch_page_button as spb


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
    "Project_Links",
    "Task_Link",
]


current_title = "Payment"


if current_title in page_sequence:
    current_index = page_sequence.index(current_title)
    if current_index < len(page_sequence) - 1:
        next_page = page_sequence[current_index + 1]
        st.markdown(
            f"""
            <div style='position: fixed; bottom: 30px; right: 30px;'>
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
