import json

from starlette import status
from starlette.testclient import TestClient


def test_get_tasks(client: TestClient):
    data = {"build": "forward_interest"}
    response = client.post("task/get_tasks", content=json.dumps(data))

    assert response.status_code == status.HTTP_200_OK


def test_get_tasks_404(client: TestClient):
    data404 = {"build": "write_beautiful"}
    response = client.post("task/get_tasks", content=json.dumps(data404))

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Build/Task with name write_beautiful does not exist."}


def test_get_tasks_424(client: TestClient):
    data404 = {"build": "front_arm"}
    response = client.post("task/get_tasks", content=json.dumps(data404))

    assert response.status_code == status.HTTP_424_FAILED_DEPENDENCY
    assert response.json() == {"detail": "Cyclic dependencies for tasks are broken."}
