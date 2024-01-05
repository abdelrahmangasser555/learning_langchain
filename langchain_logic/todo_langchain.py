from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import fastapi
import json


app = fastapi.FastAPI()

# @app.get("/creating_todos")
def create_todos(todo : str):
    llm  = OpenAI(temperature = 0.1)
    template = """here is a todo item {todo} , As a proficient todo list maker, generate your task is to break down a given todo item into smaller tasks, providing the breakdown in JSON make two keys  the first the title of the todo and the secont a list of dictionaries having the tasks  . Each task should include an explanation and the approach you plan to use. Present the breakdown in concise steps.

    Example:
    Todo Item: "Build a Todo App"

    Breakdown:
    
      "Step 1": "Task": "Define Requirements", "Explanation": "Understand required functionalities and features.",
      "Step 2": "Task": "Set Up Dev Environment", "Explanation": "Install necessary tools and set up version control.",
      "Step 3": "Task": "Create UI/UX Design", "Explanation": "Design user interface and experience.",
      "Step 4": "Task": "Implement Backend", "Explanation": "Develop server-side logic and data management.",
      "Step 5": "Task": "Build Frontend", "Explanation": "Develop client-side components and user interactions.",
      "Step 6": "Task": "Connect Backend and Frontend", "Explanation": "Establish communication between components.",
      "Step 7": "Task": "Test and Debug", "Explanation": "Thoroughly test the application and fix issues.",
      "Step 8": "Task": "Deploy and Monitor", "Explanation": "Deploy to production and monitor performance."
    
    """
    prompt = PromptTemplate(
        input_variables=["todo"],
        template=template
    )

    chain = LLMChain(llm = llm , prompt = prompt)
    response  = chain({"todo": todo})

    return response

data  = create_todos("have a dinner ")["text"]
print(type(data))
print("---------------------")
print(data)

with open("romantic.txt" , "a") as r:
    r.write(data)

