#!/usr/bin/env python

import os
import pathlib

from datetime import datetime
# from src.cli.menu_manager import MenuManager
from src.modules.task.repository import TaskRepository
from src.modules.task.models import Task

test = TaskRepository.create_task(
    task=Task(
        Name='sou só uma task de teste',
        Description='sou apenas uma descricao de task',
        time_for_pomodoro=1,
        project_id=1
    )
)

# MenuManager(
#     app_name="PomodoroZ",
#     app_icon=f"{str(pathlib.Path(__file__).parent.resolve()).replace('/src', '')}/storage/images/pomodoroz_icon.png",
#     storage_path=f"{str(pathlib.Path(__file__).parent.resolve()).replace('/src', '')}/storage/",
# ).run()
