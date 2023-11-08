from langchain.llms import OpenAI
from langchain.agents import load_tools , initialize_agent , AgentType
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone
load_dotenv()

embeddings = OpenAIEmbeddings()
def youtube_agent(vedio_url):
    llm  = OpenAI()
    loader = YoutubeLoader.from_youtube_url(vedio_url)
    transcript  = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000 , chunk_overlap=100)
    docs  = splitter.split_documents(transcript)

    db = Pinecone.add_documents()
