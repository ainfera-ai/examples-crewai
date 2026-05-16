"""CrewAI + Ainfera — researcher + writer crew, all calls auditable."""

import os

from crewai import LLM, Agent, Crew, Task

llm = LLM(
    model="openai/claude-opus-4-7",
    api_key=os.environ["AINFERA_API_KEY"],
    base_url="https://api.ainfera.ai/v1",
)

researcher = Agent(
    role="Researcher",
    goal="Find three short, surprising facts on a topic",
    backstory="You are a precise, fact-driven researcher who cites sources.",
    llm=llm,
)

writer = Agent(
    role="Writer",
    goal="Compress facts into a haiku",
    backstory="You write spare, evocative verse.",
    llm=llm,
)

research_task = Task(
    description="Find three short, surprising facts about Indonesian coffee.",
    agent=researcher,
    expected_output="Three bullet points.",
)

haiku_task = Task(
    description="Turn those three facts into a single haiku (5-7-5).",
    agent=writer,
    expected_output="A haiku.",
)

crew = Crew(agents=[researcher, writer], tasks=[research_task, haiku_task])
result = crew.kickoff()

print(result)
print("\nAudit chain: https://app.ainfera.ai (every call from this run is signed and hash-chained)")
