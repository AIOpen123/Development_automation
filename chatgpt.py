import os
import openai
import os
from openai import AzureOpenAI


os.environ['AZURE_OPENAI_ENDPOINT'] = 'https://kgsopenaipoc.openai.azure.com/'
os.environ['AZURE_OPENAI_API_KEY'] = '87ff18d54a6546639b6091961c2484af'
os.environ['OPENAI_API_BASE'] = 'azure'
os.environ['OPENAI_API_VERSION'] = '2023-03-15-preview'

openai.api_base = 'https://kgsopenaipoc.openai.azure.com/'
openai.api_key = '87ff18d54a6546639b6091961c2484af'
openai.api_type = 'azure'
openai.api_version = '2023-03-15-preview'

deployment_name = 'TestPoc'
gpt_model = 'gpt-35-turbo'
ada_model = "text-embedding-ada-002"

# print(os.getenv("AZURE_OPENAI_API_KEY"))

client = AzureOpenAI(
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version = '2023-03-15-preview',
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
)

def chat_completion(query):
    response = client.chat.completions.create(
        model="gpt-35-turbo",
        messages=[
            {"role": "user", "content": query}
        ]
    )
    response_chat = response.choices[0].message.content
    # print(response.choices[0].message.content)
    return response_chat


