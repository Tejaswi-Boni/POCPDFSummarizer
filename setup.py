from setuptools import find_packages, setup

setup(
    name="PDFbot",
    version="0.0.1",
    author="Tejaswi",
    author_email="tejaswi1314@gmail.com",
    packages =find_packages(),
    install_requires=["langchain","langchain-openai","openai","langchain_community","datasets","pypdf","python-dotenv","flask","tiktoken","qdrant-client"]
)