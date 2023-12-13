import datetime
import uuid

import pytest

from src.domain.model import Task


def test_task_make_and_create_normal() -> None:
    uid: uuid.UUID = uuid.uuid4()
    name: str = "testtesttesttesttesttesttesttesttest"
    description: str = "testtesttesttesttesttesttesttesttest"
    create_at: datetime.datetime = datetime.datetime.now()

    made_task: Task = Task.make(
        uid=uid,
        name=name,
        description=description,
        create_at=create_at
    )

    assert made_task.task_id.value == uid
    assert made_task.name.value == name
    assert made_task.description.value == description
    assert made_task.create_at.value == create_at

    created_task: Task = Task.create(
        name=name,
        description=description,
    )

    assert created_task.name.value == name
    assert created_task.description.value == description


def test_task_make_and_create_error() -> None:
    uid: uuid.UUID = uuid.uuid4()
    name: str = "test"
    description: str = "test"
    create_at: datetime.datetime = datetime.datetime.now()

    with pytest.raises(ValueError):
        Task.make(
            uid=uid,
            name=name,
            description=description,
            create_at=create_at
        )
