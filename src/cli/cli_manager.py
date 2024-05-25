import os
import questionary

from typing import List, Any
from pyfiglet import figlet_format

from src.utils.text_to_bold import text_to_bold
from src.utils.pagination import paginated_menu

class CLIManager:
    """
        an compiler of utils functions to work with questionary and cli.
    """

    @staticmethod
    def main_logo():
        print(figlet_format(text='PomodoroZ'))
        print('🍅 An extremely minimalist Command-line Pomodoro Timer for Linux Systems 🚀\n')
    
    @staticmethod
    def creator_info():
        print(f'⚡ {text_to_bold("Powered by")}: Lucas Amorim (Kakaroto)')
        print(f'📧 {text_to_bold("Email")}: lucas.ala1999@gmail.com')
        print(f'🐙 {text_to_bold("GitHub")}: https://github.com/lucaslima18')
        print(f'🔗 {text_to_bold("LinkedIn")}: https://www.linkedin.com/in/lucas-amorim-b09691173/')
        print('\n\n')

    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def paginated_choice(message: str, offset: int, limit: int, task_list: List[str | Any]) -> str:
            page_content = task_list[offset-1:offset+limit-1]
            page_content.extend(
                    paginated_menu(offset=offset, limit=limit, menu_lenght=len(task_list))
                )

            task = questionary.select(
                message=message,
                choices=page_content
            ).ask()

            return task
