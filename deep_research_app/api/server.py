from fastapi import FastAPI
from deep_research_app.controllers.research_controller import run_research

app = FastAPI()


@app.get("/research")
def research(query: str):

    result = run_research(query, breadth=2, depth=2)

    return {"result": result}