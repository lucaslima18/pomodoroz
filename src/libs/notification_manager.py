from plyer import notification

class NotificationManager():
    def __init__(self, app_name: str, app_icon: str) -> None:
        self.app_name = app_name
        self.app_icon = app_icon

    def send_notification(self, message: str, title: str) -> None:
        notification.notify(
            app_name=self.app_name,
            title=title,
            message=message,
            app_icon=self.app_icon
        )
