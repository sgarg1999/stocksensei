from app import inference_pipeline
import random

import os

import streamlit as st


spinner_texts = [
    'Doing financey stuff... :thinking_face:',
    'Let me get my sushi first... :sushi:',
    'Hold on, gotta take a quick nap... :sleepy:',
    'I really need to upgrade my internet...',
    'So... whats in this for me?'
]

img_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'data', 'img')

st.set_page_config(page_icon= os.path.join(img_path, 'stock_senpai.jpg'),
                   page_title= "⚔ Stock Sensei ⚔",
                   layout='wide')

def main():
    st.title("⚔ Stock Sensei ⚔")
    st.write("Enter a stock name and press submit to get Stock Sensei's verdict.")

    footer_content = '''
    **DISCLAIMER**: 
    \nStock Sensei is an AI tool built using LangChain and OpenAI's GPT-3.5-Turbo API.
    \nThe stock ratings and information provided by Stock Sensei are for informational purposes only, and should not at all be considered professional financial advice.
    \nThere is no guarantee of accuracy, and I will not be liable for any losses or taxes you incur. 
    \nAlways seek professional advice when deciding on trading.
    \nStock Sensei is an independent project, and is not affiliated with any companies or financial institutions.
    \n *Created by Shivam Garg*
    '''

    col1, padding, col2 = st.columns([5,3,10],)

    col1.write("\n\n")
    col2.write("\n\n\n\n")

    stock_name = st.text_input("Stock Name")

    st.markdown(footer_content)


    if st.button("Submit"):

        with st.spinner(text = random.choice(spinner_texts)):
            response = inference_pipeline(stock_name)
            
            response = response.replace('Could not parse LLM output: ', '')
        
        with col1:
            st.image(os.path.join(img_path, 'stock_senpai.jpg'), width=250, caption='Generated with MidJourney')
            # st.image('../data/img/stock_Sensei.jpg', width=250, caption='Generated with MidJourney')
        
        with col2:
            st.markdown(response)


# Run the app
if __name__ == '__main__':
    main()