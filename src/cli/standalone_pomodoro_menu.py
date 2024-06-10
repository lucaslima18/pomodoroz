from cli.cli_manager import CLIManager


class StandalonePomodoroMenu:
    def __init__(self, notification_manager):
        self.cli_manager = CLIManager(
            notification_manager=notification_manager
        )

    def run(self):
        self.cli_manager.create_pomodoro()
        self.cli_manager.create_break()
        self.cli_manager.ask_new_pomodoro()
