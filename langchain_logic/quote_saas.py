from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.agents import AgentType , initialize_agent , load_tools
from langchain.tools import tool
from fastapi import FastAPI
from quotes_array import quotes
import random


app = FastAPI()

load_dotenv()

wisdom_quotes = quotes

@app.get("/")
def wise_quote_generator(question : str):
    llm = OpenAI(temperature=0)
    quote_prompt_template  = PromptTemplate(
        input_variables=["topic"],
        template="generater me a wise and usefull quote inspired by on this topic {topic}"

    )
    chain  = LLMChain(llm = llm , prompt = quote_prompt_template )
    result = chain({"topic": question})
    return result["text"]

@app.get("/agent")
def wise_quote_agent(quote : str = "meaning of life"):
    wise_quotes_example = quote
    llm  = OpenAI(temperature = 0.5)
    load_tools_agent = load_tools(["serpapi"])
    agent  = initialize_agent(
        tools=load_tools_agent ,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION ,
        verbose = True ,
        llm = llm
    )
    respone = agent.run(f"generate a very meaningfull and wise quote on this topic {quote}")
    return respone


@app.get("/wisdomRandom")
def wisdom_random():
    random_quote = random.choice(wisdom_quotes)
    return random_quote

# command to run
# uvicorn quote_saas:app --reload
#complete path for file is
#
if __name__ == "__main__":
    for i in range(5):
        print(wisdom_random() , "\n")