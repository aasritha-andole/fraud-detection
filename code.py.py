import streamlit as st
st.set_page_config(page_title="AI Fraud Detection", page_icon="🔍", layout="wide")
import joblib
import numpy as np
import pandas as pd
import torch
from transformers import pipeline
from urllib.parse import urlparse

# Load pre-trained NLP models
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Load the trained phishing classifier
try:
    vectorizer, classifier = joblib.load("phishing_classifier.pkl")
except Exception as e:
    st.error("Error loading phishing classifier: " + str(e))
    vectorizer, classifier = None, None

# Custom CSS for better UI
st.markdown("""
    <style>
        .main {background-color: #eef2f3; padding: 20px;}
        .title {text-align: center; color: #2c3e50;}
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🔍 AI Fraud Detector")
st.sidebar.markdown("Detect scams, phishing emails, and malicious URLs in real-time.")

# Main UI
st.markdown("<h1 class='title'>🔎 AI Fraud Detection System</h1>", unsafe_allow_html=True)
st.markdown("### 💡 **Check text, URLs, and detect fraud efficiently!**")

# User Inputs
text_input = st.text_area("📜 Enter text for fraud detection:", height=150)
url_input = st.text_input("🔗 Enter URL for verification:")

if st.button("🚀 Verify for Fraud"):
    with st.spinner("🔍 Analyzing... Please wait."):
        results = []
        fraud_text = "✅ Not Fraud"
        
        # Text Analysis
        if text_input and vectorizer and classifier:
            text_vectorized = vectorizer.transform([text_input])
            prediction = classifier.predict(text_vectorized)
            if prediction[0] == 1:
                fraud_text = "🚨 Fraud Detected"
            results.append(f"📜 **Phishing Detection:** {fraud_text}")
            sentiment = sentiment_analyzer(text_input)
            results.append(f"📊 **Sentiment Analysis:** {sentiment[0]['label']} (Score: {sentiment[0]['score']:.2f})")

        # Display Results
        st.success("✅ Analysis Complete!")
        for result in results:
            st.markdown(f"- {result}")

st.markdown("---")
st.markdown("📌 **Note:** This is an AI-based fraud detection system. Always verify results manually.")
