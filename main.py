import os

from src.cli.main_menu import MenuManager

MenuManager(
    app_name='PomodoroZ',
    app_icon=f'{os.getcwd()}/storage/images/pomodoroz_icon.png',
    storage_path=f'{os.getcwd()}/storage/'
)()
