from scrapegraphai.graphs import SearchGraph
from scrapegraphai.utils import prettify_exec_info
import json
import os
from dotenv import load_dotenv

load_dotenv()


# OPTION 1: LOCAL MODEL (OLLAMA)

ollama_config = {
    "llm": {
        "model": "ollama/llama3.1",
        "model_tokens": 8192
    },
    "max_results": 5,
    "headless": True,
    "verbose": True
}


# OPTION 2: PAID MODEL

paid_model_config = {
    "llm": {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "model": "openai/gpt-4o-mini"
    },
    "max_results": 2,
    "headless": True,
    "verbose": True
}

from pydantic import BaseModel, Field
from typing import List

class Destination(BaseModel):
    name: str = Field(description="The name of the destination")
    location: str = Field(description="The location (state/country) of the destination")
    description: str = Field(description="A one-line description")
    highlights: str = Field(description="Travel highlights")

class Destinations(BaseModel):
    destinations: List[Destination]


# Create the Search Graph

graph = SearchGraph(
    prompt="List the best hill stations to visit in India",
    config=ollama_config,
    schema=Destinations
)

try:
    result = graph.run()
except Exception as e:
    print(f"Graph execution failed/incomplete: {e}")
    # Try to retrieve partial result/info if possible
    result = graph.final_state if hasattr(graph, 'final_state') else {"error": str(e)}

# Create output structure
output = {
    "result": result,
    "execution_info": graph.execution_info if hasattr(graph, 'execution_info') else []
}

# Save to JSON file
output_file = "search_graph_result.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2)

print(f"Output saved to {output_file}")

# Print execution info to console as well
print("\n" + prettify_exec_info(graph.execution_info))
