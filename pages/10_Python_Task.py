import streamlit as st
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from instagrapi import Client as InstaClient


st.set_page_config(page_title="Communication Dashboard", layout="centered")


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



st.title("📡 Communication Dashboard – By PLK")
st.markdown("---")

st.subheader("📩 Send SMS")

with st.form("sms_form"):
    twilio_sid = st.text_input("Twilio SID", type="password")
    twilio_token = st.text_input("Twilio Auth Token", type="password")
    twilio_number = st.text_input("Twilio Phone Number (with +country code)")
    recipient_number = st.text_input("Recipient Phone Number (with +country code)")
    sms_body = st.text_input("Message Text", value="Hello from Python, I am PLK!")
    sms_submit = st.form_submit_button("Send SMS")

    if sms_submit:
        try:
            client = Client(twilio_sid, twilio_token)
            message = client.messages.create(
                body=sms_body,
                from_=twilio_number,
                to=recipient_number
            )
            st.success(f"✅ SMS sent! SID: {message.sid}")
        except Exception as e:
            st.error(f"❌ SMS Error: {e}")


st.subheader("📞 Make a Call")

with st.form("call_form"):
    call_sid = st.text_input("Twilio SID (Call)", type="password")
    call_token = st.text_input("Twilio Auth Token (Call)", type="password")
    call_from = st.text_input("Twilio Phone Number (Call)")
    call_to = st.text_input("Recipient Phone Number (Call)")
    call_msg = st.text_area("Call Message", value="Hello! This is a Python-Twilio call. Have a great day!")
    call_submit = st.form_submit_button("Make Call")

    if call_submit:
        try:
            call_client = Client(call_sid, call_token)
            twiml = f'<Response><Say>{call_msg}</Say></Response>'
            call = call_client.calls.create(
                to=call_to,
                from_=call_from,
                twiml=twiml
            )
            st.success(f"✅ Call initiated! SID: {call.sid}")
        except Exception as e:
            st.error(f"❌ Call Error: {e}")


st.subheader("📧 Send Email")

with st.form("email_form"):
    sender_email = st.text_input("Your Gmail Address")
    app_password = st.text_input("App Password", type="password")
    receiver_email = st.text_input("Receiver Email")
    subject = st.text_input("Subject", value="Test Email from Python")
    plain_text = st.text_input("Plain Text Message", value="Hi, how are you?")
    html_content = st.text_area("HTML Message", value="<h2>Hello!</h2><p>This is a test email from Streamlit + Python.</p>")
    email_submit = st.form_submit_button("Send Email")

    if email_submit:
        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = sender_email
            msg["To"] = receiver_email

            msg.attach(MIMEText(plain_text, "plain"))
            msg.attach(MIMEText(html_content, "html"))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, app_password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
            st.success("✅ Email sent successfully!")
        except Exception as e:
            st.error(f"❌ Email Error: {e}")


st.subheader("📸 Instagram Auto Post")

with st.form("insta_form"):
    insta_user = st.text_input("Instagram Username")
    insta_pass = st.text_input("Instagram Password", type="password")
    caption = st.text_input("Caption", value="Automated post from Streamlit + Python ❤️")
    uploaded_img = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    insta_submit = st.form_submit_button("Post to Instagram")

    if insta_submit:
        if uploaded_img is None:
            st.warning("⚠️ Please upload an image to post.")
        else:
            try:
                with open("temp_insta_img.jpg", "wb") as f:
                    f.write(uploaded_img.read())

                cl = InstaClient()
                cl.login(insta_user, insta_pass)
                cl.photo_upload("temp_insta_img.jpg", caption)
                st.success("✅ Instagram post uploaded!")
            except Exception as e:
                st.error(f"❌ Instagram Error: {e}")


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



current_title = "Python_Task"


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
