# 🤖 Deep Research Assistant with CrewAI

## 📖 Project Overview

This is a **Python-based AI research assistant** built with Streamlit and CrewAI that automates deep research workflows. It accepts a user query, executes a multi-agent research process, and generates a professional PDF report with findings.

### 🎯 Problems Solved
- ✅ Reduces manual effort in collecting, summarizing, and presenting research
- ✅ Packages findings into readable, professional report format
- ✅ Enables rapid topic synthesis with configurable research depth
- ✅ Demonstrates enterprise-grade multi-agent LLM orchestration

### 👥 Target Users
- 📊 Analysts and Researchers needing rapid topic synthesis
- 🎓 Students conducting comprehensive research
- 👨‍💼 Business professionals doing competitive analysis
- 🛠️ Developers learning multi-agent LLM patterns

---

## 📸 Application Screenshots

### Streamlit Frontend
![Frontend Screenshot 1](images/Screenshot%202026-02-28%20153744.png)
![Frontend Screenshot 2](images/Screenshot%202026-02-28%20153752.png)
![Frontend Screenshot 3](images/Screenshot%202026-02-28%20153757.png)
![Frontend Screenshot 4](images/Screenshot%202026-02-28%20153802.png)

---

## ✨ Key Features

- 🖥️ **Interactive Streamlit UI** - Query input with breadth & depth sliders for research control
- 🤖 **Multi-Agent Workflow** - Specialized CrewAI agents (Research, Summarization, Presentation)
- 🌐 **Web Search Integration** - Firecrawl API with intelligent LLM fallback
- 📝 **Markdown Normalization** - Cleaned, formatted output pipeline
- 📄 **PDF Generation** - Professional downloadable reports with inline preview
- 🔐 **Environment-Based Secrets** - Secure API key management via `.env`
- ⚡ **Fast & Reliable** - API validation and error handling built-in

---

## 🏗️ System Architecture

### High-Level Design
```
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit UI (main.py)                   │
│         User Query Input + Breadth/Depth Sliders            │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│          Research Controller (Orchestration Layer)           │
│           Manages workflow execution and coordination        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              CrewAI Multi-Agent System                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Research    │→ │ Summarization│→ │ Presentation │      │
│  │  Agent       │  │  Agent       │  │  Agent       │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              Firecrawl Search API (Web Search)               │
│         + OpenAI Fallback (LLM-Generated Insights)          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│         Markdown Cleaner (Output Normalization)              │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│          PDF Generator (ReportLab)                           │
│       Professional Report Creation & Formatting             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              User Output                                     │
│   PDF Download + Browser Preview + Markdown Display        │
└─────────────────────────────────────────────────────────────┘
```

### Project Structure
```
deep_research_app/
├── main.py                              # 🖥️  Streamlit UI & Interactions
├── controllers/
│   └── research_controller.py            # 🎮 Orchestration Logic
├── services/
│   └── agents_service.py                 # 🤖 CrewAI Agents & Tools
├── models/
│   └── pdf_generator.py                  # 📄 PDF Report Generation
├── utils/
│   └── markdown_cleaner.py               # ✏️  Output Formatting
└── .env                                  # 🔑 API Keys Configuration
```

