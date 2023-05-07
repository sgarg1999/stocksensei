import os
from langchain.prompts import PromptTemplate



def load_prompt_template(prompt_style = 'financial_advisor'):

    prompts_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'data', 'prompts')


    if prompt_style == 'financial_advisor':

        with open( os.path.join(prompts_path, 'fin_advisor_prompt.txt'),
                   'r') as file:
            prompt_template = file.read().replace('\n', '')

    return prompt_template



def generate_prompt_obj(prompt_template, input_variables, company):

    prompt = PromptTemplate(input_variables=input_variables, template = prompt_template)


    formatted_prompt = prompt.format(company = company)
    return formatted_prompt
