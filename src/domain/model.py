import datetime
import uuid

from src.domain.base import EntityModel

from src.domain.field import (
    TaskID,
    TaskName,
    TaskDescription,
    TaskCreateAt,
)


class Task(EntityModel):
    task_id: TaskID

    name: TaskName
    description: TaskDescription

    create_at: TaskCreateAt

    @staticmethod
    def make(
        uid: uuid.UUID,
        name: str,
        description: str,
        create_at: datetime.datetime
    ) -> "Task":
        task_id: TaskID = TaskID(value=uid)

        task_name: TaskName = TaskName(value=name)
        task_description: TaskDescription = TaskDescription(value=description)

        task_create_at: TaskCreateAt = TaskCreateAt(value=create_at)

        result: Task = Task(
            task_id=task_id,
            name=task_name,
            description=task_description,
            create_at=task_create_at,
        )

        return result

    @staticmethod
    def create(
        name: str,
        description: str,
    ) -> "Task":
        task_id: uuid.UUID = uuid.uuid4()
        create_at: datetime.datetime = datetime.datetime.now()

        result: Task = Task.make(
            uid=task_id,
            name=name,
            description=description,
            create_at=create_at
        )

        return result
