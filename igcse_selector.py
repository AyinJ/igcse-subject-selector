from openai import OpenAI
import streamlit as st

# Load OpenAI client using secret key stored securely in Streamlit Cloud
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit app title and instructions
st.title("🎓 IGCSE Subject Selector")
st.write("Answer a few simple questions to get personalized subject recommendations.")

# Questions for the student
strengths = st.text_input("💪 What subjects or topics are you good at or enjoy?")
dislikes = st.text_input("❌ Are there subjects you dislike or want to avoid?")
learning_style = st.text_input("🧠 How do you prefer to learn? (e.g. visual, hands-on, reading)")
balance = st.selectbox("⚖️ Do you want a balance of science, arts, and humanities?", ["Yes", "No"])
career_interest = st.text_input(
    "💼 What kind of job or career sounds exciting to you?",
    help="E.g. doctor, engineer, artist, YouTuber, business owner, not sure, etc."
)

# When the button is clicked, AI generates subject recommendations
if st.button("Get Subject Recommendations"):
    prompt = f"""
You are an academic advisor for IGCSE students. A student is unsure of their career path and is choosing subjects.
Here are their responses:
Strengths: {strengths}
Dislikes: {dislikes}
Learning style: {learning_style}
Wants balanced mix: {balance}
Career interests: {career_interest}

Suggest 5–6 IGCSE subjects. For each, explain in one sentence why it’s a good choice.
Format:
- Subject: [Name] – Reason: [short reason]
"""

    # OpenAI generates the response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Display the result in the app
    st.subheader("📚 Recommended IGCSE Subjects")
    st.write(response.choices[0].message.content.strip())
