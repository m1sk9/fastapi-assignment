import datetime
import uuid

from pydantic import BaseModel, Field

class Task(BaseModel):
    uid: uuid.UUID = Field(description="Task ID")
    name: str = Field(description="Task name")
    description: str = Field(description="Task description")
    created_at: datetime.datetime = Field(description="Task creation date")
    updated_at: datetime.datetime = Field(description="Task creation date")


class CreateTask(BaseModel):
    name: str = Field(description="Task name")
    description: str = Field(description="Task description")
