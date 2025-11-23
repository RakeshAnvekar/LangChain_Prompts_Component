from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

chat_temlate=ChatPromptTemplate([
   ('system',"You are a helpful {domain} expert."),
   ('human',"Explain in simple terms whst is {topic}")]    
)

prompt=chat_temlate.invoke(
    {  
    "domain":"science",
    "topic":"quantum computing"
    })

print("Prompt Messages: ", prompt)

