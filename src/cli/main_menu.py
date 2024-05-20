import os
import re
import time
import questionary

from typing import Any
from pyfiglet import figlet_format

from src.libs.notification_manager import NotificationManager
from src.utils.progress_bar import progress_bar


class MainMenu:
    def __init__(
        self, app_name: str,
        app_icon: str,
        storage_path: str
    ) -> None:
        self.notifications = NotificationManager(
            app_name=app_name,
            app_icon=app_icon,
            storage_path=storage_path
        )

    def __call__(self, *args: Any, **kwds: Any) -> str:
        self.__start_icon()
        self.__main_menu_selector()

    def __start_icon(self) -> None:
        print(figlet_format(text="PomodoroZ"))
        print("⚡ Powered by: Lucas Amorim (Kakaroto)")
        print("📧 Email: lucas.ala1999@gmail.com")
        print("🐙 GitHub: https://github.com/lucaslima18")
        print("🔗 LinkedIn: https://www.linkedin.com/in/lucas-amorim-b09691173/")
        print("\n\n")

    def __main_menu_selector(self) -> str:
        main_menu_item = questionary.select(
            message="What you whant to do?",
            choices=["📃 Task List", "🍅 Start Pomodoro"]
        ).ask()

        if re.search("task list", main_menu_item, re.IGNORECASE):
            self.__task_list()
        self.__pomodoro_manager()

    def __task_list(self):
        questionary.select(
            "My tasks:",
            choices=["Test1", "Test2", "Previous menu"]
        ).ask()

    def __pomodoro_manager(self):
        ## fazer com que tenha um controle do pomodoro tipo, iniciar descanso e etc...
        os.system('cls' if os.name == 'nt' else 'clear')
        self.__start_icon()
        print("Pomodoro Name: Test")
        print("Pomodoro Description: Teste descricao")
        print("Total time: " "12h")
    
        progress_bar(total_seconds=30, state='pomodoro')
        self.notifications.send_notification(
            message="Time to take a well-deserved break. 🌟 Keep up the good work! 🚀",
            title="🍅 Pomodoro X completed successfully! 🎉",
            state="pomodoro_finished"
        )
        os.system('cls' if os.name == 'nt' else 'clear')
        self.__start_icon()
        questionary.confirm("⏳ Start break?").ask()
        os.system('cls' if os.name == 'nt' else 'clear')
        self.__start_icon()
        print("Pomodoro Name: Test")
        print("Pomodoro Description: Teste descricao")
        print("Total time: " "12h")
        progress_bar(total_seconds=30, state='break')
        self.notifications.send_notification(
            message="Time to get back to work! 💪 Start your next Pomodoro session now. ⏳",
            title="🍅 Break Over! Let's Begin Pomodoro X! 🔥",
            state="break_finished"
        )
        os.system('cls' if os.name == 'nt' else 'clear')
        self.__start_icon()
        questionary.confirm("⏳ Start new pomodoro?").ask()
