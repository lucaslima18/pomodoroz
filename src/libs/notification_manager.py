from plyer import notification
from src.utils.sound_notification import sound_notification


class NotificationManager:
    def __init__(
        self, app_name: str,
        app_icon: str,
        storage_path: str
    ) -> None:
        self.app_name = app_name
        self.app_icon = app_icon
        self.storage_path = storage_path

    def send_notification(
        self, message: str, title: str, state: str = None
    ) -> None:
        try:
            notification.notify(
                app_name=self.app_name,
                title=title,
                message=message,
                app_icon=self.app_icon
            )
            print(state)
            if state:
                self.send_sound_notification(state=state)

        except Exception as err:
            print(err)

    def send_sound_notification(self, state: str):
        try:
            if 'pomodoro_finished' in state.lower():
                sound_notification(
                    f'{self.storage_path}/mp3/pomodoro_finished.mp3'
                )
                print("tocando pomodoro finisher")

            if 'break_finished' in state.lower():
                sound_notification(
                    f'{self.storage_path}/mp3/break_finished.mp3'
                )
                print("tocando break finisher")

        except Exception as err:
            # TODO: Dropar excessão customizada
            # TODO: usar logger para erros
            print(err)
