import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from src.retriever import retrieve_documents


# Load .env variables
load_dotenv()
print(os.getenv("GOOGLE_API_KEY"))


def create_chatbot():
    """
    Create Gemini LLM.
    """

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.2
    )

    return llm


def ask_question(question, chat_history=None):
    """
    Ask a question using RAG.
    """
    if chat_history is None:
        chat_history = []
    
    conversation = ""
    for message in chat_history[-6:]:   # Last 6 messages
        role = message["role"].capitalize()
        conversation += f"{role}: {message['content']}\n"

    # Retrieve relevant chunks
    results = retrieve_documents(question)
    documents = results["documents"]
    sources = results["sources"]
    print("\n==============================")
    print("Retrieved Metadata")
    print("==============================")
    print(sources)
    context = "\n\n".join(documents)

    prompt = f"""
You are an AI College Assistant.

You should answer naturally while considering the previous conversation.

Use ONLY the retrieved document context to answer factual questions.

If the answer cannot be found in the context, reply:

"I couldn't find this information in the uploaded college documents."

--------------------------
Conversation History
--------------------------

{conversation}

--------------------------
Retrieved Context
--------------------------

{context}

--------------------------
Current Question
--------------------------

{question}

--------------------------
Answer
--------------------------
"""

    llm = create_chatbot()

    response = llm.invoke(prompt)

    answer = response.content

    # Remove duplicate sources
    unique_sources = []

    for item in sources:
        source = item["source"]

        if source not in unique_sources:
            unique_sources.append(source)

    answer += "\n\n---\n"
    answer += "📄 **Sources:**\n\n"
    shown = set()
    for item in sources:
        key = (item["source"], item["page"])
        if key not in shown:
            shown.add(key)
            answer += f"- {item['source']} (Page {item['page']})\n"

    return answer