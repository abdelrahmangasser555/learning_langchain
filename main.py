from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from fastapi import FastAPI
import os
app = FastAPI()
load_dotenv()

@app.get("/")
def generate_pet_name(color : str = "brown" , pet_type : str = "dog"):
    llm  =  OpenAI(temperature=0.9)
    prompt_template_name  = PromptTemplate(
        input_variables=["color" , "pet_type"],
        template="here is a {color} and a {pet_type} of a certain pet type geenrate some names for it and add emojies with the name ",
    )

    name_chain = LLMChain(llm = llm  , prompt = prompt_template_name )
    response  = name_chain({"color": color , "pet_type": pet_type})
    return response

if __name__ == "__main__":
    print(generate_pet_name("yellow" , "dog")["text"])

## how to run
# uvicorn main:app --reload