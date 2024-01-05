from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import AgentType , initialize_agent , load_tools
import streamlit as st
import time


def discrete_project_using_llm_chain(user_input):
    llm  = OpenAI(temperature=0.4)
    prompt = PromptTemplate(
        input_variables=["question"],
        template="You are a skilled instructor in discrete mathematics. Presented with a discrete mathematics question {question}, your task is to deconstruct it into smaller, manageable sub-problems. Approach each of these sub-problems methodically, solving them one by one. Please provide a comprehensive explanation for each step taken during the problem-solving process, ensuring that the logic and reasoning behind each decision are clearly articulated. Conclude by presenting the final answer, encapsulating the resolution of the initial question. For this exercise, rely solely on your expertise in discrete mathematics; do not use the internet or external resources to find the solution. ",
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
        my_bar = st.progress(0)

        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        st.write(answer)
    else:
        st.write("Please enter a question.")

# when the button is submiting it should show the loading bar

