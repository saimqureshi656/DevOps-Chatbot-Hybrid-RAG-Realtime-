import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()
client= TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def tavily_web_search(query):
    response = client.search(query=query, search_depth="advanced")
    return "\n\n".join([r['content'] for r in response['results']])