
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

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template="Write a {length_input}-length summary of {paper_input} in {style_input} style.",
    validate_template=True
)
```

---

## **3. Message Types in LangChain**

LangChain supports three primary message types:

| Message Type     | Purpose                     | Example                                           |
|------------------|-----------------------------|---------------------------------------------------|
| **SystemMessage** | Defines system-level instructions (rules, behavior). | `"You are a helpful assistant."` |
| **HumanMessage**  | Represents user input.      | `"Tell me the capital of India."` |
| **AIMessage**     | Represents model output.    | `"The capital of India is New Delhi."` |

---

## **4. Using the `invoke()` Method**

The `invoke()` method sends prompts or message lists to the model.

### **Example — Multi-message Interaction**
```python
from langchain.schema import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me the capital of India.")
]

response = model.invoke(messages)
```

---

## **5. Dynamic Messages with `ChatPromptTemplate`**

`ChatPromptTemplate` allows you to create dynamic chat-based prompts using structured roles.

```python
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful {domain} expert."),
    HumanMessage(content="Explain about {topic}.")
])
```

---

## **6. Using `MessagePlaceholder` (Maintaining Chat History)**

LLMs do not remember previous messages automatically.  
`MessagePlaceholder` inserts past conversation history into new prompts.

### 📌 Example Scenario

User: `"I need a refund."`  
Bot: `"Amount will be refunded in 3–5 days."`  
Later User: `"What is the status of my refund?"` → Without context, model forgets.

### **Example**
```python
from langchain.prompts.chat import ChatPromptTemplate
from langchain.prompts.chat import MessagePlaceholder
from langchain.schema import HumanMessage, SystemMessage

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful support assistant."),
    MessagePlaceholder(variable_name="history"),
    HumanMessage(content="What is the status of my refund?")
])
```

---

## **7. Visual References**

### Dynamic Prompt
![Dynamic Prompt](https://github.com/user-attachments/assets/d5f9307f-3180-4730-94c9-890bcb2d52f3)

### Basic ChatBot Without Context History
![Without History](https://github.com/user-attachments/assets/7d47f788-1818-4ba9-9aa5-fd86064ddf25)

### Basic ChatBot With Context History
![With History](https://github.com/user-attachments/assets/5b27f42d-597f-4664-bc4a-81ad6cda512b)

### ChatPromptTemplate
![ChatPromptTemplate](https://github.com/user-attachments/assets/25a40645-0fee-4537-96b4-2bd0819a8d88)

### MessagePlaceholder
![MessagePlaceholder](https://github.com/user-attachments/assets/46f04f8d-d005-400c-a198-b7136f09df19)

---

### **✔ Saved Successfully**

