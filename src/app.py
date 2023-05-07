from llm import init_gpt, init_agent
from tools import init_tools
from load_prompts import load_prompt_template, generate_prompt_obj
import os
import openai



import nltk


print_logs = True
verbose = True


def generate_response(agent, prompt):
    try:
        response = agent.run(prompt)

    except Exception as e:
                response = str(e)
                if response.startswith("Could not parse LLM output: `"):
                    response = response.removeprefix("Thought:Could not parse LLM output: `").removesuffix("`")
                    
                    final_answer = response

    final_answer = response
    final_answer.replace("Thought:Could not parse LLM output: ","")
    final_answer.replace("Could not parse LLM output: ","")

    return final_answer 
     


def inference_pipeline(input_stock_name):
    nltk.download(['vader_lexicon'])

    if print_logs:
        print("Fetching OpenAI Token...")
    #------------------------------------------------------------------------------------
    # Initialize Model
    #------------------------------------------------------------------------------------
    if print_logs:
        print("Initiliazing model...")

    llm = init_gpt()

    if print_logs:
        print("Model loaded")

    #------------------------------------------------------------------------------------
    # Initialize Tools
    #------------------------------------------------------------------------------------
    if print_logs:
        print("Loading tools...")

    tools = init_tools()
    
    if print_logs:
        print("Done", tools)

    #------------------------------------------------------------------------------------      
    # Init zero_shot_agent
    #------------------------------------------------------------------------------------
    
    if print_logs:
        print("Initializing agent...")        

    zero_shot_agent = init_agent(llm = llm,
                                 tools = tools,
                                 verbose=verbose
                                 )
    if print_logs:
        print("Done")
    
    #------------------------------------------------------------------------------------     
    # Generate Prompts
    #-----------------------------------------------------------------------------------
    
    prompt_style = 'financial_advisor'

    if print_logs:
        print("{} prompt style selected...".format(prompt_style))    
    
    prompt_template = load_prompt_template(prompt_style)

    if print_logs:
        print("Done")


    if print_logs:
        print("Formatting prompt...")   

    prompt = generate_prompt_obj(prompt_template, ["company"], input_stock_name)
    
    if print_logs:
        print("Done")   

    #-----------------------------------------------------------------------------------
    # Run prompt
    #-----------------------------------------------------------------------------------


    final_answer = generate_response(zero_shot_agent,   
                                     prompt=prompt)
    
    print(type(final_answer))

    attempt = 0
    
    final_answer = final_answer.replace('Could not parse LLM output: ', '')

    if final_answer.startswith("Question:") == False:
        return final_answer
    
    while True:
         attempt+=1
         print("Hmm, lets try that again... (attempt {} of 3)".format(attempt))

         if attempt <= 3:
            final_answer = generate_response(zero_shot_agent,
                                            prompt=prompt)
            if final_answer.startswith("Question") == False:
                return final_answer
            
         else:
            return "Sorry, I am tired right now, please try again later :sad:"
         
    # print(final_answer)



