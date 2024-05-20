import streamlit as st
#from langchain.llms import OpenAI
from langchain_openai import OpenAI

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')  # Secure API key input

def generate_response(input_text):
    try:
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        response = llm.invoke(input_text)  # Ensure we use the 'invoke' method as per LangChain v0.2
        st.info(response)
    except Exception as e:
        st.error(f"Error generating response: {e}")

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    
    if not openai_api_key:
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    elif not openai_api_key.startswith('sk-'):
        st.warning('Invalid OpenAI API key format!', icon='⚠')
    elif submitted:
        generate_response(text)
