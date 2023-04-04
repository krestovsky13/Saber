from fastapi import APIRouter
from starlette import status

from api.schemas import BuildSchema, TasksSchema
from api.services import collect_build_tasks

router = APIRouter(
    prefix='/task',
    tags=['task'],
)


@router.post("/get_tasks", response_model=TasksSchema, status_code=status.HTTP_200_OK)
async def get_tasks(schema: BuildSchema):
    return collect_build_tasks(schema.build)
