import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
import io


st.set_page_config(page_title="🚢 Titanic Survival Predictor", layout="centered")


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


st.title("🚢 Titanic Survival Prediction App")
st.markdown("Predict survival using logistic regression on the Titanic dataset.")


csv_path = "data/Titanic.csv"

try:
    dataset = pd.read_csv(csv_path)

    st.subheader("📊 Dataset Preview")
    st.write(dataset.head())

    st.subheader("📄 Dataset Info")
    buffer = io.StringIO()
    dataset.info(buf=buffer)
    st.text(buffer.getvalue())

    
    st.subheader("📈 Data Visualizations")
    for col in ['Sex', 'Pclass', 'SibSp', 'Parch']:
        fig, ax = plt.subplots()
        sns.countplot(data=dataset, x=col, hue='Survived', ax=ax)
        st.pyplot(fig)


    y = dataset['Survived']
    X = dataset[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']]

    
    st.subheader("🧼 Missing Data Heatmap (Before Cleaning)")
    fig, ax = plt.subplots()
    sns.heatmap(X.isnull(), ax=ax)
    st.pyplot(fig)

    
    def ageupdate(row):
        Pclass, age = row
        return 38 if pd.isnull(age) and Pclass == 1 else (29 if Pclass == 2 else 25) if pd.isnull(age) else age

    X['Age'] = X[['Pclass', 'Age']].apply(ageupdate, axis=1)

    
    st.subheader("✅ Missing Data Heatmap (After Cleaning)")
    fig, ax = plt.subplots()
    sns.heatmap(X.isnull(), ax=ax)
    st.pyplot(fig)

    
    X = pd.get_dummies(X, columns=['Sex', 'Pclass', 'SibSp', 'Parch'], drop_first=False)
    X.columns = X.columns.astype(str)
    feature_columns = X.columns.tolist()

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

  
    y_pred = model.predict(X_test)
    st.subheader("📌 Model Evaluation")
    st.write(f"Accuracy: **{round(accuracy_score(y_test, y_pred)*100, 2)}%**")
    st.write("Confusion Matrix:")
    st.write(confusion_matrix(y_test, y_pred))

    
    st.subheader("🔮 Try Your Own Prediction")
    age_input = st.slider("Age", 1, 80, 25)
    sex_input = st.selectbox("Sex", sorted(dataset["Sex"].unique()))
    pclass_input = st.selectbox("Pclass", sorted(dataset["Pclass"].unique()))
    sibsp_input = st.selectbox("SibSp (Siblings/Spouses)", sorted(dataset["SibSp"].unique()))
    parch_input = st.selectbox("Parch (Parents/Children)", sorted(dataset["Parch"].unique()))

    input_dict = dict.fromkeys(feature_columns, 0)
    input_dict["Age"] = age_input
    input_dict[f"Sex_{sex_input}"] = 1
    input_dict[f"Pclass_{pclass_input}"] = 1
    input_dict[f"SibSp_{sibsp_input}"] = 1
    input_dict[f"Parch_{parch_input}"] = 1

    input_df = pd.DataFrame([input_dict])

    if st.button("Predict"):
        prediction = model.predict(input_df)[0]
        st.success("🎉 Survived!" if prediction == 1 else "❌ Did not survive.")

except FileNotFoundError:
    st.error("❌ Titanic dataset not found. Please ensure it's in `data/Titanic.csv`.")


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
current_title = "Titanic"

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
