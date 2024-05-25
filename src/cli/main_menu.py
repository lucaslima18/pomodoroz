import questionary

from typing import Any

from src.libs.notification_manager import NotificationManager
from src.utils.progress_bar import progress_bar

from src.cli.cli_manager import CLIManager

class MenuManager:
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
        self.main_menu_selector()

    def main_menu_selector(self) -> str:
        CLIManager.clear_terminal()
        CLIManager.main_logo()
        CLIManager.creator_info()
        main_menu_item = questionary.select(
            message="What you whant to do?",
            choices=["📁 My Projects", "📊 My Stats", "🍅 Start an standalone Pomodoro"]
        ).ask()
        
        match main_menu_item:
            case '📁 My Projects':
                self.__project_select(offset=1, limit=5)

            case '📊 My Stats':
                ...

            case '🍅 Start an standalone Pomodoro':
                self.__pomodoro_manager()
    
    def __project_select(self, offset: int,limit: int):
        CLIManager.clear_terminal()
        CLIManager.main_logo()
        buceta = [
            'Project Alpha', 'Project Beta', 'Project Gamma', 'Project Delta',
            'Project Epsilon', 'Project Zeta', 'Project Eta', 'Project Theta',
            'Project Iota', 'Project Kappa', 'Project Lambda', 'Project Mu'
        ]
        project = CLIManager.paginated_choice(
            message='Select a project:',
            offset=offset,limit=limit,
            task_list=buceta
        )

        match project:
            case '🏠 Home':
                self.main_menu_selector()
            
            case '⏪ Previous':
                self.__project_select(offset=offset-limit, limit=limit)
            
            case '⏩ next':
                self.__project_select(offset=offset+limit, limit=limit)

            case _ if project in buceta:
                self.__project_task_select(offset=1, limit=5)
    
    def __project_task_select(self, offset: int, limit: int):
        CLIManager.clear_terminal()
        CLIManager.main_logo()
        buceta = [
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
        project = CLIManager.paginated_choice(message='How task you want start?',offset=offset,limit=limit,task_list=buceta)

        match project:
            case '🏠 Home':
                self.main_menu_selector()
            
            case '⏪ Previous':
                self.__project_select(offset=offset-limit, limit=limit)
            
            case '⏩ next':
                self.__project_select(offset=offset+limit, limit=limit)

            case _ if project in buceta:
                self.__pomodoro_manager()
            
        
    def __pomodoro_manager(self):
        ## fazer com que tenha um controle do pomodoro tipo, iniciar descanso e etc...
        CLIManager.clear_terminal()
        CLIManager.main_logo()
        print("Pomodoro Name: Test")
        print("Pomodoro Description: Teste descricao")
        print("Total time: " "12h")
    
        progress_bar(total_seconds=30, state='pomodoro')
        self.notifications.send_notification(
            message="Time to take a well-deserved break. 🌟 Keep up the good work! 🚀",
            title="🍅 Pomodoro X completed successfully! 🎉",
            state="pomodoro_finished"
        )
        CLIManager.clear_terminal()
        CLIManager.main_logo()
        questionary.confirm("⏳ Start break?").ask()
        CLIManager.clear_terminal()
        CLIManager.main_logo()
        print("Pomodoro Name: Test")
        print("Pomodoro Description: Teste descricao")
        print("Total time: " "12h")
        progress_bar(total_seconds=30, state='break')
        self.notifications.send_notification(
            message="Time to get back to work! 💪 Start your next Pomodoro session now. ⏳",
            title="🍅 Break Over! Let's Begin Pomodoro X! 🔥",
            state="break_finished"
        )
        CLIManager.clear_terminal()
        CLIManager.main_logo()
        questionary.confirm("⏳ Start new pomodoro?").ask()
