import os
import dotenv

from langchain_cohere.chat_models import ChatCohere
from langchain_core.messages import AIMessage, HumanMessage

dotenv.load_dotenv()

llm = ChatCohere(cohere_api_key=os.getenv("COHERE_API_KEY"))
message = [HumanMessage(content="Hi, whats up?")]

print(llm(message))
