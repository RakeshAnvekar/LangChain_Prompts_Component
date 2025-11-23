from  langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()


model= ChatOpenAI(model_name="gpt-4", temperature=0)

st.header("Research Tool using LLM Prompts")

st.subheader("Chat with GPT-4")

userInput=st.text_input("Enter your prompt here:")

if st.button("summarize"):
   result=model.invoke(userInput)
   st.write(result.content)
