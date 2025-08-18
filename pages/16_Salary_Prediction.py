import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


st.set_page_config(page_title="💼 Salary Predictor", layout="centered")


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


st.title("💼 Salary Prediction using Linear Regression")
st.markdown("Predict salary based on experience using data from `data/SalaryData.csv`.")


csv_path = "Data/SalaryData.csv"

try:
    dataset = pd.read_csv(csv_path)

    st.subheader("📄 Dataset Preview")
    st.write(dataset.head())

    if "YearsExperience" not in dataset.columns or "Salary" not in dataset.columns:
        st.error("CSV must contain 'YearsExperience' and 'Salary' columns.")
    else:
        
        x = dataset[['YearsExperience']].values
        y = dataset['Salary'].values
        model = LinearRegression()
        model.fit(x, y)

        
        st.subheader("🔢 Enter Experience")
        exp = st.slider("Years of Experience:", 0.0, 20.0, 2.5, 0.1)
        input_exp = np.array([[exp]])
        prediction = model.predict(input_exp)[0]

        st.success(f"💰 Predicted Salary: ₹ {prediction:,.2f}")

        
        st.subheader("📊 Experience vs Salary Plot")
        fig, ax = plt.subplots()
        ax.scatter(x, y, color='blue', label='Data')
        ax.plot(x, model.predict(x), color='red', label='Regression Line')
        ax.scatter(exp, prediction, color='green', s=100, label='Your Prediction')
        ax.set_xlabel("Years of Experience")
        ax.set_ylabel("Salary")
        ax.set_title("Salary Prediction")
        ax.legend()
        st.pyplot(fig)

except FileNotFoundError:
    st.error("❌ Could not find 'Data/SalaryData.csv'. Please make sure it exists.")



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

current_title = "Salary_Prediction"

if current_title in page_sequence:
    current_index = page_sequence.index(current_title)
    if current_index < len(page_sequence) - 1:
        next_page = page_sequence[current_index + 1]
        st.markdown(
            f"""
            <div style='position: fixed; bottom: 30px; right: 30px; z-index: 9999;'>
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
