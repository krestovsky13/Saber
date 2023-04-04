from starlette.exceptions import HTTPException


def exceptions_handler(func):
    """
    Декоратор для перехвата исключений билдов и задач
    (Основные исключения рейзит pydantic)
    """
    def catch_exceptions(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as err:
            raise HTTPException(
                status_code=404,
                detail=f"Build/Task with name {err.args[0]} does not exist.",
            )
        except Exception:
            raise HTTPException(
                status_code=424,
                detail="Cyclic dependencies for tasks are broken.",
            )
    return catch_exceptions
