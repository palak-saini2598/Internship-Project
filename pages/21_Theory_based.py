import streamlit as st


st.set_page_config(page_title="Theory Links", layout="centered")


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
    "Python": [
        {"title": "List vs Tuple", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_programmingtips-tuplevslist-pythonlearning-activity-7351981632142176270-Ewdi?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
    "Linux": [
        {"title": "GUI in Linux", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_exploring-the-power-behind-the-gui-in-linux-activity-7351917410209148929-p0_u?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
        {"title": "Ctrl+C or Ctrl+Z", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_linux-ctrlc-ctrlz-activity-7352200536739168256-qx6M?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4", "color": "#6A1B9A", "text_color": "#FFFFFF"},
        {"title": "Company use linux", "url": "https://www.linkedin.com/posts/palak-saini-7868b921b_linux-opensource-cloudcomputing-activity-7352268492475105280-N28f?utm_source=share&utm_medium=member_desktop&rcm=ACoAADd8DBYBYlk5UNY5NMFs0iIe53dWMgIfAn4",  "color": "#6A1B9A", "text_color": "#FFFFFF"},
    ],
}

st.title("📚 Theory Links")


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
]



current_title = "Theory_based"

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
