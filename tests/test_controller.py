from deep_research_app.controllers.research_controller import run_research


def test_research_query():
    result = run_research("Artificial Intelligence")
    assert result is not None
