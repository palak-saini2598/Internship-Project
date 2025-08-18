import streamlit as st


st.set_page_config(page_title="Task Links", layout="centered")


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



st.markdown("<h3 style='margin-bottom: 20px;'>Task Links</h3>", unsafe_allow_html=True)


linkedin_links = {
    "Python": [
        {
            "title": "Google Search",
            "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_pythonproject-automationwithpython-googlesearch-activity-7350764809061122048-qaXE?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4",
            "color": "#6A1B9A",
            "text_color": "#FFFFFF"
        },
        {
            "title": "Monitoring System RAM",
            "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_pythonproject-systemmonitoring-pythonscript-activity-7350849143411507201-m1bj?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4",
            "color": "#6A1B9A",
            "text_color": "#FFFFFF"
        },
        {
            "title": "Digital Art",
            "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_pythonprogramming-pillowlibrary-digitalart-activity-7351296305190596610-2xac?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4",
            "color": "#6A1B9A",
            "text_color": "#FFFFFF"
        },
        {
            "title": "Whatsapp Automation",
            "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_python-automation-whatsappbot-activity-7343508397134073856-hYj_?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4",
            "color": "#6A1B9A",
            "text_color": "#FFFFFF"
        },
    ],
    "Machine Learning": [
        {
            "title": "Visualizing Error in Linear Regression",
            "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_machinelearning-linearregression-modelevaluation-activity-7355838239179444224-dDir?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4",
            "color": "#6A1B9A",
            "text_color": "#FFFFFF"
        },
        {
            "title": "Natural Language Processing",
            "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_nlp-spacy-textanalysis-activity-7354768688283009025-I1Ym?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4",
            "color": "#6A1B9A",
            "text_color": "#FFFFFF"
        },
        {
            "title": "NLTK",
            "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_nltk-machinelearning-nlp-activity-7354563615552634880-JMK3?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4",
            "color": "#6A1B9A",
            "text_color": "#FFFFFF"
        },
    ]
}


for topic, projects in linkedin_links.items():
    st.markdown(f"<h4 style='margin-top: 10px;'>{topic}</h4>", unsafe_allow_html=True)

    for i in range(0, len(projects), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(projects):
                project = projects[i + j]
                with cols[j]:
                    st.markdown(
                        f"""
                        <a href="{project['url']}" target="_blank">
                            <button style="
                                width: 100%;
                                background-color: {project['color']};
                                color: {project['text_color']};
                                font-size: 16px;
                                font-weight: bold;
                                padding: 12px 20px;
                                margin: 10px 0;
                                border: none;
                                border-radius: 10px;
                                cursor: pointer;
                                transition: transform 0.2s, background-color 0.2s;
                            " 
                            onmouseover="this.style.transform='scale(1.05)'"
                            onmouseout="this.style.transform='scale(1)'">
                                {project['title']}
                            </button>
                        </a>
                        """,
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
]



current_title = "Task_Link"

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

