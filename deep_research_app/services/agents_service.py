from crewai import Crew, Agent, Task
from langchain_openai import ChatOpenAI
from crewai.tools import tool
import os
import requests
from pathlib import Path

extracted_links = []

# Task 1: Add dotenv import here
from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=True)


# Task 1: Add your OPENAI API key here

def _get_env_value(name: str) -> str:
    value = os.getenv(name, "")
    return value.strip().strip('"').strip("'")


OPENAI_API_KEY = _get_env_value("OPENAI_API_KEY")

# Task 2: Add your FIRECRAWL API Key  here

FIRECRAWL_KEY = _get_env_value("FIRECRAWL_KEY")


def _validate_api_keys() -> None:
    if not OPENAI_API_KEY or "your_openai_api_key" in OPENAI_API_KEY or OPENAI_API_KEY.startswith("<"):
        raise ValueError("OPENAI_API_KEY is missing or a placeholder in deep_research_app/.env. Add a valid OpenAI API key and retry.")

# Task 3: Add Firecrawl Search function here

@tool("FirecrawlSearch")
def firecrawl_search(query: str) -> str:
    """Search the web using Firecrawl API and return web results or an LLM fallback summary."""
    response = requests.get(
        f"https://api.firecrawl.dev/v1/search?query={query}",
        headers={"Authorization": f"Bearer {FIRECRAWL_KEY}"}
    )

    if response.status_code == 200:
        try:
            json_data = response.json()
            results = json_data.get("results", [])
            if results:
                for result in results:
                    url = result.get("url")
                    if url:
                        extracted_links.append(url)
                return response.text
        except Exception:
            pass

    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.3)
    fallback_response = llm.invoke(
        f"Please provide a clear explanation about: {query}. Include definition, features, and common use cases."
    )
    return fallback_response.content

# Task 5: Implement Researcher, Summarizer, and presenter Agents

def setup_agents_and_tasks(query, breadth, depth):
    _validate_api_keys()
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.3)

    researcher = Agent(
        name="Research Agent",
        role="Web searcher and data collector",
        goal="Conduct deep recursive web research",
        backstory="Expert in online information mining and query generation",
        tools=[firecrawl_search],
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    summarizer = Agent(
        name="Summarization Agent",
        role="Content summarizer",
        goal="Condense detailed findings into concise summaries",
        backstory="Skilled in summarizing complex texts for better understanding",
        tools=[],
        llm=llm,
        verbose=True,
        allow_delegation=True
    )

    presenter = Agent(
        name="Presentation Agent",
        role="Report formatter",
        goal="Create readable and well-structured reports",
        backstory="Experienced in generating polished documents for readers",
        tools=[],
        llm=llm,
        verbose=True,
        allow_delegation=True
    )

    task_research = Task(
        description=f"Perform deep research on: {query}.",
        expected_output="Raw web content, source links, and extracted notes",
        agent=researcher
    )

    task_summarize = Task(
        description="Summarize the research findings into structured points.",
        expected_output="Summarized bullets categorized by topic",
        agent=summarizer
    )

    task_present = Task(
        description="Format all summaries into a professional report.",
        expected_output="A final human-readable report",
        agent=presenter
    )

    crew = Crew(
        agents=[researcher, summarizer, presenter],
        tasks=[task_research, task_summarize, task_present],
        verbose=True,
        max_steps=20,
        max_time=300
    )

    return crew, researcher, firecrawl_search