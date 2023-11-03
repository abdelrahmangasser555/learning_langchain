from langchain_logic.langchain_helper import generate_pet_name , generate_memes
import streamlit as st

def template_testing( title : str = "testing" , titles : list = ["testing"]  , function_type : str = "pet_name"):

    #set the function acording to the function type
    if function_type == "pet_name":
        function = generate_pet_name
    elif function_type == "meme":
        function = generate_memes
    else:
        raise ValueError("function_type must be pet_name or meme")
    #adding a title
    st.title(title)

    #setting up the inputs
    if function_type == "pet_name":
        color = st.text_input("color" , value = "ex : brown")
        pet_type = st.text_input("pet_type" , value = "ex : dog")
        # creating a generate button
        st.button("generate name")
    elif function_type == "meme":
        meme_type = st.text_input("meme_type" , value = "ex : funny")
        # creating a generate button
        st.button("generate meme")


    #creating a response only when the button is pressed
    if st.button == False:
        if function_type == "pet_name":
            response = function(color = color , pet_type = pet_type)
        elif function_type == "meme":
            response = function(meme_type = meme_type)

        st.write(response["text"])

template_testing( title = "meme generator "  , function_type = "meme")
st.write("--------------------------------------------------")

template_testing( title = "pet name generator "  , function_type = "pet_name")

st.camera_input()