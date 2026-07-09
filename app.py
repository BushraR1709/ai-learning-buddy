
import streamlit as st
from google import genai

# Create Gemini client
api_key = st.secret["OPEN_API_KEY"]

# Page configuration
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 AI Learning Buddy")

st.write("Learn any topic with your AI Learning Buddy!")

# User Input
topic = st.text_input("Enter a Topic")

# Activity Selection
option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

# Generate Button
if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"""
            Explain {topic} in simple language for a beginner.
            Use simple words and step-by-step explanation.
            """

        elif option == "Real-Life Example":
            prompt = f"""
            Give one simple real-life example of {topic}.
            """

        elif option == "Generate Quiz":
            prompt = f"""
            Create 5 multiple choice questions on {topic}.

            For each question provide:
            - Four options (A, B, C, D)
            - Correct Answer
            """

        else:
            prompt = topic

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.success("Response Generated Successfully!")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
