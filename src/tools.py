from langchain.agents import Tool
from yahoo_fin.stock_info import get_analysts_info

from duckduckgo_search import ddg_news

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


#--------------------------------------------------
# Raw Python Functions
#--------------------------------------------------
def get_sentiment(input = ""):


  sia = SentimentIntensityAnalyzer()
  results = sia.polarity_scores(input)
  return results.get('compound')


def fetch_nltk_packages():
  nltk.download(["vader_lexicon",])


def yfin_search(input = ""):

  return get_analysts_info(input)


def get_news(inputs):
  parsed_news = ddg_news(inputs, safesearch = "Off", time = 'w', max_results = 10)

  articles = ''

  for i in parsed_news:
      # title = i.get('title') 
      body =  i.get('body')

      # combined_string = title + '\n' + body

      combined_string = body


      # print(combined_string)
      if body is not None:
        articles += combined_string + ' '

      else :
        continue
      # print(articles)
  
  return articles.strip()

def process_thought(thought):
    return thought


#--------------------------------------------------
# Langchain Tools
#--------------------------------------------------

def init_tools(
      ddg_news_article_search_tool = True,
        sentiment_analysis_tool = True,
        yfin_search_tool = True,
               ):
    
    tools = []

    ddg_news_article_search_tool = Tool(
    name = 'DDG News Articles Tool',
    func = get_news,
    description = '''Input a subject that you would like to search for using a search engine. Sentiment analysis can be performed on the output. E.g. <stock name> stock news''')
    

    sentiment_analysis_tool = Tool(
    name = 'Perform Sentiment Analysis Tool',
    func = get_sentiment,
    description = "Input a text to get a score between -1 and 1 indicating the sentiment of the text, 1 being very positive, and -1 being very negative. Very good to use on news articles to get a better sense of what is going on."
)

    yfin_search_tool = Tool(
    name = "Yahoo Finance Tool",
    func = yfin_search,
    description = '''Provides useful financial metrics used by professional trading analysts. 
    Input should be the ticker symbol of the company you would like to search. 
    This should be your go to function for looking up company financial metrics."
    '''
)
    
    thought_processing_tool = Tool(
       name = "Thought Processing",
       description= '''
       This is useful for when you have a thought that you want to use in a task,
        but you want to make sure it's formatted correctly. Input is your thought and self-critique and output is the processed thought.",
         ''',
         func = process_thought
    )
        

    if  ddg_news_article_search_tool:
        tools.append(ddg_news_article_search_tool)   
    if  sentiment_analysis_tool:
        tools.append(sentiment_analysis_tool)   
    if  yfin_search_tool:
        tools.append(yfin_search_tool)

    # tools.append(thought_processing_tool)

    return tools

