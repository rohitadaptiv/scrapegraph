from scrapegraphai.graphs import SmartScraperMultiGraph
from scrapegraphai.utils import prettify_exec_info
import json
import os
from dotenv import load_dotenv

load_dotenv()


# OPTION 1: LOCAL MODEL (OLLAMA)

ollama_config = {
    "llm": {
        "model": "ollama/llama3.1",
        "model_tokens": 8192,
        "base_url": os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    },
    "headless": True,
    "verbose": True
}


# OPTION 2: PAID MODEL

paid_model_config = {
    "llm": {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "model": "openai/gpt-4o-mini"
    },
    "headless": True,
    "verbose": True
}

prompt = """
Extract structured destination data:
- Name
- Country / State
- Description
- Top attractions
- Best time to visit
- Budget category
"""

sources = [
    "https://www.tourism.rajasthan.gov.in/jaipur.html",
    "https://chokhidhani.com/tourist-places-in-jaipur/?gad_source=1&gad_campaignid=23196308879&gbraid=0AAAAADluP-89THjmczrV0Vv0dlQyqvxkj&gclid=CjwKCAiAjc7KBhBvEiwAE2BDOfhX4yBluoRMPic9thBmY16J4zcAf86T7KbupvEbhx_uycXDWKLG1hoCnDcQAvD_BwE",
    "https://en.wikipedia.org/wiki/List_of_tourist_attractions_in_Jaipur"
]

graph = SmartScraperMultiGraph(
    prompt=prompt,
    source=sources,
    config=ollama_config   #  change to paid_model_config if needed
)

result = graph.run()

# Create output structure
output = {
    "result": result,
    "execution_info": graph.execution_info
}

# Save to JSON file
output_file = "smart_scraper_multi_result.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2)

print(f"Output saved to {output_file}")

# Print execution info to console as well
print("\n" + prettify_exec_info(graph.execution_info))
