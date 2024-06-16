import questionary

from typing import Any

from libs.notification_manager import NotificationManager
from libs.schemas import PomodoroInfo
from libs.pomodoro.pomodoro_manager import PomodoroManager
from utils.progress_bar import progress_bar
from cli.cli_manager import CLIManager
from cli.standalone_pomodoro_menu import StandalonePomodoroMenu


class MenuManager:
    def __init__(
        self, app_name: str,
        app_icon: str,
        storage_path: str
    ) -> None:
        self.notifiction_manager = NotificationManager(
            app_name=app_name,
            app_icon=app_icon,
            storage_path=storage_path
        )
        self.cli_manager = CLIManager(notification_manager=self.notifiction_manager)

    def run(self) -> str:
        self.main_menu_selector()

    def main_menu_selector(self) -> str:
        self.cli_manager.clear_terminal()
        self.cli_manager.main_logo()
        self.cli_manager.creator_info()
        main_menu_item = questionary.select(
            message="What you whant to do?",
            choices=[
                "📁 My Projects",
                "📊 My Stats",
                "🍅 Start an standalone Pomodoro"
            ]
        ).ask()

        match main_menu_item:
            case '📁 My Projects':
                self.__project_select(offset=1, limit=5)

            case '📊 My Stats':
                ...

            case '🍅 Start an standalone Pomodoro':
                StandalonePomodoroMenu(
                    notification_manager=self.notifiction_manager
                ).run()
                self.main_menu_selector()

    def __project_select(self, offset: int,limit: int):
        self.cli_manager.clear_terminal()
        self.cli_manager.main_logo()
        task_fake_list = [
            'Project Alpha', 'Project Beta', 'Project Gamma', 'Project Delta',
            'Project Epsilon', 'Project Zeta', 'Project Eta', 'Project Theta',
            'Project Iota', 'Project Kappa', 'Project Lambda', 'Project Mu'
        ]
        project = self.cli_manager.paginated_choice(
            message='Select a project:',
            offset=offset,limit=limit,
            task_list=task_fake_list
        )

        match project:
            case '🏠 Home':
                self.main_menu_selector()

            case '⏪ Previous':
                self.__project_select(offset=offset-limit, limit=limit)

            case '⏩ next':
                self.__project_select(offset=offset+limit, limit=limit)

            case _ if project in task_fake_list:
                self.__project_task_select(offset=1, limit=5)

    def __project_task_select(self, offset: int, limit: int):
        self.cli_manager.clear_terminal()
        self.cli_manager.main_logo()
        task_fake_list = [
            'Task Planning 🍅🍅🍅',
            'Task Design 🍅🍅🍅🍅',
            'Task Development 🍅🍅',
            'Task Testing 🍅🍅🍅🍅🍅',
            'Task Deployment 🍅',
            'Task Documentation 🍅🍅🍅',
            'Task Review 🍅🍅🍅🍅',
            'Task Analysis 🍅🍅',
            'Task Meeting 🍅🍅🍅🍅🍅',
            'Task Feedback 🍅🍅',
            'Task Research 🍅🍅🍅',
            'Task Maintenance 🍅🍅🍅🍅'
        ]
        project = self.cli_manager.paginated_choice(message='How task you want start?',offset=offset,limit=limit,task_list=task_fake_list)

        match project:
            case '🏠 Home':
                self.main_menu_selector()
            
            case '⏪ Previous':
                self.__project_select(offset=offset-limit, limit=limit)
            
            case '⏩ next':
                self.__project_select(offset=offset+limit, limit=limit)
               
     
    def __pomodoro_manager(self):
       ...