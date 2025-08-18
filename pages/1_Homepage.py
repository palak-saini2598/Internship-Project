import streamlit as st
import base64
import os


st.set_page_config(page_title="🎤 Event Pass", page_icon="🎫", layout="wide")


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


image_path = "pages/images/event_img.jpg"

def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

if os.path.exists(image_path):
    img_base64 = get_base64_image(image_path)
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        padding-top: 0px !important;
    }}

    [data-testid="stHeader"] {{
        background: transparent;
        height: 0rem;
        visibility: hidden;
    }}

    .block-container {{
        background-color: rgba(255, 255, 255, 0.3);
        padding: 2rem;
        border-radius: 12px;
        backdrop-filter: blur(5px);
    }}

    h1, h2, h3, h4, h5, h6, p, span {{
        color: #000000 !important;
    }}

    .stButton button {{
        background-color: white !important;
        color: black !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: 1px solid #ccc;
        transition: 0.3s;
    }}

    .stButton button:hover {{
        background-color: #f0f0f0 !important;
        border: 1px solid #888;
        cursor: pointer;
    }}
    </style>
    """, unsafe_allow_html=True)
else:
    st.error("Image not found. Please check the path.")

st.markdown("<div class='block-container'>", unsafe_allow_html=True)

st.title("🎤 Event Pass")
st.write("A Concert Booking Platform.")
st.write("📍 JECC, Jaipur")
st.write("🕗 8:30 PM")

st.write("## What would you like to do?")
col1, col2 = st.columns(2)

with col1:
    if st.button("🎟️ Book Ticket"):
        st.switch_page("pages/2_Registration.py")

with col2:
    if st.button("🔍 Check Your Ticket"):
        st.switch_page("pages/4_Ticket_Check.py")

st.markdown("</div>", unsafe_allow_html=True)

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


current_title = "Homepage"


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
