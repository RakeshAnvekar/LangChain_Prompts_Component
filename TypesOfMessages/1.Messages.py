from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about India")
]

result= model.invoke(messages)


messages.append(AIMessage(result.content))

print(messages)