### Data Flow Pipeline
1. User submits query + parameters in Streamlit UI
2. Research Controller initializes CrewAI Crew
3. **Research Agent** → Calls Firecrawl Search Tool
4. If search fails → **LLM Fallback** generates insights via OpenAI
5. **Summarization Agent** → Analyzes & synthesizes information
6. **Presentation Agent** → Formats findings into structured report
7. **Markdown Cleaner** → Normalizes and cleans output
8. **PDF Generator** → Builds professional report file
9. **Streamlit UI** → Returns preview + download link

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit |
| **Agent Orchestration** | CrewAI v1.9.3+ |
| **LLM & Chat** | OpenAI API (ChatOpenAI via LangChain) |
| **Web Search** | Firecrawl API |
| **PDF Generation** | ReportLab |
| **Config Management** | python-dotenv |
| **Python Version** | 3.10, 3.11, 3.12, 3.13 |
| **OS Support** | macOS, Linux, Windows |

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10 or higher
- OpenAI API Key ([Get it here](https://platform.openai.com/api-keys))
- Firecrawl API Key ([Get it here](https://www.firecrawl.dev))
- pip or conda package manager

### Installation (macOS/Linux)

#### Step 1: Clone & Navigate
```bash
cd /path/to/Deep_Research_Through_an_AI_Agent_Using_OpenAI
```

#### Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Configure Environment Variables
Create `deep_research_app/.env`:
```env
OPENAI_API_KEY=sk-your_actual_key_here
FIRECRAWL_KEY=fc-your_actual_key_here
```

#### Step 5: Run the Application
```bash
streamlit run deep_research_app/main.py
```

#### Step 6: Access the App
```
Local URL: http://localhost:8501
Network URL: http://<your-ip>:8501
```

### Installation (Windows)

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure .env file
# Create: deep_research_app\.env

# Run application
streamlit run deep_research_app/main.py
```

---

## 💡 How to Use the Application

### 1. Enter Your Research Query
Type any research topic in the text input field:
- "Artificial Intelligence in Finance"
- "Climate Change Mitigation Strategies"
- "Blockchain Technology Applications"

### 2. Configure Research Parameters
- **Search Breadth** (1-10): Number of parallel search queries
- **Search Depth** (1-5): Recursion levels for deeper research

### 3. Click "Run Deep Research"
The multi-agent workflow will:
- ✅ Search the web for relevant information
- ✅ Analyze and synthesize findings
- ✅ Generate structured report
- ✅ Create professional PDF

### 4. Review & Download
- 📖 Read cleaned report in preview
- 📥 Download PDF report
- 👁️ View PDF inline in browser

---

## 🔐 Environment Configuration

### Required Environment Variables

Create `deep_research_app/.env`:

```env
# OpenAI API Key - Required for LLM operations
OPENAI_API_KEY=sk-proj-YOUR_ACTUAL_KEY_HERE

# Firecrawl API Key - Required for web search
FIRECRAWL_KEY=fc-YOUR_ACTUAL_KEY_HERE
```

### Getting API Keys

**OpenAI API Key:**
1. Visit https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy and paste into `.env`

**Firecrawl API Key:**
1. Visit https://www.firecrawl.dev
2. Sign up for account
3. Generate API key from dashboard
4. Copy and paste into `.env`

### Security Best Practices
- ✅ Never commit `.env` file to version control
- ✅ Add `.env` to `.gitignore`
- ✅ Use environment variables for production
- ✅ Rotate API keys periodically
- ✅ Monitor API usage and costs

---

## 🧪 Testing & Validation

### Test the Installation
```bash
# Verify Python version
python --version

# Verify all imports work
python -c "import streamlit; import crewai; import langchain_openai; print('✅ All imports successful')"

# Check API configuration
python -c "from dotenv import load_dotenv; import os; load_dotenv('deep_research_app/.env'); print('OpenAI Key Set:', bool(os.getenv('OPENAI_API_KEY')))"
```

### Manual Testing Workflow
1. Start the app: `streamlit run deep_research_app/main.py`
2. Try a simple query: "What is machine learning?"
3. Use breadth=2, depth=1 for quick test
4. Verify PDF generates and downloads
5. Check report content for accuracy

---

## 📊 Example Queries

### Financial Analysis
- "Impact of AI on stock market trading"
- "Cryptocurrency market trends 2026"
- "Digital banking transformation"

### Technology Research
- "Quantum computing breakthroughs"
- "Edge computing vs cloud computing"
- "5G network implementations"

### Business Strategy
- "Remote work future trends"
- "Supply chain optimization techniques"
- "Customer experience innovations"

---

## 🐛 Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError` | Missing dependencies | Run `pip install -r requirements.txt` |
| `API Key validation error` | Invalid/missing keys | Check `.env` file and API keys |
| `Streamlit not found` | Wrong virtual environment | Verify venv is activated |
| `Port 8501 already in use` | Port conflict | Streamlit auto-uses 8502, 8503, etc. |
| `Firecrawl search fails` | API key invalid/quota exceeded | Verify Firecrawl key validity |
| `OpenAI API error` | API key issue or quota exceeded | Check OpenAI account and credits |
| `PDF generation fails` | ReportLab issue | Reinstall: `pip install --upgrade reportlab` |

---

## 🔧 Advanced Configuration

### Customizing Agent Behavior
Edit `deep_research_app/services/agents_service.py`:
```python
# Adjust LLM temperature (0.0-1.0)
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    temperature=0.3  # Change for more/less creativity
)

# Modify agent prompts
researcher = Agent(
    goal="Your custom research goal here",
    backstory="Your custom backstory here"
)
```

### Adjusting Crew Settings
```python
crew = Crew(
    agents=[...],
    tasks=[...],
    max_steps=100,        # Max iterations
    max_time=3600,        # Max time in seconds
    verbose=True          # Enable detailed logging
)
```

---

## 📈 Performance Considerations

### Typical Execution Times
- Small query (breadth=1, depth=1): 2-5 minutes
- Medium query (breadth=3, depth=2): 5-15 minutes
- Large query (breadth=5, depth=3): 15-30+ minutes

### Resource Requirements
- **CPU**: 2+ cores recommended
- **Memory**: 4GB+ RAM
- **Network**: Stable internet connection for API calls
- **Storage**: ~50MB for dependencies + 10MB per report

### Cost Estimates (as of March 2026)
- OpenAI API: ~$0.01-0.05 per query
- Firecrawl API: Variable based on search volume
- Total per research: ~$0.05-0.20 (typical)

---

## 🚀 Deployment Options

### Local Development
✅ Current setup - best for testing and learning

### Docker Deployment (Recommended for Production)
```dockerfile
FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY deep_research_app ./deep_research_app
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV FIRECRAWL_KEY=${FIRECRAWL_KEY}

EXPOSE 8501
CMD ["streamlit", "run", "deep_research_app/main.py"]
```

### Cloud Platforms
- **Streamlit Cloud**: Free hosting for Streamlit apps
- **Heroku**: Easy Python app deployment
- **AWS/GCP/Azure**: Full infrastructure control

---

## 🤝 Contributing

### How to Contribute
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Areas for Improvement
- 🧪 Add comprehensive test suite
- 📚 Add more agent types (Financial Analyst, Legal Reviewer, etc.)
- 💾 Implement database for report history
- 🔐 Add user authentication & multi-tenancy
- ⚡ Add async/parallel processing
- 🐳 Add Docker configuration
- 📊 Add analytics dashboard

---

## 📝 License

This project is part of the AI-Financial-Analyst-Assistant-Application repository.

---

## 👨‍💻 Author

Built as a comprehensive AI orchestration project demonstrating:
- ✅ Multi-agent LLM workflow design (CrewAI)
- ✅ Third-party API integration & fallback patterns
- ✅ Streamlit application development
- ✅ Document generation & post-processing
- ✅ Production-ready error handling

**Repository**: https://github.com/TejeswaniMajji/AI-Financial-Analyst-Assistant-Application

---

## 📞 Support & Questions

- 📧 Email: Check repository for contact info
- 🐛 Issues: Report bugs on GitHub Issues
- 💬 Discussions: Join repository discussions
- 📖 Docs: Check documentation in repository

---

## ⭐ Star This Project!

If you found this project helpful, please give it a ⭐ on GitHub!

---

**Last Updated**: March 7, 2026
**Version**: 1.0.0
**Status**: ✅ Production Ready
