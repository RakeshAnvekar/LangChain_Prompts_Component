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

