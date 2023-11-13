from langchain.llms import OpenAI
from langchain.agents import load_tools , initialize_agent , AgentType
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import LLMChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
# import os
# import getpass
import pinecone

pinecone.init(
    api_key="4d11f4e1-f222-4882-a042-3ecba7bf030d",  # find at app.pinecone.io
    environment="northamerica-northeast1-gcp",  # next to api key in console
)

# import dotenv

# dotenv.load_dotenv()



print("starting...")

loader = TextLoader("./test.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

print("splitting documents done")

embeddings = OpenAIEmbeddings()

print("starting initialization...")


print("done initialization")

index_name = "langchain-demo"

print("creating index...")
docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)
print("done")

# if you already have an index, you can load it like this
docsearch = Pinecone.from_existing_index(index_name, embeddings)

query = "What is the name inside the file ?"
docs = docsearch.similarity_search(query)
print(docs[0].page_content)