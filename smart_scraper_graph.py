from scrapegraphai.graphs import SmartScraperGraph
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


# OPTION 2: PAID MODEL (GPT / GROQ / GEMINI)

paid_model_config = {
    "llm": {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "model": "openai/gpt-4o-mini"
    },
    "headless": True,
    "verbose": True
}

prompt = """
Extract destination travel data:
- Destination name
- Country / State
- Short description
- Top attractions
- Ideal budget range
- Best time to visit
"""

source_url = "https://www.tourism.rajasthan.gov.in/jaipur.html"

graph = SmartScraperGraph(
    prompt=prompt,
    source=source_url,
    config=ollama_config   # 🔁 switch to paid_model_config if needed
)

result = graph.run()


# Create output structure
output = {
    "result": result,
    "execution_info": graph.execution_info
}

# Save to JSON file
output_file = "smart_scraper_result.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2)

print(f"Output saved to {output_file}")

# Print execution info to console as well
print("\n" + prettify_exec_info(graph.execution_info))
