from langchain.tools import tool
from langchain.agents import load_tools , initialize_agent , AgentType
from langchain.prompts import HumanMessagePromptTemplate , AIMessagePromptTemplate , PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain



def generate_code(prompt):
    model  = OpenAI(temperature = 0)
    prompt  = PromptTemplate(
        input_variables = ["problem"],
        template = "you are a very skilled proggramer you take in a problem in proggramming and you only return the most suitable answer for it in c++ you return only the code "
    )
    problem  = input("enter a problem solving question ")
    chain = LLMChain()
