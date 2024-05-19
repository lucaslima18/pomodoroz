import re,os
import time, datetime
import questionary

from typing import Any
from pyfiglet import figlet_format
from pygame import mixer

from src.utils.sound_notification import sound_notification
from src.libs.notification_manager import NotificationManager


class MainMenu:
    def __init__(self, app_name, app_icon) -> None:
        self.notifications = NotificationManager(
            app_name=app_name, app_icon=app_icon
        )
        pass

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
        questionary.select("My tasks:", choices=["Test1", "Test2", "Previous menu"]).ask()

    def __pomodoro_manager(self):
        ## fazer com que tenha um controle do pomodoro tipo, iniciar descanso e etc...
        print("Pomodoro Name: Test")
        print("Pomodoro Description: Teste descricao")
        print("Total time: " "12h")
        
        total_seconds = 0 * 3600 + 0 * 60 + 1
        
        self.progress_bar(total_seconds)
        self.notifications.send_notification(
            message= "Time to take a well-deserved break. 🌟 Keep up the good work! 🚀",
            title="🍅 Pomodoro X completed successfully! 🎉"
        )
        sound_notification("/home/kakaroto/www/personal_projects/pomodoroz/storage/mp3/pomodoro_finished.mp3")
        os.system('cls' if os.name == 'nt' else 'clear')
        self.__start_icon()
        questionary.confirm("⏳ Start break?").ask()
        self.progress_bar(5)
        self.notifications.send_notification(
            message="Time to get back to work! 💪 Start your next Pomodoro session now. ⏳",
            title="🍅 Break Over! Let's Begin Pomodoro X! 🔥"
        )
        sound_notification("/home/kakaroto/www/personal_projects/pomodoroz/storage/mp3/break_finished.mp3")
        questionary.confirm("⏳ Start new pomodoro?").ask()
        
    def progress_bar(self, total_seconds):
        bar_length = 20
        start_time = time.time()
        end_time = start_time + total_seconds

        while time.time() < end_time:
            elapsed_time = time.time() - start_time
            remaining_time = total_seconds - elapsed_time
            fraction = elapsed_time / total_seconds

            bar = int(fraction * bar_length + 1) * '█'
            padding = int(bar_length - len(bar)) * '░'

            ending = '\r' if remaining_time > 0 else '\n'
            minutes, seconds = divmod(int(remaining_time), 60)
            time_display = f"{minutes:02}:{seconds:02}"

            print(f'Pomodoro: [{bar}{padding}] {int(fraction*100)}% Time Left: {time_display}', end=ending)
            time.sleep(.02)
 
