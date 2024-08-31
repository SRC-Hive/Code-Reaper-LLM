import os
import dotenv

from langchain_cohere.chat_models import ChatCohere
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import PromptTemplate

dotenv.load_dotenv()


prompt_template = PromptTemplate.from_template(
    "Tell me about the Open Source project {name}."
)

# Importing models
llm = ChatCohere(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    temperature=0.7
)
# message = [HumanMessage(content="Hi, whats up?")]

chain = prompt_template | llm
response = chain.invoke({"name": "AWS CDK"})

print(response)
