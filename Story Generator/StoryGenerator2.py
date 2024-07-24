import os
import streamlit as st
from langchain.chains import LLMChain
from langchain.llms import Cohere as OpenAI
from langchain.prompts import PromptTemplate

OPENAI_API_KEY = "o4SMHvCR9cSvNRtc2f8QtL6uEqXWfAo5mnNVF6Gn"

#OPENAI_API_KEY = ""

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = OpenAI(cohere_api_key=OPENAI_API_KEY)

prompt_template = PromptTemplate(
    input_variables=["prompt"],
    template="Write a science fiction story based on the following topic: {prompt}"
)

chain = LLMChain(llm=llm, prompt=prompt_template)

def generate_story(prompt):
    response = chain.run({"prompt": prompt})
    return response.strip()

st.title("Science Fiction Story Generator")

prompt = st.text_input("Prompt", "Enter a Topic")

if st.button("Create a Story"):
    if prompt:
        with st.spinner("Writing a science fiction story..."):
            try:
                story = generate_story(prompt)
                st.write(story)
            except Exception as e:
                st.error(f"Error generating story: {e}")
    else:
        st.warning("Please enter a Topic to generate a story.")
