import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline
from wordcloud import WordCloud

# Page title
st.title("🏛️📊 LegisAI - Legislative Comment Analyzer")
st.write("Analyze stakeholder sentiment and opinions on legislative discussions.")

# Load AI models
sentiment_pipeline = pipeline("sentiment-analysis", framework="pt")

# Get HF token from Streamlit secrets
HF_API_TOKEN = st.secrets["HF_API_TOKEN"]

# Load summarizer using HF API token
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    use_auth_token=HF_API_TOKEN,
    framework="pt"
)

# Summary function
def generate_summary(text):
    if len(text.split()) < 12:
        return text
    try:
        summary = summarizer(text, max_length=30, min_length=10, do_sample=False)
        return summary[0]['summary_text']
    except:
        return text

# Mode selection
option = st.radio(
    "Choose Analysis Mode",
    ("Analyze Single Comment", "Upload CSV for Bulk Analysis")
)

# ----------------------------
# SINGLE COMMENT ANALYSIS
# ----------------------------

if option == "Analyze Single Comment":

    user_comment = st.text_area("Enter your comment")

    if st.button("Analyze Comment"):

        if user_comment:

            sentiment = sentiment_pipeline(user_comment)[0]["label"]
            summary = generate_summary(user_comment)

            st.subheader("Results")

            st.write("**Comment:**", user_comment)
            st.write("**Sentiment:**", sentiment)
            st.write("**Summary:**", summary)

        else:
            st.warning("Please enter a comment.")

# ----------------------------
# BULK CSV ANALYSIS
# ----------------------------

elif option == "Upload CSV for Bulk Analysis":

    uploaded_file = st.file_uploader("Upload CSV file containing comments", type=["csv"])

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

        st.write("Preview of dataset")
        st.dataframe(df.head())

        if st.button("Run Analysis"):

            # Sentiment analysis
            df["sentiment"] = df["comment"].apply(lambda x: sentiment_pipeline(x)[0]["label"])

            # Summary generation
            df["summary"] = df["comment"].apply(generate_summary)

            st.subheader("Analyzed Data")
            st.dataframe(df.head())

            # Sentiment chart
            st.subheader("Sentiment Distribution")

            df["sentiment"].value_counts().plot(kind="bar")
            plt.xlabel("Sentiment")
            plt.ylabel("Number of Comments")

            st.pyplot(plt)

            # Word cloud
            st.subheader("Word Cloud")

            text = " ".join(df["comment"])

            wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

            plt.figure(figsize=(10,5))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")

            st.pyplot(plt)