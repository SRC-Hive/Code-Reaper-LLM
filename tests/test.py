import os
import dotenv

from langchain_cohere.chat_models import ChatCohere
from langchain_milvus import Milvus, Zilliz
from langchain_cohere import CohereEmbeddings
from langchain_openai import OpenAIEmbeddings

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    PromptTemplate,
    MessagesPlaceholder
)
from langchain_core.output_parsers import StrOutputParser

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


store = {}  # memory is maintained outside the chain

def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

dotenv.load_dotenv()

main_prompt_str = """
    You are a chatbot created for the purposes of interpreting and understanding large codebases, 
    repositories and open source projects. Your jobs is to use the context and your prior
    knowledge in order to answer questions that a user may have.

    {context}
        
    {question}
    """

system_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["context"],
        template=main_prompt_str
    )
)

history = MessagesPlaceholder("history")

human_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["question"],
        template="{question}"
    )
)

messages = [system_prompt, history, human_prompt]

chat_prompt = ChatPromptTemplate(
    input_variables=["context", "history", "question"],
    messages = messages
)

output_parser = StrOutputParser()

# Importing models
model = ChatCohere(cohere_api_key=os.getenv("COHERE_API_KEY"), temperature=0.7)
chain = chat_prompt | model | output_parser


chain_new = RunnableWithMessageHistory(chain, get_session_history=get_session_history, input_messages_key="question", history_messages_key="history")

def get_bot_response(x):
    return chain_new.invoke(
        input={"context" : "No additional context available", "question" : x}, 
        config={"configurable": {"session_id": "1"}}
)

if __name__ == "main":
    pass