from transformers import pipeline
import streamlit as st


# ✅ Load model only once (Streamlit safe)
@st.cache_resource
def load_summarizer():
    return pipeline(
        task="summarization",
        model="sshleifer/distilbart-cnn-6-6",
        device=-1   # force CPU for Streamlit Cloud
    )


def generate_summary(text):

    if len(text.strip()) < 30:
        return "Text too short to summarize."

    summarizer = load_summarizer()

    summary = summarizer(
        text,
        max_length=60,
        min_length=20,
        do_sample=False,
        truncation=True
    )

    return summary[0]["summary_text"]
