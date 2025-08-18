import streamlit as st


st.set_page_config(
    page_title="🌟 My Summer Project",
    page_icon="📚",
    layout="wide"
)


st.markdown("""
<style>
/* 🎨 Dashboard Background */
.stApp {
    background-image: linear-gradient(to right top, #051937, #004d7a, #008793, #00bf72, #a8eb12);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* 🌟 Title Animation */
.title {
    font-size: 3rem;
    font-weight: bold;
    text-align: center;
    margin-top: 30px;
    animation: fadeInDown 1.2s ease-out;
    color: #fff;
    text-shadow: 1px 1px 4px #000;
}

.subtitle {
    font-size: 1.3rem;
    text-align: center;
    margin-bottom: 40px;
    animation: fadeIn 2s ease-in;
    color: #fdfdfd;
}

/* 🔘 Buttons */
.st-emotion-cache-1avcm0n a {
    background: linear-gradient(to right, #6a11cb, #2575fc);
    color: white;
    padding: 0.8rem 1.2rem;
    border-radius: 10px;
    font-weight: bold;
    transition: transform 0.2s, box-shadow 0.2s;
    text-decoration: none;
    border: none;
}
.st-emotion-cache-1avcm0n a:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px rgba(255,255,255,0.3);
    background: linear-gradient(to right, #f7971e, #ffd200);
    color: black;
}

/* ✨ Sidebar Style */
section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom right, #23074d, #cc5333);
    color: white;
    animation: fadeSlideIn 1.2s ease-in-out;
}

/* Sidebar Heading Text */
section[data-testid="stSidebar"] .css-1d391kg {
    color: #ffdd57 !important;
    font-size: 20px;
    font-weight: bold;
    padding-bottom: 10px;
}

/* Animations */
@keyframes fadeInDown {
    0% { opacity: 0; transform: translateY(-20px); }
    100% { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
@keyframes fadeSlideIn {
    from { opacity: 0; transform: translateX(-30px); }
    to { opacity: 1; transform: translateX(0); }
}

/* Headings */
h3 {
    color: #ffe500;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<div class='title'>🌟 MY SUMMER PROJECT</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>🚀 Explore tools & automations built during my LinuxWorld Summer Internship 2025</div>", unsafe_allow_html=True)

st.divider()


def link_section(header, links):
    st.subheader(header)
    col1, col2 = st.columns(2)
    for i, (label, path) in enumerate(links):
        with (col1 if i % 2 == 0 else col2):
            st.page_link(f"pages/{path}", label=label)


link_section("📌 Event Management", [
    ("🏠 Home Page", "1_Homepage.py"),
    ("📝 Registration", "2_Registration.py"),
    ("💳 Payment", "3_Payment.py"),
    ("🔍 Ticket Checker", "4_Ticket_Check.py"),
])

link_section("🧠 AI Projects", [
    ("🤖 Personal BOT", "5_My_AI_Bot.py"),
    ("📰 AI News Generator", "6_Web_Scrapping.py"),
    ("🗣️ Prompt Engineering", "7_Prompt.py"),
    ("🌐 AI Agents", "8_AI_Agents.py"),
    ("🧬 AI Disease Assistant", "9_AI_Disease_Assistant.py"),
])

link_section("⚙️ Python & Shell Utilities", [
    ("🐍 Python Automation", "10_Python_Task.py"),
    ("🐧 Linux-Docker Menu", "11_Menu_CLI.py"),
])

link_section("🖱️ JavaScript Tools", [
    ("💡 JavaScript Utility", "12_JavaScript_Task.py"),
])

link_section("🖱️ Fullstack Tools", [
    ("💡 Fullstack Utility", "13_Fullstack_Task.py"),
])

link_section("📈 Machine Learning", [
    ("📊 ML Task", "14_Machine_Learning_project.py"),
    ("🚢 Titanic Survival", "15_Titanic.py"),
    ("💼 Salary Prediction", "16_Salary_Prediction.py"),
    ("🖼️ Computer Vision", "17_Computer_Vision.py"),
])

link_section("📎 Project Links", [
    ("🔗 Project Links", "18_Project_Links.py"),
    ("🧾 Task Links", "19_Task_Link.py"),
])

link_section("📎 Case Study Links", [
    ("🔗 Case Study Links", "20_Case_Study.py"),
])

link_section("📎 Theory Links", [
    ("🔗 Theory Links", "21_Theory_based.py"),
])


st.divider()
st.caption("✨ Designed by Palak Saini | Summer Project 2025 | LinuxWorld Informatics Pvt Ltd")
