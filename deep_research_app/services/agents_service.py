from crewai import Crew, Agent, Task
from langchain_openai import ChatOpenAI
from crewai.tools import tool
import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

# Store extracted links
extracted_links = []

# Load environment variables
ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=True)


def _get_env_value(name: str) -> str:
    value = os.getenv(name, "")
    return value.strip().strip('"').strip("'")


OPENAI_API_KEY = _get_env_value("OPENAI_API_KEY")
FIRECRAWL_KEY = _get_env_value("FIRECRAWL_KEY")


def _validate_api_keys():
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY missing in .env")


# ---------------------------------------------------
# Firecrawl Search Tool
# ---------------------------------------------------

@tool("FirecrawlSearch")
def firecrawl_search(query: str) -> str:
    """Search the web using Firecrawl API."""

    response = requests.get(
        f"https://api.firecrawl.dev/v1/search?query={query}",
        headers={"Authorization": f"Bearer {FIRECRAWL_KEY}"},
    )

    if response.status_code == 200:
        try:
            json_data = response.json()
            results = json_data.get("results", [])

            formatted_results = []

            for result in results:
                title = result.get("title", "")
                url = result.get("url", "")
                snippet = result.get("snippet", "")

                if url:
                    extracted_links.append(url)

                formatted_results.append(
                    f"Title: {title}\nURL: {url}\nSnippet: {snippet}"
                )

            return "\n\n".join(formatted_results)

        except Exception:
            pass

    # fallback if Firecrawl fails
    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model="gpt-4o-mini",
        temperature=0.3
    )

    fallback = llm.invoke(
        f"Explain the topic clearly: {query}. Include definition, key points and applications."
    )

    return fallback.content


# ---------------------------------------------------
# Parallel Search
# ---------------------------------------------------

def run_parallel_search(queries):

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(lambda q: firecrawl_search.run(q), queries))

    return results


# ---------------------------------------------------
# Setup CrewAI Agents + Tasks
# ---------------------------------------------------

def setup_agents_and_tasks(query, breadth, depth):

    _validate_api_keys()

    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model="gpt-4o-mini",
        temperature=0.3
    )

    queries = [
        f"{query} overview",
        f"{query} latest research",
        f"{query} statistics",
        f"{query} trends",
        f"{query} future predictions",
    ][:breadth]

    parallel_results = run_parallel_search(queries)

    combined_results = "\n\n".join(parallel_results)

    # Research Agent
    researcher = Agent(
        name="Research Agent",
        role="Web Research Specialist",
        goal="Collect detailed information from web sources",
        backstory="Expert in extracting valuable insights from online content.",
        tools=[firecrawl_search],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    # Summarizer Agent
    summarizer = Agent(
        name="Summarization Agent",
        role="Content Summarizer",
        goal="Condense large research data into concise summaries",
        backstory="Expert at turning complex information into clear insights.",
        llm=llm,
        verbose=True,
    )

    # Presenter Agent
    presenter = Agent(
        name="Presentation Agent",
        role="Report Formatter",
        goal="Create professional research reports",
        backstory="Expert in structuring reports for readability.",
        llm=llm,
        verbose=True,
    )

    # Tasks
    task_research = Task(
        description=f"""
        Conduct deep research on the topic: {query}

        Use the following web results:
        {combined_results}

        Extract key insights, statistics, and important findings.
        """,
        expected_output="Detailed research notes with insights and sources.",
        agent=researcher,
    )

    task_summarize = Task(
        description="Summarize the research findings into structured bullet points.",
        expected_output="Structured summarized insights.",
        agent=summarizer,
    )

    task_present = Task(
        description="Convert the summarized insights into a professional report.",
        expected_output="Final research report.",
        agent=presenter,
    )

    crew = Crew(
        agents=[researcher, summarizer, presenter],
        tasks=[task_research, task_summarize, task_present],
        verbose=True,
    )

    return crew, researcher, firecrawl_search