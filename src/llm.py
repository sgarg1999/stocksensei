
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent

from utils.loading_utilties import get_openai_token


temperature = 0.5
open_ai_token = get_openai_token
# verbose = True

def init_gpt(temperature = 0.5,
             open_ai_token= open_ai_token,
             verbose = True):

  open_ai_token = get_openai_token()

  llm = ChatOpenAI(temperature=temperature,
                verbose = verbose,
                  model_name = 'gpt-3.5-turbo',
                    openai_api_key=open_ai_token)

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
