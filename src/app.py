from llm import init_gpt, init_agent
from tools import init_tools
from load_prompts import load_prompt_template, generate_prompt_obj
from pylatexenc.latex2text import LatexNodes2Text


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

    # Remove LaTex elements
    final_answer = LatexNodes2Text().latex_to_text(final_answer)



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
    satisfactory_answer = False
    
    while not satisfactory_answer:
        final_answer = generate_response(zero_shot_agent, prompt=prompt)
        final_answer = final_answer.replace('Could not parse LLM output: ', '')
    
        if final_answer.startswith("Question:") or len(final_answer.split(' ')) < 40:
            continue
        else:
            satisfactory_answer = True
            break
    
    return final_answer


