from langchain.llms import OpenAI
from langchain.agents import load_tools , initialize_agent , AgentType
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import LLMChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import os
import getpass
import pinecone

os.environ["PINECONE_API_KEY"] = getpass.getpass("Pinecone API Key:")

os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

os.environ["PINECONE_ENV"] = getpass.getpass("Pinecone Environment:")


loader = TextLoader("./test.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
    environment=os.getenv("PINECONE_ENV"),  # next to api key in console
)

index_name = "langchain-demo"



# First, check if our index already exists. If it doesn't, we create it
if index_name not in pinecone.list_indexes():
    # we create a new index
    pinecone.create_index(name=index_name, metric="cosine", dimension=1536)
# The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`
docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)

# if you already have an index, you can load it like this
# docsearch = Pinecone.from_existing_index(index_name, embeddings)

query = "What is the name inside the file ?"
docs = docsearch.similarity_search(query)
print(docs[0].page_content)