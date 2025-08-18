import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import google.generativeai as genai
import time

st.set_page_config(page_title="MyBuddy – Palak’s Assistant", layout="centered")


st.markdown("""
<style>
    /* Sidebar styling (unchanged) */
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
model = genai.GenerativeModel("gemini-2.5-flash")

@st.cache_data(show_spinner=False)
def get_rendered_portfolio_text(url):
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(url)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        text = soup.get_text(separator="\n", strip=True)
        driver.quit()
        return text
    except Exception as e:
        return f" Error fetching portfolio content: {e}"

portfolio_url = "https://palaksaini-portfolio.netlify.app/"
portfolio_text = get_rendered_portfolio_text(portfolio_url)

def answer_about_portfolio(user_query):
    prompt = f"""
You are MyBuddy, a helpful AI assistant designed to answer questions about Palak Saini based on her portfolio website.

Here is the content from her website:
---
{portfolio_text}
---

Now, answer this question as clearly and informatively as possible:
"{user_query}"
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f" Gemini Error: {e}"

st.title("🤖 MyBuddy: Palak Saini’s Portfolio Assistant")
st.markdown("""
Ask anything about **Palak Saini** — her skills, experience, education, or projects — powered by her live website content.  
🌐 Website: [palaksaini-portfolio.netlify.app](https://palaksaini-portfolio.netlify.app/)
""")

user_input = st.text_input("💬 Ask your question:", placeholder="e.g., What technologies does Palak know?")

if user_input:
    with st.spinner("Analyzing Palak's portfolio..."):
        result = answer_about_portfolio(user_input)
    st.success("✅ Gemini's Answer:")
    st.write(result)


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

current_title = "My_AI_Bot"

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
