import streamlit as st
from  langchain_logic.langchain_helper  import generate_pet_name , generate_memes

#I WANT TO TO GENERATE ME A TEMplate that takes in the function name and a list of the inputs and it generates a streamlit template ui for it


def create_ui_for_function(function_name : str , input_variables : list , function):
    st.title("LangChain")
    st.header(f"Generate {function_name}")
    for variable in input_variables:
        variable  = st.text_input(f"Enter {variable}")
    if st.button(f"Generate {function_name}"):
        st.write(function(**{variable : st.text_input(f"Enter {variable}") for variable in input_variables})["text"])


create_ui_for_function("meme" , ["meme_type"] , generate_memes)
