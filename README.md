# LangChain Prompting and Chat Message Guide

This repository contains notes and examples related to **LangChain prompt templates**, message handling, and dynamic chat interactions.

---

## **1. Introduction to Prompts in LLMs**

Prompts are instructions or queries given to a Large Language Model (LLM) to guide its output.  
They are crucial because **the quality of the model’s output depends directly on how well prompts are designed**.

### **Types of Prompts**
1. **Text-based prompts**  
2. **Multi-modal prompts** (image, video, audio, etc.)

---

## **2. Why Use `PromptTemplate` Instead of f-strings?**

While f-strings can dynamically insert data into text, `PromptTemplate` provides key advantages:

### **Benefits of PromptTemplate**
| Feature | Description |
|---------|------------|
| **Validation** | Built-in validation using `validate_template=True` |
| **Reusability** | Templates can be stored as JSON and reused |
| **Integration** | Fully compatible with LangChain ecosystem |

### **Example**

from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template="Write a {length_input}-length summary of {paper_input} in {style_input} style.",
    validate_template=True
)
# Messages in LangChain

LangChain provides structured message types to support conversational AI workflows. Instead of sending raw text prompts, messages help instruct the model with clear roles and context.

---

## **3. Message Types in LangChain**

LangChain supports three primary message types:

| Message Type     | Purpose                     | Example                                           |
|------------------|-----------------------------|---------------------------------------------------|
| **SystemMessage** | Defines system-level instructions (rules, behavior). | `"You are a helpful assistant."` |
| **HumanMessage**  | Represents user input.      | `"Tell me the capital of India."` |
| **AIMessage**     | Represents model output.    | `"The capital of India is New Delhi."` |

These messages allow structured control over a conversation, enabling multi-turn chat, role alignment, and better context management.

---

## **4. Using the `invoke()` Method**

The `invoke()` method sends prompts or message lists to the model.

### **When to Use**
| Scenario | Usage |
|----------|-------|
| **Single query** | Send a single message |
| **Multi-turn chat** | Pass a list of messages |

---

### **Example — Multi-message Interaction**

from langchain.schema import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me the capital of India.")
]

response = model.invoke(messages)

# 5. Dynamic Messages with `ChatPromptTemplate`

`ChatPromptTemplate` allows you to create prompts that support dynamic variables and structured message formatting. This is useful when building chat-based workflows, where different roles (system, human, AI) need template-driven content.

### **Example**


from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful {domain} expert."),
    HumanMessage(content="Explain about {topic}.")
])
## 6. Using `MessagePlaceholder`

`MessagePlaceholder` is used to inject previous conversation history into a new prompt so the model can maintain context in a multi-turn conversation. Without this, LLMs treat each message independently and forget prior interactions.

---

### 📌 Scenario: Refund Support Conversation

A user contacts support:

| Role | Message |
|------|---------|
| **User** | "I need a refund." |
| **Bot** | "Amount will be refunded in 3–5 working days." |
| *(Later)* |
| **User** | "What is the status of my refund?" |

If we send only the final query, the model does not know what refund is being referenced.  
By injecting history via `MessagePlaceholder`, the model sees the entire conversation and responds appropriately.

---

### 🔧 Example

```python
from langchain.prompts.chat import ChatPromptTemplate
from langchain.prompts.chat import MessagePlaceholder
from langchain.schema import HumanMessage, SystemMessage

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful support assistant."),
    MessagePlaceholder(variable_name="history"),  # Inject previous conversation
    HumanMessage(content="What is the status of my refund?")
])
<img width="940" height="490" alt="image" src="https://github.com/user-attachments/assets/d5f9307f-3180-4730-94c9-890bcb2d52f3" />
###  Dynamic Prompt
<img width="940" height="490" alt="image" src="https://github.com/user-attachments/assets/d5f9307f-3180-4730-94c9-890bcb2d52f3" />
### Basic ChatBot Without Context History
<img width="940" height="552" alt="image" src="https://github.com/user-attachments/assets/7d47f788-1818-4ba9-9aa2-fd86064ddf25" />  
<img width="940" height="491" alt="image" src="https://github.com/user-attachments/assets/82cb333a-e2a4-4110-a4cc-d65d7d508b7d" />
### Basic ChatBot With Context History
<img width="940" height="526" alt="image" src="https://github.com/user-attachments/assets/5b27f42d-597f-4664-bc4a-81ad6cda512b" />
### Chat Bot with Chat History 
    In below we are not able to find who has sent the message bot or user, its very difficult to llm model to understand
<img width="940" height="526" alt="image" src="https://github.com/user-attachments/assets/9c10bb7e-bb1d-43db-a9f8-d9cea8a7b791" />
### Chat Bot with Chat History -Human Message,AI Message,System Message
<img width="940" height="489" alt="image" src="https://github.com/user-attachments/assets/2013d669-5eff-4bc2-b902-fc3fdaa2ada1" />
### ChatPromptTemplate
<img width="940" height="406" alt="image" src="https://github.com/user-attachments/assets/25a40645-0fee-4537-96b4-2bd0819a8d88" />
### MessagePlaceHolder
<img width="940" height="518" alt="image" src="https://github.com/user-attachments/assets/46f04f8d-d005-400c-a198-b7136f09df19" />








