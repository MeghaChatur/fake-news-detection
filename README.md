**📰 Fake News Detection using Machine Learning & NLP**

**📌 Project Overview**

Misinformation spreads rapidly through online platforms and social media, making it difficult for students to distinguish between reliable and fake news. This project provides an AI-powered solution that analyzes news articles, predicts their credibility, and generates concise summaries to help users understand information quickly and accurately.
The system uses Natural Language Processing (NLP) and Machine Learning models to classify news as REAL or FAKE, along with a confidence score and automated article summarization.

**⚙️ Installation & Setup**

**1️⃣ Clone Repository**

git clone https://github.com/MeghaChatur/fake-news-detection.git
cd fake-news-detection

**2️⃣ Create Virtual Environment**

Windows:

python -m venv venv
venv\Scripts\activate

**3️⃣ Install Dependencies**
**Option A: ML Models Only (Logistic Regression & SVM)**
    pip install -r requirements-ml.txt

**Option B: ML + BERT Models**
    pip install -r requirements-bert.txt

**🏋️ Model Training**

**Prepare dataset:**

python -m src.prepare_data --input data/raw.csv --output data/cleaned.csv

Train Logistic Regression:

python -m src.train_tfidf --data data/cleaned.csv --model lr

Train SVM:

python -m src.train_tfidf --data data/cleaned.csv --model svm

Train BERT (optional):

python -m src.train_bert --data data/cleaned.csv --out models/bert_distilbert

▶️ Run Application
streamlit run app/streamlit_app.py

Open browser:
http://localhost:8501
