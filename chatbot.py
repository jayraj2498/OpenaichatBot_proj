from langchain_community.llms import OpenAI  # Correct import statement
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Get the secret key from the environment variable
secrete_key = os.getenv("OPENAI_API_KEY")

# Check if the secret key was loaded correctly
if not secrete_key:
    raise ValueError("OpenAI API key not found. Please set it in the .env file.")

def get_openai_response(question):
    try:
        # Initialize the OpenAI model with the correct keyword argument
        llm = OpenAI(api_key=secrete_key, temperature=0.5) 
        response = llm(question)
        return response
    except Exception as e:
        return str(e)

# Set up the Streamlit app
st.set_page_config(page_title="Q&A Demo Chatbot")
st.header("Langchain Application")

# Input text from the user
user_input = st.text_input("Input:", key="input")

# Button to submit the question
submit = st.button("Ask Your Question")

# If the button is pressed, get the response and display it
if submit and user_input:
    response = get_openai_response(user_input)
    st.subheader("The Response is:")
    st.write(response)
