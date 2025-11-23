from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatOpenAI()

st.header("Research Tool using LLM Dynamic-Prompt")
st.subheader("Chat with GPT-4")

paper_input = st.selectbox("Select Paper Topic:", 
                           ["AI in Healthcare","Climate Change","Quantum Computing","Renewable Energy","Cybersecurity"])

style_input = st.selectbox("Select Summary Style:", 
                           ["Bullet Points","Paragraph","Executive Summary","Infographic Style","Q&A Format"])

length_input = st.selectbox("Select Summary Length:", 
                            ["Short (100 words)","Medium (250 words)","Long (500 words)"])

template=load_prompt("template.json", validate_template=True)

prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})

if st.button("summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
