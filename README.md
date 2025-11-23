# LangChain Prompting and Chat Message Guide

This repository contains notes and examples related to **LangChain prompt templates, messages, and dynamic chat handling**.

---

## 1. Prompts in LLMs

Prompts are instructions or queries given to a model to guide its output. They are essential because the **output of an LLM depends directly on the prompts**.

### Types of Prompts
1. **Text-based prompts**
2. **Multi-modal prompts** (image, video, audio, etc.)

---

### Why use `PromptTemplate` instead of f-strings?

While f-strings can be used for dynamic text insertion, `PromptTemplate` provides:

- **Validation**: Built-in input validation using `validate_template=True`.
- **Reusability**: Templates can be saved as JSON and reused across multiple prompts.
- **Integration with LangChain**: Fully compatible with the ecosystem.

Example:

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template="Write a {length_input}-length summary of {paper_input} in {style_input} style.",
    validate_template=True
)

2. Messages in LangChain

LangChain supports three types of messages:

SystemMessage – System-level instructions, e.g., "You are a helpful assistant."

HumanMessage – Messages sent by the user, e.g., "Tell me the capital of India."

AIMessage – Responses from the model, e.g., "The capital of India is New Delhi."

3. Using the invoke Method

The invoke method allows sending messages to the model:

Single message: Useful for standalone queries.

List of messages: Used in multi-turn conversations.

Example of static messages:

from langchain.schema import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me the capital of India.")
]

response = model.invoke(messages)

4. Dynamic Messages with ChatPromptTemplate

ChatPromptTemplate allows dynamic content in messages. For example:

from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful {domain} expert."),
    HumanMessage(content="Explain about {topic}.")
])
MessagePlaceholder

MessagePlaceholder is used to inject previous chat history or dynamic messages into a conversation.

Example scenario:

A user asks a chatbot for a refund.

Chatbot responds: "Amount will be refunded in 3-5 working days."

User comes back asking: "What is the status of my refund?"

Solution: Use MessagePlaceholder to include the previous chat history in the new conversation.

from langchain.prompts.chat import ChatPromptTemplate
from langchain.prompts.chat import MessagePlaceholder

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful support assistant."),
    MessagePlaceholder(variable_name="history"),  # Inject previous conversation
    HumanMessage(content="What is the status of my refund?")
])