from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()


chat_History=[
    SystemMessage(content="You are a helpful assistant.")
]

# this chat bot should run infine time in loop until user wants to exit

while True:
    user_input = input("You: ")
    chat_History.append(HumanMessage(content=user_input))
    if(user_input.lower() in ['exit', 'quit', 'bye']):
        print("ChatBot: Goodbye!")
        break
    result= model.invoke(chat_History)
    chat_History.append(AIMessage(content=result.content))
    print("ChatBot: ", result.content)
    
print("Chat History: ", chat_History)