import datetime
import uuid

from pydantic import Field

from src.domain.base import FrozenValueObjectModel


class TaskID(FrozenValueObjectModel):
    value: uuid.UUID = Field(description="タスクに紐付けられるID.")


class TaskName(FrozenValueObjectModel):
    value: str = Field(description="タスクの名前. 5文字以上である必要がある.", min_length=5)


class TaskDescription(FrozenValueObjectModel):
    value: str = Field(description="タスクの説明. 10文字以上である必要がある.", min_length=10)


class TaskCreateAt(FrozenValueObjectModel):
    value: datetime.datetime = Field(description="タスクの作成日時.")
