import streamlit as st
import google.generativeai as genai
 
st.set_page_config(page_title="🧬 Disease Assistant", layout="centered")


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



def build_symptom_prompt(symptoms, strategy):
    if strategy == "Zero-shot":
        return f"What disease could this be based on the symptoms: {symptoms}?"
    elif strategy == "One-shot":
        return f"Symptoms: fever, cough, fatigue -> Disease: Common Cold\nSymptoms: {symptoms} -> Disease:"
    elif strategy == "Few-shot":
        return f"""
Examples:
- fever, rash, joint pain → Dengue
- chest pain, shortness of breath → Heart Attack
- yellow skin, vomiting → Hepatitis

Symptoms: {symptoms} → Disease:"""
    elif strategy == "Chain of Thought":
        return f"A patient presents with: {symptoms}\nLet's think step by step to identify the most likely disease."
    return symptoms


def build_question_prompt(query, strategy):
    if strategy == "Zero-shot":
        return f"Answer this medical question: {query}"
    elif strategy == "One-shot":
        return f"Example: What is malaria? -> A mosquito-borne disease affecting red blood cells.\n\nQuestion: {query} ->"
    elif strategy == "Few-shot":
        return f"""
Q: What is dengue?
A: Dengue is a viral infection transmitted by Aedes mosquitoes.

Q: How does tuberculosis spread?
A: It spreads through airborne droplets when an infected person coughs or sneezes.

Q: {query}
A:"""
    elif strategy == "Chain of Thought":
        return f"Let’s break this down step by step: {query}"
    return query


 
st.title("🧬 Disease Diagnosis Assistant")
st.caption("🧠 Diagnose smarter with Gemini and intelligent prompt strategies")

mode = st.radio("Choose Mode", ["🧬 Symptom-Based Diagnosis", "💬 Ask About Any Disease"])
strategy = st.selectbox("🧠 Choose Prompting Strategy", ["Zero-shot", "One-shot", "Few-shot", "Chain of Thought"])

if mode == "🧬 Symptom-Based Diagnosis":
    symptoms = st.text_input("📝 Enter Symptoms", placeholder="e.g. fever, chills, headache")
    if st.button("💡 Diagnose"):
        if symptoms.strip():
            prompt = build_symptom_prompt(symptoms, strategy)
            try:
                with st.spinner("Gemini is analyzing symptoms..."):
                    response = model.generate_content(prompt)
                    st.success("🧬 Diagnosis Suggestion:")
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"Gemini API Error: {e}")
        else:
            st.warning("Please enter symptoms.")

elif mode == "💬 Ask About Any Disease":
    question = st.text_input("💬 Ask your question", placeholder="e.g. What is tuberculosis?")
    if st.button("📘 Get Answer"):
        if question.strip():
            prompt = build_question_prompt(question, strategy)
            try:
                with st.spinner("Gemini is answering..."):
                    response = model.generate_content(prompt)
                    st.success("📖 Answer:")
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"Gemini API Error: {e}")
        else:
            st.warning("Please enter a question.")


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



current_title = "Prompt"

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
