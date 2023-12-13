import datetime
import uuid

from fastapi import FastAPI, Depends

from src.schema import Task, CreateTask

app = FastAPI()

task_db: dict[uuid.UUID, Task] = {}


def get_task_dict() -> dict[uuid.UUID, Task]:
    return task_db


# タスクの一覧取得
@app.get("/tasks")
async def get_tasks(task_db: dict[uuid.UUID, Task] = Depends(get_task_dict),) -> list[Task]:
    result = list(task_db.values())

    return result


# タスクの作成
@app.post("/tasks", response_model=Task)
async def create_task(task: CreateTask, task_db: dict[uuid.UUID, Task] = Depends(get_task_dict),) -> Task:
    now: datetime.datetime = datetime.datetime.now()

    task_id: uuid.UUID = uuid.uuid4()
    created_at = now

    task = Task(uid=task_id, name=task.name, description=task.description, created_at=created_at)
    task_db[task_id] = task

    return task


# タスクの取得 (題名指定)
@app.get("/tasks/{task_name}")
async def get_task(task_name: str, task_db: dict[uuid.UUID, Task] = Depends(get_task_dict),) -> list[Task]:
    result: list[Task] = []
    all_tasks: list[Task] = list(task_db.values())

    for task in all_tasks:
        if task.name in task_name:
            result.append(task)

    return result


# タスクの更新 (修正)
# @app.put("/tasks/{task_id}")
# async def update_task():
#     pass


# タスクの削除
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: uuid.UUID, task_db: dict[uuid.UUID, Task] = Depends(get_task_dict),):
    task_db.pop(task_id)
