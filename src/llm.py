
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent

from utils.loading_utilties import get_openai_token

import openai
import os


# temperature = 0.5
# verbose = True

def init_gpt(temperature = 0.3,
             verbose = True):

  openai.api_key = os.environ["OPENAI_API_KEY"]

  llm = ChatOpenAI(temperature=temperature,
                verbose = verbose,
                  model_name = 'gpt-3.5-turbo')

  return llm




def init_agent(tools,
               llm,
               verbose = True,
               agent = "chat-zero-shot-react-description",
               ):

    zero_shot_agent = initialize_agent(
        agent = agent,
        tools = tools,
        llm = llm, 
        verbose = verbose

    )

    return zero_shot_agent
