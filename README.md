# Deep Research Through an AI Agent Using OpenAI

This project is a Python research assistant that uses CrewAI agents, OpenAI models, and Firecrawl search to generate a research report and export it as PDF.

The repository currently includes:

- A Streamlit UI for entering a research topic and downloading the generated PDF
- A FastAPI endpoint for triggering research by query string
- A CrewAI-based multi-agent workflow
- Markdown cleanup utilities
- PDF report generation with source links
- Basic tests for controller and agent setup

## How It Works

1. The user submits a research query from the Streamlit app or the FastAPI endpoint.
2. The service builds several search variations from that query based on `breadth`.
3. Firecrawl search is used to collect web results.
4. If Firecrawl does not return usable data, the app falls back to an OpenAI model response.
5. CrewAI runs a three-agent workflow:
   - Research Agent
   - Summarization Agent
   - Presentation Agent
6. The final output is cleaned for display.
7. A PDF report is generated and returned to the UI.

## Project Structure

```text
deep_research_app/
├── api/
│   └── server.py
├── config/
│   └── agents.yaml
├── controllers/
│   └── research_controller.py
├── models/
│   ├── database.py
│   └── pdf_generator.py
├── services/
│   └── agents_service.py
├── utils/
│   ├── agent_loader.py
│   ├── logger.py
│   ├── markdown_cleaner.py
│   ├── monitoring.py
│   └── validation.py
├── .env_example
└── main.py
tests/
├── conftest.py
├── test_agents.py
└── test_controller.py
```

## Main Components

### Streamlit App

`deep_research_app/main.py` provides a small UI with:

- Research query input
- Breadth slider
- Depth slider
- Temperature slider in the UI
- Report preview
- PDF download
- Inline PDF preview

Note: the current controller does not consume the UI temperature value.

### Research Controller

`deep_research_app/controllers/research_controller.py` orchestrates the flow:

- Creates the crew and tools
- Runs the CrewAI workflow
- Cleans markdown output
- Builds the PDF
- Returns text output, PDF bytes, and a base64 PDF string

### Agent Service

`deep_research_app/services/agents_service.py`:

- Loads environment variables from `deep_research_app/.env`
- Validates `OPENAI_API_KEY`
- Defines the Firecrawl tool
- Falls back to `gpt-4o-mini` if Firecrawl search is not usable
- Runs parallel search queries with `ThreadPoolExecutor`
- Creates the CrewAI agents and tasks

### FastAPI Endpoint

`deep_research_app/api/server.py` exposes:

```http
GET /research?query=your-topic
```

This currently uses fixed values of `breadth=2` and `depth=2`.

## Requirements

- Python 3.10+
- OpenAI API key
- Firecrawl API key

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Environment Setup

Create `deep_research_app/.env`:

```env
OPENAI_API_KEY=your_openai_api_key
FIRECRAWL_KEY=your_firecrawl_api_key
```

The app reads environment values from `deep_research_app/.env`.

## Run the Streamlit App

From the repository root:

```bash
streamlit run deep_research_app/main.py
```

Then open the local Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Run the FastAPI App

From the repository root:

```bash
uvicorn deep_research_app.api.server:app --reload
```

Then open:

```text
http://127.0.0.1:8000/research?query=Artificial%20Intelligence
```

## Running Tests

Run:

```bash
pytest
```

Current tests are minimal and depend on the runtime setup of the application. In practice, successful execution may still require valid API keys because the test suite does not fully mock the external services.

## Screenshots

The repository includes Streamlit screenshots in [`images/`](/Users/nithineleti/Downloads/PROJECTS/Deep_Research_Through_an_AI_Agent_Using_OpenAI/images).

## Current Limitations

This README reflects the code as it exists today. A few things are present in the repository but are only partially integrated:

- `depth` is passed through the flow but is not meaningfully used in agent behavior
- The Streamlit temperature slider is not used by the backend
- `utils/validation.py` is defined but not applied to incoming queries
- `models/database.py` exists, but research history is not written during the main workflow
- `config/agents.yaml` is not used to build the active CrewAI agents
- Tests do not isolate all external dependencies

## Tech Stack

- Python
- Streamlit
- FastAPI
- CrewAI
- LangChain OpenAI
- OpenAI API
- Firecrawl API
- ReportLab
- pytest

## Updating the README on GitHub

I updated the local [`README.md`](/Users/nithineleti/Downloads/PROJECTS/Deep_Research_Through_an_AI_Agent_Using_OpenAI/README.md). To publish it to GitHub, run these commands from the repository root:

```bash
git status
git add README.md
git commit -m "Update README to match current project structure"
git push origin <your-branch>
```

If you are working directly on `main`, replace `<your-branch>` with `main`.
