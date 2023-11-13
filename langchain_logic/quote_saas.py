from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()

load_dotenv()


@app.get("/")
def wise_quote_generator(question : str):
    llm = OpenAI(temperature=0)
    quote_prompt_template  = PromptTemplate(
        input_variables=["structure"],
        template="you are a wise person who is so smart and wise here is a topic : {structure} from your knowlege about all the wise people like sokratize and so one generate a very wise  generate me a wise quote on this topic do not exceed 20 words and not less than 10 words make it meaningful and full of wisdom here is some examples "
                 "topic : life quote : life is a journey not a destination "
                 "topic : love quote : love is a beautiful thing "
                 "topic : money quote : money is the root of all evil ",
    )
    chain  = LLMChain(llm = llm , prompt = quote_prompt_template )
    result = chain({"structure": question})
    return result["text"]

if __name__ == "__main__":
    question = input("enter a topic  ")
    result = wise_quote_generator(question)
    print(result)