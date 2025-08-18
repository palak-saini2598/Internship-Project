import streamlit as st

st.set_page_config(page_title="🧲 LinkedIn Project Links", layout="centered")

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

linkedin_links = {
    "Docker Projects": [
        {"title": "DIND Setup", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_dockerindocker-dind-rhel9-activity-7351484551539441664-ie6R?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
        {"title": "Apache Webserver Setup", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_apacheserver-dockerdeployment-webhosting-activity-7348256254839926785-Oz0c?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
    "Jenkins Projects": [
        {"title": "CI/CD Pipeline", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_cicdpipeline-devops-docker-activity-7349672612215554048-h-jR?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
    "Kubernetes Projects": [
        {"title": "Kubernetes Media Pipeline", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_kubernetes-mediapipeline-kubernetesproject-activity-7355575706652700674-eC--?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
    "Agentic AI": [
        {"title": "Langchain Tool", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_twilio-langchain-voiceautomation-activity-7347595930780495872--pjA?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
    "MicroService Architecture": [
        {"title": "Cache", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_microservices-dockercompose-restapi-activity-7353836738395435009-Snu6?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
    "Bot": [
        {"title": "Telegram Bot", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_late-post-but-worth-it-looking-back-at-activity-7359274649517449217-fSCy?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
        {"title": "Portfolio Bot", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_aichatbot-portfolioproject-personalai-activity-7355301748778983426-OvgF?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
        {"title": "My Buddy", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_mybuddy-aichatbot-portfolioassistant-activity-7355896121065455618-BsAo?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
    "Firebase": [
        {"title": "Firebase Authentication", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_firebase-authentication-appdevelopment-activity-7359237766687137792-hZtC?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
    "Backup Project": [
        {"title": "Backup Project", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_python-flask-automation-activity-7359153846796828672-Ya0S?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
    "Website": [
        {"title": "Portfolio", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_portfolio-webdevelopment-frontenddeveloper-activity-7355469621740634112-hSq0?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
        {"title": "Apno ki Awaj", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_lakshyachalana-palaksaini-productportfolio-activity-7358549209517645826-UWEj?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
    "All in one": [
        {"title": "Summer Project", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_summerproject2025-webappproject-fullstackdeveloper-activity-7349078688757420034-q_NB?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
}

st.markdown("### 🧲 Project Links", unsafe_allow_html=True)

for topic, posts in linkedin_links.items():
    st.markdown(f"#### 🔹 {topic}", unsafe_allow_html=True)

    for i in range(0, len(posts), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(posts):
                post = posts[i + j]
                with cols[j]:
                    st.markdown(
                        f"<a href='{post['url']}' target='_blank'>"
                        f"<button style='width:100%; background-color:{post['color']}; color:{post['text_color']}; "
                        "font-size:16px; padding:10px 24px; border:none; border-radius:8px; cursor:pointer;'>"
                        f"{post['title']}</button></a>",
                        unsafe_allow_html=True
                    )

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
    "Case_Study",
    "Theory_based",
]

current_title = "Project_Links"

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
