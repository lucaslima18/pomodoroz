import os
import questionary
import random

from typing import List, Any
from pyfiglet import figlet_format
from datetime import timedelta

from utils.text_to_bold import text_to_bold
from utils.pagination import paginated_menu
from libs.pomodoro.pomodoro_manager import PomodoroManager
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
    
    def pomodoro_menu(self, pomodoro_manager: PomodoroManager):
        self.clear_terminal()
        self.main_logo()
        pomodoro_manager.show_pomodoro()
        
    def create_pomodoro(self, pomodoro_manager: PomodoroManager):
        for index, _ in enumerate(pomodoro_manager.pomodoro_progress):
            self.pomodoro_menu(pomodoro_manager=pomodoro_manager)
            progress_bar(total_seconds=pomodoro_manager.pomodoro_info.time_for_pomodoro_sec,  state='pomodoro')
            
            pomodoro_manager.end_pomodoro(pomodoro_to_end_index=index)

            if index < pomodoro_manager.pomodoro_info.count-1:
                self.notifcation_manager.send_notification(
                    message="Time to take a well-deserved break. 🌟 Keep up the good work! 🚀",
                    title="🍅 Pomodoro X completed successfully! 🎉",
                    state="pomodoro_finished"
                )
                self.create_break(pomodoro_manager=pomodoro_manager, act_pomodoro_index=index)
            
        self.notifcation_manager.send_notification(
            message="👏 Amazing! You've successfully completed all your Pomodoros for this task! 🏅 Excellent work! ✨",
            title="🏁 Task Completed Successfully! 🎉",
            state="pomodoro_finished"
        )
        
    def create_break(self, pomodoro_manager: PomodoroManager, act_pomodoro_index: int):
        self.pomodoro_menu(pomodoro_manager=pomodoro_manager)
        break_time = pomodoro_manager.pomodoro_progress[act_pomodoro_index]['break_time_sec']
        
        
        while not questionary.confirm("⏳ Start break?").ask():
            self.pomodoro_menu(pomodoro_manager=pomodoro_manager)

        self.pomodoro_menu(pomodoro_manager=pomodoro_manager)
        progress_bar(total_seconds=break_time, state='break')
        self.notifcation_manager.send_notification(
            message="Time to get back to work! 💪 Start your next Pomodoro session now. ⏳",
            title="🍅 Break Over! Let's Begin Pomodoro X! 🔥",
            state="break_finished"
        )

        while not questionary.confirm("🔄 Return to work?").ask():
            self.pomodoro_menu(pomodoro_manager=pomodoro_manager)

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
