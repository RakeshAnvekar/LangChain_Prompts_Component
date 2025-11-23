from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()


chat_History=[]
   


# this chat bot should run infine time in loop until user wants to exit

while True:
    user_input = input("You: ")
    chat_History.append(content=user_input)
    if(user_input.lower() in ['exit', 'quit', 'bye']):
        print("ChatBot: Goodbye!")
        break
    result= model.invoke(chat_History)
    chat_History.append(content=result.content)
    print("ChatBot: ", result.content)
    
print("Chat History: ", chat_History)