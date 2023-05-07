import os

# def get_openai_token():

#     with open('../keys/openai_key_.txt', 'r') as f:
#         openai_key = f.read()

#     return openai_key



def get_openai_token():

    openai_key = os.environ.get("OPENAI_API_KEY")

    return openai_key