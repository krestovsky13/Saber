import os

from fastapi import FastAPI

from api.v1.routes import router
from api.utils import load_files


def start_application():
    """
    Инициализация приложения
    """
    _app = FastAPI()

    _app.include_router(router, prefix='/api/v1')

    return _app


app = start_application()


@app.on_event("startup")
def app_startup():
    """
    Подгрузка файлов .yaml из папки
    """
    load_files(os.path.abspath('builds'))
