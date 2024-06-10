import os
import questionary
import random

from typing import List, Any
from pyfiglet import figlet_format

from utils.text_to_bold import text_to_bold
from utils.pagination import paginated_menu
from libs.notification_manager import NotificationManager
from utils.progress_bar import progress_bar


class CLIManager:
    """
        an compiler of utils functions to work with questionary and cli.
    """

    def __init__(self, notification_manager: NotificationManager):
        self.notifcation_manager = notification_manager

    def main_logo(self):
        print(figlet_format(text='PomodoroZ'))
        print('🍅 An extremely minimalist Command-line Pomodoro Timer for Linux Systems 🚀\n')

    def creator_info(self):
        print(f'⚡ {text_to_bold("Powered by")}: Lucas Amorim (Kakaroto)')
        print(f'📧 {text_to_bold("Email")}: lucas.ala1999@gmail.com')
        print(f'🐙 {text_to_bold("GitHub")}: https://github.com/lucaslima18')
        print(f'🔗 {text_to_bold("LinkedIn")}: https://www.linkedin.com/in/lucas-amorim-b09691173/')
        print('\n\n')

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def paginated_choice(
        self,
        message: str,
        offset: int,
        limit: int,
        task_list: List[str]
    ) -> str:
        page_content = task_list[offset-1:offset+limit-1]
        page_content.extend(
                paginated_menu(
                    offset=offset,
                    limit=limit,
                    menu_lenght=len(task_list))
            )

        task = questionary.select(
            message=message,
            choices=page_content
        ).ask()

        return task

    def create_pomodoro(self):
        self.clear_terminal()
        self.main_logo()
        print("Standalone Pomodoro")
        print(self.motivational_phrase())
        print("🕒 Total time: " "20m\n\n")

        progress_bar(total_seconds=5,  state='pomodoro')
        self.notifcation_manager.send_notification(
            message="Time to take a well-deserved break. 🌟 Keep up the good work! 🚀",
            title="🍅 Pomodoro X completed successfully! 🎉",
            state="pomodoro_finished"
        )
        self.clear_terminal()
        self.main_logo()
        questionary.confirm("⏳ Start break?").ask()
        self.clear_terminal()
        self.main_logo()

    def create_break(self):
        print("Pomodoro Name: Test")
        print("Pomodoro Description: Teste descricao")
        print("Total time: " "12h")
        progress_bar(total_seconds=5, state='break') .send_notification(
            message="Time to get back to work! 💪 Start your next Pomodoro session now. ⏳",
            title="🍅 Break Over! Let's Begin Pomodoro X! 🔥",
            state="break_finished"
        )

    def ask_new_pomodoro(self):
        CLIManager.clear_terminal()
        CLIManager.main_logo()
        questionary.confirm("⏳ Start new pomodoro?").ask()

    def motivational_phrase(self):
        phrases = [
            "You're just one Pomodoro away from great progress! 🚀",
            "Keep going, every Pomodoro counts! 💪",
            "Today's effort will be tomorrow's success. 🌟",
            "Stay focused, you're doing great! 🎯",
            "Persistence is the key to achievement. 🗝️",
            "One step at a time, one Pomodoro at a time. 🕒",
            "You are capable of great things, keep going! 🌠",
            "Every completed Pomodoro is a victory. 🏆",
            "Work hard, rest well, repeat. 🔄",
            "The road to success is paved with small, consistent steps. 🚶‍♂️"
        ]
        return random.choice(phrases)
    
    def break_phrase(self):
        ...

    def pomodoro_notifications(self, state: str):
        match state:
            case 'pomodoro_finish':
                self.notifcation_manager.send_notification(
                    message="Time to take a well-deserved break. 🌟 Keep up the good work! 🚀",
                    title="🍅 Pomodoro X completed successfully! 🎉",
                    state="pomodoro_finished"
                )

            case 'break_finish':
                self.notifcation_manager.send_notification(
                    message="Time to get back to work! 💪 Start your next Pomodoro session now. ⏳",
                    title="🍅 Break Over! Let's Begin Pomodoro X! 🔥",
                    state="break_finished"
                )
