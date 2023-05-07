# Stock Sensei

## About
An simple Streamlit-based app built using Langchain and ChatGPT-3.5-Turbo, through OpenAI's API.

Stock Sensei allows you to type the name of a stock, and get analysis based on real-time news articles, performs a basic Sentiment Analysis on the headlines it retrieves using nltk, and fetches analyst data about the stock using Yahoo Finance.

Ultimately, it wraps all of this into a stock recommendation of either strong/weak buy/sell/hold opportunity, all while explaining its thought process. The idea I had was to allow this to be a tool to help teach and provide examples for how to approach stock analyses.

## LLM Details

Uses ChatGPT 3.5 Turbo, with `temperature == 0.3`.

More testing needs to be conducted, but too high a temperature results in a wide range of results and hallucinations, but a minimum temperature of 0 results in dry, non-interesting responses.

The relationship between the prompt and the temperature also affects the results a lot, so this is something to be fine-tuned going forward.

## Tools 
The tools available to the model are as follows:

- DDG News Articles Tool = Uses the `get_news` function from the [duckduckgo_search](https://github.com/deedy5/duckduckgo_search) Python module. Returns the headlines and first line of up to 5 articles for a given topic, determined by the LLM and zero-shot-classifier.
- Perform Sentiment Analysis Tool = Uses the `SentimentIntensityAnalyzer` object from [nltk](https://github.com/nltk/nltk), and specifically the `SentimentIntensityAnalyzer.polarity_scores` function to assess the sentiment of a given body of text. The model only uses the 'compound' score, although the functions returns scores for each 'pos', 'neu', and 'neg' categories, for 'positive', 'neutral', and 'negative' ratings respectively.
- Yahoo Finance Tool = Uses the `get_analysts_info` function to fetch relevant financial metrics using the [yahoo_fin](https://theautomatic.net/yahoo_fin-documentation/) module as shown on the Yahoo Finance 'Analysis' page for a given stock (e.g. https://finance.yahoo.com/quote/NFLX/analysis?p=NFLX).


## Prompt

The prompt is the heart of what makes this possible.
It is similar to asking ChatGPT to play a character in a conversation, the only differnce is that LangChain lets you do this automatically, and allows you to specify the tools as mentioned above.

As of 7th May 2023, this is the prompt Stock Sensei is using:

  Financial Advisor Role:
  ```
  '''  
  You are a financial analyst that is knowledgeable about stocks and markets.
  You must research recent news for the company that the stock belongs to and comment on how this news will affect the stock price.
  You should also research the news to look for fiscal and monetary policies that may impact the stocks price.
  You will either be given the company name, or the ticker of the stock.
  You are explaining to finance students your rating of the stock. As such, you must be instructive, and reply as if you are teaching them.
  If you cannot find any information about the stock, you should mention this in your answer, but try your best.

  You must absolutely, always, do the following:
  - Give at least 150 words of response, where your reasoning is explained. 
  - Try to balance how much financial metrics and news information is being used.
  - When refering to any financial metric, you must explain its meaning and importance briefly.
  - Mention explicitly the articles and metrics you are using, and then provide your prediction on whether it is either a strong/weak buy, hold, or sell opportunity.
  - Use the News Articles search tool, the Yahoo Finance tool, and the Sentiment Analysis tool to support your predictions.

  Student: What is your analysis on {company}'s stock? Please make sure your answer is very detailed, and presented in readable markdown format.
  You:
  '''
  ```

Here, the prompt is essentially what would otherwise be code. Based on instructions, GPT is deciding how and what to carry out. Therefore, tuning the prompt is extremely important, but can also be very tricky due to the sheer number of variables that could affect outputs.


## Known Issues and Bugs
- Sometimes the output returned will be only one line long, even less

*Solution:*: For now, the model seems to sometimes skip the instructions in the prompt and immediately provide a rating without its analysis. Rerunning the model should help alleviate this, and produce more wholistic output.

- Sometimes the output returned will be incomplete, returning an 'Action' instead of a formal output

*Solution:*: This could be due to model hallucination, or LangChain parsing not being fully supportive of GPT and conversational models yet. Rerunning the model should help alleviate this.

- Sometimes the output returned will be in LaTEX font and misspaced

*Solution:*: WIP

## Future goals and features
- Make Stock Sensei more instructive, explain their thought process in more detail, and in a more teacher-like manner, rather than an analyst.
- Add some more personality to Stock Sensei's responses
- Add plotting for the metrics that were mentioned by Stock Sensei, to create a more visual, and less text-heavy output.
