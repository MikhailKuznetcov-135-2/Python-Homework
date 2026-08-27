import pytest
from api_client import YougileAPIError


def test_create_project_positive(projects_client):
    name = "New Project Positive Test"
    result = projects_client.create_project(name)
    assert result is not None
    assert "id" in result
    assert result["name"] == name


def test_create_project_negative_empty_name(projects_client):
    with pytest.raises(YougileAPIError):
        projects_client.create_project("")


def test_get_project_positive(created_project, projects_client):
    project = projects_client.get_project(created_project["id"])
    assert project is not None
    assert project["id"] == created_project["id"]


def test_get_project_negative_not_found(projects_client):
    project = projects_client.get_project("nonexistent-id-12345")
    assert project is None


def test_update_project_positive(created_project, projects_client):
    new_name = "Updated Project Name"
    projects_client.update_project(created_project["id"], name=new_name)
    updated = projects_client.get_project(created_project["id"])
    assert updated is not None
    assert updated["name"] == new_name


def test_update_project_negative_nonexistent_id(projects_client):
    with pytest.raises(YougileAPIError):
        projects_client.update_project("invalid-id-999", name="Should fail")
