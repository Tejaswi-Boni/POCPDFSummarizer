from langchain.prompts import PromptTemplate

#Define prompt template
prompt_template = """
You are a helpful AI assistant. Use the following context to answer the question concisely:

Context:
{context}

Question:
{question}

Answer in clear, structured language.
"""

PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template
)
