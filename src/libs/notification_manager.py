from plyer import notification

from utils.sound_notification import sound_notification
from utils.windows_notification import notify_windows, running_on_wsl


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
            self.send_desktop_notification(message=message, title=title)
        except Exception as err:
            print(err)

        if state:
            self.send_sound_notification(state=state)

    def send_desktop_notification(self, message: str, title: str) -> None:
        if running_on_wsl():
            notify_windows(title=title, message=message, icon_path=self.app_icon)
            return

        notification.notify(
            app_name=self.app_name,
            title=title,
            message=message,
            app_icon=self.app_icon
        )

    def send_sound_notification(self, state: str):
        try:
            if 'pomodoro_finished' in state.lower():
                sound_notification(
                    f'{self.storage_path}/mp3/pomodoro_finished.mp3'
                )

            if 'break_finished' in state.lower():
                sound_notification(
                    f'{self.storage_path}/mp3/break_finished.mp3'
                )

        except Exception as err:
            # TODO: Dropar excessão customizada
            # TODO: usar logger para erros
            print(err)
