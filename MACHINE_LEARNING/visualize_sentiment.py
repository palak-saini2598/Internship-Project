import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Sentiment": ["Positive", "Negative", "Neutral"],
    "Count": [45, 30, 25]
}
df = pd.DataFrame(data)

def show_chart():
    st.write("### 📊 Sentiment Distribution Chart")
    fig, ax = plt.subplots()
    ax.bar(df["Sentiment"], df["Count"])
    ax.set_xlabel("Sentiment Type")
    ax.set_ylabel("Number of Reviews")
    ax.set_title("Sentiment Analysis Visualization")
    st.pyplot(fig)
