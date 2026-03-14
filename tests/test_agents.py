from deep_research_app.services.agents_service import setup_agents_and_tasks


def test_agents_creation():
    crew, researcher, search_tool = setup_agents_and_tasks(
        "Artificial Intelligence", breadth=1, depth=1
    )

    assert crew is not None
