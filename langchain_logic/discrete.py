from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import AgentType , initialize_agent , load_tools
import streamlit as st
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.llms import OpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
import time
from dotenv import load_dotenv
import os



load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


def creating_agent(question):
    llm = OpenAI(temperature=0.3)
    tools = load_tools(["tavily_search"], llm=llm)
    prompt = PromptTemplate(
        input_variables=["question"],
        template="You are a skilled instructor in discrete mathematics. Presented with a discrete mathematics question {question}, your task is to deconstruct it into smaller, manageable sub-problems. Approach each of these sub-problems methodically, solving them one by one. Please provide a comprehensive explanation for each step taken during the problem-solving process, ensuring that the logic and reasoning behind each decision are clearly articulated. Conclude by presenting the final answer, encapsulating the resolution of the initial question. For this exercise, rely solely on your expertise in discrete mathematics; do not use the internet or external resources to find the solution. ",
    )
    llm = OpenAI()
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor.invoke({"input": question})


def discrete_project_using_llm_chain(user_input):
    llm  = OpenAI(temperature=0.4 , max_tokens=3000)
    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
        Assume the role of an expert discrete mathematics tutor. When faced with a discrete mathematics query {question}, your objective is to dissect it into more digestible, smaller segments. Tackle each of these segments with a systematic approach, resolving them sequentially. Your response should include a thorough and well-articulated explanation for each step of the problem-solving journey, highlighting the rationale and principles guiding each decision. Conclude your explanation by presenting the final solution, which addresses the initial query comprehensively. In your response, rely exclusively on your knowledge of discrete mathematics without resorting to the internet or other external sources. Structure your answer in Markdown format, including the use of LaTeX for mathematical symbols, tables, and titles. For text coloration in Markdown, here’s an example format: :blue[gasser] for coloring the word 'gasser' in blue. Ensure your answer adheres to Markdown syntax for effective presentation
    """,
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain({"question": user_input})
    return response["text"]




st.title('Discrete Math Problem Solver')

# Input text box
user_input = st.text_input("Enter your discrete math question:")

# Button to generate response
if st.button('Generate'):
    if user_input:
        answer = discrete_project_using_llm_chain(user_input)
        ## make the loading bar
        st.markdown(answer)
    else:
        st.write("Please enter a question.")

# when the button is submiting it should show the loading bar

