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

            answers = questionary.form(
                name=questionary.text("Type the task name:"),
                description=questionary.text("Describe your task:"),
                time_for_pomodoro_sec=questionary.text(
                    "How many minutes of concentration do you want per Pomodoro?",
                    validate=TimeForPomodoroSecDTO,
                ),
                count=questionary.text(
                    "How many Pomodoros will be needed to complete your task?",
                    validate=PomodoroCountDTO,
                ),
            ).ask()

            return PomodoroInfo(
                name=answers["name"],
                description=answers["description"],
                time_for_pomodoro_sec=int(answers["time_for_pomodoro_sec"])*60,
                count=int(answers["count"]),
            )

        except Exception as err:
            print(err)
