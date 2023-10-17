import os
import streamlit as st


def get_openai_token():

    openai_key = st.secrets['OPENAI_API_KEY']
    
    return openai_key