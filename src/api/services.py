from collections import OrderedDict

from api.exceptions import exceptions_handler
from api.utils import (
    TASKS,
    BUILDS,
    TASK_INDEXES,
    BUILD_INDEXES,
)


def sort_task_deps(deps_task: str) -> list:
    """
    Рекурсивная сортировка иерархии зависимостей для одной задачи
    """
    sort_tasks = []
    if deps := TASKS['tasks'][TASK_INDEXES[deps_task]]['dependencies']:
        for task in deps:
            sort_tasks.extend(sort_task_deps(task))
    sort_tasks.append(deps_task)

    return sort_tasks


@exceptions_handler
def collect_build_tasks(build: str) -> dict:
    """
    Соединение всех (уникальных, с сохранением иерархии) задач сборки
    """
    all_tasks_deps = []
    if tasks_build := BUILDS['builds'][BUILD_INDEXES[build]]['tasks']:
        for task in tasks_build:
            all_tasks_deps.extend(sort_task_deps(task))

    list_tasks = list(OrderedDict.fromkeys(all_tasks_deps))
    result = dict(tasks=list_tasks, count=len(list_tasks))

    return result
