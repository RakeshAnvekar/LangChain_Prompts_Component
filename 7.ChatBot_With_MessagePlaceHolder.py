from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate
from langchain_core.messages import HumanMessage

# Chat Template
chat_Template=ChatPromptTemplate([
    ('system',"You are a helpful customer support agent."),

    MessagesPlaceholder(variable_name='chat_history'),
    
    ('human',"{query}"),
])


#load the Chat history
chat_history = []
with open('chat_history.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:
            chat_history.append(line)

prompt= chat_Template.invoke(
    {
        "chat_history": chat_history,
        "query": "What is the status of my refund?"
    }
)

print("Prompt Messages: ", prompt)
# Create prompts
