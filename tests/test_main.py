import datetime
import uuid

from fastapi.testclient import TestClient

from src.main import get_task_dict, app
from src.schema import Task

client = TestClient(app)

mock_task_db: dict[uuid.UUID, Task] = {
    uuid.UUID("e4a8e8c5-4c7d-4a5f-9b8b-0c2c0a7b4c8f"): Task(
        uid=uuid.UUID("e4a8e8c5-4c7d-4a5f-9b8b-0c2c0a7b4c8f"),
        name="task1",
        description="description1",
        created_at=datetime.datetime(2021, 1, 1, 0, 0, 0),
        updated_at=datetime.datetime(2021, 1, 1, 0, 0, 0),
    ),
}


def get_mock_task_dict() -> dict[uuid.UUID, Task]:
    return mock_task_db


app.dependency_overrides[get_task_dict] = get_mock_task_dict


def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200

    expected: list[dict] = []
    for task in mock_task_db.values():
        serialized_task: str = task.model_dump_json()
        re_deserialized_task: dict = Task.model_validate_json(serialized_task).model_dump()

        expected.append(re_deserialized_task)

    assert response.json() == expected
