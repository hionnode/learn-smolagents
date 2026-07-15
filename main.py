"""Minimal smolagents example: a CodeAgent that can search the web and do math."""

from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel

model = InferenceClientModel()  # reads HF_TOKEN from the environment
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

if __name__ == "__main__":
    result = agent.run("What is the current population of Japan, divided by 100?")
    print(result)
