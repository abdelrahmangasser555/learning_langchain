from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import initialize_agent , load_tools , AgentType



load_dotenv()

def langchain_agent(question):
    llm = OpenAI(temperature=0.9)
    prompt_template_structure  = PromptTemplate(
        input_variables=["structure"],
        template="here is a {structure} generate me a story with emojies with it the story should me more than 30 words",
    )
    tools = load_tools(["serpapi" , "llm-math"] , llm = llm)
    agent  = initialize_agent(
        tools = tools,
        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION ,
        llm = llm ,
        verbose = True
    )
    question = input("eneter a question to search the internet ")
    result = agent.run(question)
    print(result)
