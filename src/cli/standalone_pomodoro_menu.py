import questionary

from questionary import ValidationError
from cli.cli_manager import CLIManager
from libs.notification_manager import NotificationManager
from libs.pomodoro.pomodoro_manager import PomodoroManager
from libs.schemas import PomodoroInfo
from libs.pomodoro.pomodoro_dto import TimeForPomodoroSecDTO, PomodoroCountDTO


class StandalonePomodoroMenu:
    def __init__(
            self,
            notification_manager: NotificationManager,
        ):
        self.cli_manager = CLIManager(
            notification_manager=notification_manager,
        )

    def run(self):
        
        
        self.cli_manager.create_pomodoro(
            pomodoro_manager=PomodoroManager(pomodoro_info=self.ask_pomodoro_infos())
        )
    
    def ask_pomodoro_infos(self) -> PomodoroInfo:
        try:
            self.cli_manager.clear_terminal()
            self.cli_manager.main_logo()
            name = questionary.text(message="Type the task name: ").ask()
            description = questionary.text("Describe your task: ").ask()
            time_for_pomodoro_sec = int(questionary.text("How many minutes of concentration do you want per Pomodoro?", validate=TimeForPomodoroSecDTO).ask())*60
            count = questionary.text(f"How many Pomodoros of {time_for_pomodoro_sec/60} minutes will be needed to complete your task?", validate=PomodoroCountDTO).ask()
            
            return PomodoroInfo(name=name, description=description, time_for_pomodoro_sec=time_for_pomodoro_sec, count=count)
        
        except Exception as err:
            print(err)
