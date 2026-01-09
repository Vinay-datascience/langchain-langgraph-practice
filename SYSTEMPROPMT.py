from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage
from pydantic import BaseModel


llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-lite-latest",
    temperature=0.7
)

system_prompt = """
You are a science fiction writer.
Create fictional capital cities for planets.
"""


question = HumanMessage(content="What is the capital of the Moon?")


response = llm.invoke([
    SystemMessage(content=system_prompt),
    question
])

print(response.content)


