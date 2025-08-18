import streamlit as st


st.set_page_config(page_title="ML Tasks Dashboard", page_icon="📊", layout="centered")


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


st.title("📊 Machine Learning NLP Tasks")


task = st.selectbox(
    "Choose a task to perform:",
    ["-- Select --", "NLTK Lemmatizer", "Spacy NLP", "Sentiment Analysis", "Visualize Sentiment"]
)


if task == "NLTK Lemmatizer":
    from MACHINE_LEARNING import nltk_task

    st.subheader("📝 NLTK Lemmatizer")
    text = st.text_area("Enter your text:", "Cats are running faster than dogs")
    
    if st.button("Lemmatize"):
        result = nltk_task.lemmatize_text(text)
        st.write("Lemmatized Words:", result)

elif task == "Spacy NLP":
    from MACHINE_LEARNING import spacy_task
    import pandas as pd

    st.subheader("🧠 spaCy NLP Task")
    text = st.text_area("Enter your text:", "Spacy is a great NLP tool.")

    if st.button("Analyze"):
        doc_result = spacy_task.process_text(text)
        if doc_result:
            st.success("Text Processed Successfully")
            df = pd.DataFrame(doc_result)
            st.dataframe(df)
        else:
            st.error("Could not process the text.")

elif task == "Sentiment Analysis":
    from MACHINE_LEARNING import sentiment_analysis

    st.subheader("🧪 TextBlob Sentiment Analysis")
    text = st.text_area("Enter a sentence:")

    if st.button("Analyze"):
        polarity, subjectivity = sentiment_analysis.analyze_sentiment(text)
        st.write(f"**Polarity:** {polarity}")
        st.write(f"**Subjectivity:** {subjectivity}")
        
        if polarity > 0:
            st.success("Overall Sentiment: Positive")
        elif polarity < 0:
            st.error("Overall Sentiment: Negative")
        else:
            st.info("Overall Sentiment: Neutral")

elif task == "Visualize Sentiment":
    from MACHINE_LEARNING import visualize_sentiment

    st.subheader("📈 Sentiment Distribution")
    visualize_sentiment.show_chart()

else:
    st.info("Please select a task from the dropdown above.")


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



current_title = "Machine_Learning_project"


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
