import pytest
from api_client import ProjectsClient


@pytest.fixture(scope="session")
def projects_client():
    return ProjectsClient()


@pytest.fixture
def created_project(projects_client):
    name = "Test Project for Lesson 8"
    proj = projects_client.create_project(
        name,
        description="Automated test project",
    )
    project_id = proj["id"]
    yield {"id": project_id, "name": name, "data": proj}
