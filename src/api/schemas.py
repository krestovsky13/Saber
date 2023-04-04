from pydantic import BaseModel, Extra


class BuildSchema(BaseModel):
    """
    Схема запроса задач
    """
    build: str

    class Config:
        extra = Extra.forbid


class TasksSchema(BaseModel):
    """
    Схема ответа задач
    """
    tasks: list[str]
    count: int
