# AI FINANCIAL ANALYST ASSISTANT APPLICATION

## 1. Project Overview
This project is a Python-based AI research assistant built with Streamlit and CrewAI orchestration. It accepts a user query, runs a multi-agent research workflow, cleans the generated markdown output, and produces a downloadable PDF report.

**Problem it solves**
- Reduces manual effort in collecting, summarizing, and presenting topic research.
- Packages findings into a readable report format for quick review.

**Target users**
- Analysts, researchers, and technical users who need rapid topic synthesis.
- Developers evaluating multi-agent LLM orchestration patterns.

## Application Screenshots

### Streamlit Frontend
![Frontend Screenshot 1](images/Screenshot%202026-02-28%20153744.png)
![Frontend Screenshot 2](images/Screenshot%202026-02-28%20153752.png)
![Frontend Screenshot 3](images/Screenshot%202026-02-28%20153757.png)
![Frontend Screenshot 4](images/Screenshot%202026-02-28%20153802.png)

## 2. Key Features
- Interactive Streamlit UI for query input and execution controls (breadth and depth sliders).
- Multi-agent workflow using CrewAI (`Research Agent`, `Summarization Agent`, `Presentation Agent`).
- Web search integration via Firecrawl API with LLM fallback when search results are unavailable.
- Markdown normalization pipeline before final presentation.
- PDF generation with optional source link listing and inline preview/download in UI.
- Environment-based API key loading with runtime validation and explicit invalid-key handling.

**Financial analytics capabilities (current state)**
- No domain-specific financial analytics engine is implemented in the current repository.
- The current implementation is a generic deep-research pipeline that can be applied to finance topics via prompt/query input.

**Security features (current implementation)**
- Secrets loaded from `.env` through `python-dotenv`.
- Placeholder/invalid OpenAI key detection before agent execution.
- No built-in auth layer, RBAC, or encrypted-at-rest persistence in current code.

## 3. System Architecture
### High-level architecture
The application follows a modular Python architecture:
- `main.py`: Streamlit presentation and interaction layer.
- `controllers/research_controller.py`: Orchestration entrypoint for end-to-end run.
- `services/agents_service.py`: CrewAI agent/task construction + external API access.
- `utils/markdown_cleaner.py`: Output normalization.
- `models/pdf_generator.py`: Report rendering to PDF.

### Architecture flow
1. User submits query and parameters in Streamlit UI.
2. Controller initializes CrewAI crew via service layer.
3. Research agent calls Firecrawl search tool.
4. If search fails or returns empty, fallback response is generated via OpenAI model.
5. Summarization and presentation agents finalize report text.
6. Markdown cleaner normalizes output.
7. PDF generator builds report file.
8. UI returns text preview + PDF download/preview.

### Why these technologies were chosen
- **Streamlit**: fast delivery of data/AI interface without custom frontend stack.
- **CrewAI**: explicit multi-agent task decomposition and orchestration.
- **LangChain OpenAI client**: straightforward model invocation and configuration.
- **ReportLab**: deterministic PDF generation from structured text.
- **dotenv-based config**: simple secret management for local development.

## 4. Tech Stack
- **Frontend/UI**: Streamlit
- **Backend/Application**: Python 3.10, modular controller/service/model/util layers
- **AI/LLM Orchestration**: CrewAI, LangChain OpenAI integration, OpenAI API
- **External Data Source**: Firecrawl Search API
- **Document Generation**: ReportLab
- **Configuration**: `python-dotenv`, `.env` / `.env_example`
- **Dependency Management**: `requirements.txt` (pinned environment export)
- **Cloud/Infra**: Not implemented in repository
- **Database**: Not implemented in repository
- **DevOps/CI/CD**: Not implemented in repository

## 5. AI & Financial Intelligence Engine
### AI usage in this codebase
- Multi-agent pipeline where each agent has a distinct responsibility:
  - Research collection
  - Summarization
  - Final presentation formatting
- OpenAI chat model instantiated through `ChatOpenAI`.
- Crew executes sequential tasks through `crew.kickoff()`.

### Data processing pipeline
- Input query -> Firecrawl search call -> result extraction (`url` capture) -> optional LLM fallback -> aggregated output -> markdown cleanup -> PDF rendering.

### RAG / embeddings / vector search status
- No RAG pipeline implemented.
- No embeddings generation implemented.
- No vector database usage in application code.

## 6. API Design
### Core endpoints summary
- No REST/GraphQL API routes are implemented in this repository.
- Primary interface is Streamlit page interactions.

### Authentication method
- External API authentication via bearer keys (`OPENAI_API_KEY`, `FIRECRAWL_KEY`) loaded from environment.

### Request/response structure overview
- Internal request object is function-based (`query`, `breadth`, `depth`).
- Internal response returns tuple: cleaned text, raw PDF bytes, base64 PDF for inline rendering.

## 7. Database Design
- No database layer exists in the current repository.
- No schema definitions, migrations, or ORM models are implemented.
- Runtime state is in-memory + temporary PDF files.

## 8. Security Implementation
- Environment-based secret loading with explicit path resolution to `.env`.
- Runtime guard rejects placeholder/missing OpenAI key before model calls.
- Controller translates invalid OpenAI key errors into actionable messages.

**Not currently implemented**
- User authentication/authorization
- RBAC
- Audit logging
- Encryption at rest / key vault integration

## 9. Scalability & Performance Considerations
### Implemented
- Separation of UI, orchestration, utility, and document generation concerns for maintainability.
- Bounded Crew execution settings (`max_steps`, `max_time`).

### Not yet implemented
- Caching strategy
- Background job queue
- Async task workers
- Horizontal scaling setup
- Containerization artifacts
- Cloud deployment manifests

## 10. Local Development Setup
### Prerequisites
- Python 3.10+
- OpenAI API key
- Firecrawl API key

### Installation
```bash
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

### Environment variables
Create `deep_research_app/.env` with:
```env
OPENAI_API_KEY="<your_openai_api_key>"
FIRECRAWL_KEY="<your_firecrawl_api_key>"
```

### Run application
```bash
cd deep_research_app
streamlit run main.py
```

### Docker setup
- No Dockerfile or docker-compose configuration is present in this repository.

## 11. Deployment Guide
### Production setup overview
- A production deployment pipeline is not defined in this repository.
- Current project is configured for local execution.

### Environment configuration
- Provide runtime secrets via environment variables or `.env`.
- Ensure OpenAI and Firecrawl keys are valid and scoped appropriately.

### CI/CD
- No CI/CD workflows are present.

## 12. Testing Strategy
- No test suite (`unit`, `integration`, or `e2e`) is currently included.
- No coverage configuration is present.

Recommended next step:
- Add `pytest` with tests for controller flow, markdown cleaning, and PDF generation.

## 13. Future Improvements
- Add financial-domain toolset (market data providers, KPI calculators, valuation templates).
- Introduce structured API layer (FastAPI) for service-to-service integration.
- Implement persistent storage for runs, reports, and source provenance.
- Add authentication and role-based access controls.
- Add caching, async workers, and queue-based execution for long research jobs.
- Add Docker + CI/CD pipeline for repeatable build and deployment.
- Add automated test suite with coverage thresholds.

## 14. Author
Built as a modular AI orchestration project demonstrating practical skills in:
- LLM agent workflow design (CrewAI)
- Third-party API integration and fallback design
- Streamlit application development
- Output post-processing and PDF reporting
- Environment and runtime error handling for reliable local execution
