from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-lite-latest",
    temperature=0
)

print(llm.invoke("Hello Gemini test").content)
