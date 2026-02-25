from transformers import pipeline

# Load summarization model
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-6-6"
)

def generate_summary(text):

    if len(text.strip()) < 30:
        return "Text too short to summarize."

    summary = summarizer(
        text,
        max_length=60,
        min_length=20,
        do_sample=False,
        truncation=True
    )

    return summary[0]['summary_text']