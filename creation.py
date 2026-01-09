from langchain_google_genai import ChatGoogleGenerativeAI

# Create the LLM
llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-lite-latest",
)

# Ask a question
response = llm.invoke("What's the capital of the Moon?")

# Print the answer
print(response.content)

