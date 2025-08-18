import streamlit as st
import random

st.title("Welcome to India's best Booking Platform")
st.header("🎵 Musical Festival Registration Form")

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


if "registered" not in st.session_state:
    st.session_state.registered = False

if not st.session_state.registered:
    with st.form(key='registration_form'):
        first_name = st.text_input("First Name:")
        last_name = st.text_input("Last Name:")
        email = st.text_input("Email:")
        phone = st.text_input("Phone Number:")
        show_date = st.selectbox("Select an available date:", [
            '21 June 2025', '22 June 2025', '23 June 2025', '24 June 2025'
        ])
        tickets = st.number_input("Number of Tickets:", min_value=1, max_value=10, step=1)
        submit = st.form_submit_button("Proceed to Payment")

    if submit:
        if not first_name or not last_name or not email or not phone:
            st.error("❌ Please fill in all the details before proceeding.")
        else:
            
            st.session_state.booking_id = random.randint(1000, 9999)
            st.session_state.user_name = f"{first_name} {last_name}"
            st.session_state.email = email
            st.session_state.phone = phone
            st.session_state.date = show_date
            st.session_state.tickets = tickets
            st.session_state.registered = True
            st.rerun()  
else:

    st.success("Registration Successful! 🎉")
    st.write("📌 Booking ID:", st.session_state.booking_id)
    st.write("👤 Name:", st.session_state.user_name)
    st.write("📧 Email:", st.session_state.email)
    st.write("📞 Phone:", st.session_state.phone)
    st.write("📅 Date:", st.session_state.date)
    st.write("🎟️ Tickets:", st.session_state.tickets)

    if st.button("Go to Payment Page"):
        st.switch_page("pages/3_Payment.py")

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



current_title = "Registration"


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
