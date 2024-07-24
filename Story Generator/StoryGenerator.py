import os
import streamlit as st
from langchain.chains import LLMChain
from langchain.llms import Cohere as c
from langchain.prompts import PromptTemplate

#COHERE_API_KEY = "o4SMHvCR9cSvNRtc2f8QtL6uEqXWfAo5mnNVF6Gn"

COHERE_API_KEY = ""

os.environ["COHERE_API_KEY"] = COHERE_API_KEY

llm = c(cohere_api_key=COHERE_API_KEY)

prompt_template = PromptTemplate(
    input_variables=["prompt"],
    template="Write a science fiction story based on the following topic: {prompt}"
)

chain = LLMChain(llm=llm, prompt=prompt_template)

def generate_story_arc(prompt):
    response = chain.run({"prompt": prompt})
    return response.strip()

st.title("Science Fiction Story Generator")

prompt = st.text_input("Prompt", "Enter a Topic")

if st.button("Create a Story"):
    if prompt:
        with st.spinner("Writing a science fiction story..."):
            try:
                story_arc = generate_story_arc(prompt)
                st.write(story_arc)
            except Exception as e:
                st.error(f"Error generating story: {e}")
    else:
        st.warning("Please enter a Topic to generate a story.")
