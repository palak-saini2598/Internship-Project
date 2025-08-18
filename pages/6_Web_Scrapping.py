import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import google.generativeai as genai


st.set_page_config(page_title="News by Date & Category", page_icon="🗞️")

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
model = genai.GenerativeModel("gemini-1.5-flash")

CATEGORY_URLS = {
    "National": "https://www.thehindu.com/news/national/",
    "International": "https://www.thehindu.com/news/international/",
    "Politics": "https://www.thehindu.com/news/national/politics/",
    "Business": "https://www.thehindu.com/business/",
    "Sports": "https://www.thehindu.com/sport/",
    "Technology": "https://www.thehindu.com/sci-tech/technology/"
}

@st.cache_data(show_spinner=True)
def scrape_category_news(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        articles = []
        for link in soup.find_all("a", href=True):
            title = link.get_text(strip=True)
            href = link['href']
            full_url = href if href.startswith("http") else f"https://www.thehindu.com{href}"

            if title and "/news/" in href:
                articles.append({"title": title, "url": full_url})

        return articles
    except Exception as e:
        return []

def generate_summary(category, news_list, user_prompt, date_text):
    if not news_list:
        return "No news articles found."

    combined_titles = "\n".join([f"- {item['title']}" for item in news_list])
    prompt = f"""
    You are a journalist summarizing the latest {category} news.

    🗓️ Date: {date_text}
    🗂️ Category: {category}
    📰 Headlines:
    {combined_titles}

    User question: {user_prompt}

    Please summarize the top news items and answer the query in a formal tone.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini API Error: {e}"


st.title("🗞️ AI News Generator")
st.markdown("Get news from *The Hindu* based on category and date.")

category = st.selectbox("Select News Category:", list(CATEGORY_URLS.keys()))
selected_date = st.date_input("Pick a date (for reference only):", value=datetime.today())
user_prompt = st.text_input("Ask something about the selected category/date:", placeholder="e.g., What happened in sports today?")

if st.button("Generate News"):
    with st.spinner(f"Scraping {category} news..."):
        news_items = scrape_category_news(CATEGORY_URLS[category])

    if news_items:
        st.success(f"Fetched {len(news_items)} news articles.")
        with st.expander("📰 Click to preview headlines"):
            for item in news_items:
                st.markdown(f"- [{item['title']}]({item['url']})")

        if user_prompt:
            with st.spinner("Asking Gemini..."):
                summary = generate_summary(category, news_items, user_prompt, selected_date.strftime('%B %d, %Y'))
                st.markdown("### 📌 Gemini's Summary")
                st.write(summary)
        else:
            st.warning("Please enter a question to ask Gemini.")
    else:
        st.error("No news articles found in this category. Try another.")



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



current_title = "Web_Scrapping"


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
