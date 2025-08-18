import streamlit as st


st.set_page_config(page_title="Case Study Links", layout="centered")


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
    "Kubernetes": [
        {"title": "IBM use Kubernetes", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_casestudy-kubernetes-ibmcloud-activity-7347498955703775232--TaY?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
    "Amazon Web Services": [
        {"title": "McDonald's use AWS", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_case-study-mcdonalds-digital-transformation-activity-7349123414147612674-s7DG?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
        {"title": "Amazon Cloud Search", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_amazoncloudsearch-awssearch-cloudcomputing-activity-7349293884021051393-OitI?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
        {"title": "AWS 86 Service", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_aws-services-activity-7350633946767835137-Iseg?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
}

st.title("📚 Case Study Links")


for topic, posts in linkedin_links.items():
    st.markdown(f"🔹 {topic}", unsafe_allow_html=True)

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



current_title = "Case_Study"

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

