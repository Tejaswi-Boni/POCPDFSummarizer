
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from PDFbot.data_ingestion import ingestdata
from PDFbot.prompt import PROMPT
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

def generation():

    # Initialize OpenAI LLM

    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo", 
        temperature=0,
        openai_api_key=OPENAI_API_KEY)
    
    # Define a chain for generation
    generation_chain = LLMChain(
        llm=llm,
        prompt=PROMPT
    )

    return generation_chain

def generate_answer(question):
    qdrant_store = ingestdata()
    
    # 1. Retrieve relevant documents
    retriever = qdrant_store.as_retriever(search_kwargs={"k": 3})

    docs = retriever.get_relevant_documents(question)
    context = "\n".join([doc.page_content for doc in docs])

    # 2. Generate answer using the LLM
    generation_chain=generation()
    answer = generation_chain.run(context=context, question=question)
    return answer

# if __name__ == "__main__":
#     question = "What is correlation in statistics?"
#     answer, docs = generate_answer(question)
#     print("Answer:\n", answer)