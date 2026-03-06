🏛️📊LegisAl - Legislative Comment Analyzer

An Al-powered system for analyzing public feedback on draft legislations and policy documents.

LegisAl helps government organizations, policy makers, and analysts understand stakeholder opinions at scale using Natural Language Processing (NLP) and Generative Al techniques.

The system automatically performs:

Sentiment Analysis

Al-powered Comment Summarization

Keyword Extraction using Word Cloud

This helps decision-makers analyze thousands of stakeholder comments efficiently without missing important insights.

---

🚀Problem Statement

Government portals such as MCA eConsultation allow stakeholders to submit feedback on draft legislations and policy amendments.

When large volumes of comments are received, it becomes difficult for analysts to:

Read every comment manually

Identify the overall sentiment

Extract key discussion topics

Summarize stakeholder feedback

LegisAl solves this problem by using Al to automatically analyze public comments and generate meaningful insights.

---

🧠Key Features

1. Sentiment Analysis

Detects the sentiment of each stakeholder comment as:

-> Positive

-> Negative

-> Neutral

This helps policymakers quickly understand public opinion trends.

2. Al Comment Summarization

Uses a Generative Al model to generate concise summaries of long stakeholder comments.

This reduces the effort required to read lengthy suggestions.

3. Word Cloud Visualization

Generates a word cloud from all comments to highlight the most frequently used keywords by stakeholders.

This helps identify major discussion topics in policy debates.

4. Interactive Streamlit UI

LegisAl provides a user-friendly web interface where users can:

-> Analyze single comments

-> Upload a CSV file containing multiple comments

-> View sentiment charts and keyword word clouds

---

🏗️ System Architecture

Stakeholder Comments
        │
        ▼
Data Processing (Pandas)
        │
        ▼
AI Models (HuggingFace Transformers)
        │
 ┌───────────────┬───────────────┐
 ▼               ▼               ▼
Sentiment      Summary        Keyword
Analysis       Generation     Extraction
                                    │
                                    ▼
                        Word Cloud Visualization
                                    │
                                    ▼
                        Streamlit Interactive UI

---

🛠️ Tech Stack

Technology                      Purpose
Python                          Core programming language
HuggingFace Transformers        LLM-based NLP models
DistilBERT                      Sentiment Analysis
DistilBART                      Text Summarization
Pandas                          Data processing
Matplotlib                      Data visualization
WordCloud                       Keyword visualization
Streamlit                       Interactive web interface

---

📂 Project Structure
LegisAI
│
├── data/
│   └── data_comments.csv
│
├── outputs/
│   └── legisai_analysis_output.csv
│
├── LegisAI.ipynb
├── app.py
├── requirements.txt
└── README.md

---

▶️Run the Application locally

Start the Streamlit app: 

streamlit run app.py

The application will open in your browser

---

📊Example Workflow

User enters a stakeholder comment

2 LegisAl performs sentiment analysis

3 Generates an Al summary

4 Displays sentiment insights

5 Creates a word cloud from all comments

---

🌎Real-World Impact

LegisAl can be used by:

Government policy departments

Legislative research organizations

Public consultation platforms

Policy think tanks

It helps analyze public opinion faster and more accurately.

---

📌Future Improvements

Topic Modeling for policy themes

Multi-language support for Indian languages

Dashboard analytics for policy insights

Integration with government consultation portals

---

👩🏻‍💻Contributors

1. Sanvi Purohit (Team Lead)
   B.Tech Computer Science (Al Specialization)
   🔗https://www.linkedin.com/in/sanvi-purohit-77b7b9251
   
2. Riya Mittal
   B.Tech Computer Science (Al Specialization)
   🔗https://www.linkedin.com/in/riya-mittal-85b02a371
   