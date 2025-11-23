from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

# this chat bot should run infine time in loop until user wants to exit

while True:
    user_input = input("You: ")
    if(user_input.lower() in ['exit', 'quit', 'bye']):
        print("ChatBot: Goodbye!")
        break
    result= model.invoke(user_input)
    print("ChatBot: ", result.content)
