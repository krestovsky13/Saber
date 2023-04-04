import os

import yaml

BUILD_INDEXES = {}
TASK_INDEXES = {}
BUILDS = {}
TASKS = {}


def load_files(path: str):
    """
    Загружаем файлы и сохраняем в глобальной зоне видимости
    """
    try:
        print(os.path.abspath('builds.yaml'))
        with open(os.path.join(path, 'builds.yaml')) as builds_file:
            BUILDS['builds'] = yaml.load(builds_file, Loader=yaml.FullLoader)['builds']
        with open(os.path.join(path, 'tasks.yaml')) as tasks_file:
            TASKS['tasks'] = yaml.load(tasks_file, Loader=yaml.FullLoader)['tasks']
    except yaml.YAMLError as exception:
        raise exception
    else:
        # словари с индексами для быстрого доступа
        for i, j in enumerate(BUILDS['builds']):
            BUILD_INDEXES[j['name']] = i
        for i, j in enumerate(TASKS['tasks']):
            TASK_INDEXES[j['name']] = i
