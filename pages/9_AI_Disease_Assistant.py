import streamlit as st
import google.generativeai as genai


st.set_page_config(page_title="🧠 Disease Detector", page_icon="🩺", layout="centered")


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


genai.configure(api_key="AIzaSyA00cuzjd1OwhyWaL7B-SQmWOMmz8G56Ew")


st.title("🩺 Disease Detector")
st.markdown("Ask me anything about a disease and I’ll reply in detail using Google's Gemini AI.")


user_input = st.text_input("Enter your disease-related question", placeholder="e.g. What is dengue?")


def get_disease_info(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat()
        chat.send_message(f"You are a medical assistant. Give detailed, clear, human-friendly answers.\n\n{prompt}")
        return chat.last.text
    except Exception as e:
        return f"❌ Error: {e}"


if st.button("Get Info"):
    if user_input.strip():
        with st.spinner("Analyzing with Gemini..."):
            response = get_disease_info(user_input)
            st.success("✅ Response from Gemini:")
            st.write(response)
    else:
        st.warning("⚠️ Please enter a valid question.")


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



current_title = "AI_Disease_Assistant"


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
