import os
import requests
from requests.exceptions import RequestException


BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com/api-v2")
TOKEN = os.getenv("YOUGILE_TOKEN")


class YougileAPIError(Exception):
    pass


class ProjectsClient:
    def __init__(self):
        if not TOKEN:
            raise ValueError("YOUGILE_TOKEN is required")
        self.base_url = BASE_URL.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
        }

    def create_project(self, name: str, description: str | None = None):
        # Базовый URL уже содержит /api-v2, поэтому дальше просто /projects
        url = f"{self.base_url}/projects"
        payload = {"name": name}
        if description:
            payload["description"] = description
        try:
            resp = requests.post(
                url,
                json=payload,
                headers=self.headers,
                timeout=10,
            )
            if resp.status_code not in (200, 201):
                raise YougileAPIError(
                    f"Create project failed: {resp.status_code}, {resp.text}"
                )
            return resp.json()
        except RequestException as e:
            raise YougileAPIError(f"Request error: {e}") from e

    def get_project(self, project_id: str):
        url = f"{self.base_url}/projects/{project_id}"
        try:
            resp = requests.get(
                url,
                headers=self.headers,
                timeout=10,
            )
            if resp.status_code == 404:
                return None
            if resp.status_code != 200:
                raise YougileAPIError(
                    f"Get project failed: {resp.status_code}, {resp.text}"
                )
            return resp.json()
        except RequestException as e:
            raise YougileAPIError(f"Request error: {e}") from e

    def update_project(
        self,
        project_id: str,
        name: str | None = None,
        description: str | None = None,
    ):
        url = f"{self.base_url}/projects/{project_id}"
        payload = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description

        try:
            resp = requests.put(
                url,
                json=payload,
                headers=self.headers,
                timeout=10,
            )
            if resp.status_code not in (200, 204):
                raise YougileAPIError(
                    f"Update project failed: {resp.status_code}, {resp.text}"
                )
            return resp.json() if resp.content else None
        except RequestException as e:
            raise YougileAPIError(f"Request error: {e}") from e
