import base64
import os
import subprocess
from xml.sax.saxutils import escape

POWERSHELL_PATH = '/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe'

POWERSHELL_APP_ID = (
    '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}'
    '\\WindowsPowerShell\\v1.0\\powershell.exe'
)

TOAST_SCRIPT_TEMPLATE = """
[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
[Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime] | Out-Null
$iconSource = '__ICON_SOURCE__'
$iconTarget = ''
if ($iconSource -ne '') {
    $iconTarget = Join-Path $env:TEMP 'pomodoroz_icon.png'
    Copy-Item -LiteralPath $iconSource -Destination $iconTarget -Force
}
$toastXml = '__TOAST_XML__'.Replace('__ICON_TARGET__', $iconTarget)
$xml = New-Object Windows.Data.Xml.Dom.XmlDocument
$xml.LoadXml($toastXml)
$toast = New-Object Windows.UI.Notifications.ToastNotification $xml
[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('__APP_ID__').Show($toast)
"""


def running_on_wsl() -> bool:
    return 'WSL_DISTRO_NAME' in os.environ


def to_windows_path(linux_path: str) -> str:
    result = subprocess.run(
        ['wslpath', '-w', linux_path],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def build_toast_xml(title: str, message: str, with_icon: bool) -> str:
    image_tag = ''
    if with_icon:
        image_tag = '<image placement="appLogoOverride" src="file:///__ICON_TARGET__"/>'
    return (
        '<toast><visual><binding template="ToastGeneric">'
        f'{image_tag}'
        f'<text>{escape(title)}</text>'
        f'<text>{escape(message)}</text>'
        '</binding></visual></toast>'
    )


def notify_windows(title: str, message: str, icon_path: str | None = None) -> None:
    """Show a Windows toast notification from inside WSL.

    Windows cannot render toast images from the WSL network share, so the icon
    is copied to the Windows temp folder before the toast is shown.

    Args:
        title: Toast headline.
        message: Toast body text.
        icon_path: Linux path to a PNG shown as the app logo. Ignored if missing.

    Raises:
        FileNotFoundError: powershell.exe is not reachable from WSL.
        subprocess.CalledProcessError: PowerShell rejected the toast script.
    """
    has_icon = bool(icon_path) and os.path.exists(icon_path)
    icon_source = to_windows_path(icon_path) if has_icon else ''
    toast_xml = build_toast_xml(title, message, with_icon=has_icon)
    script = (
        TOAST_SCRIPT_TEMPLATE
        .replace('__ICON_SOURCE__', icon_source.replace("'", "''"))
        .replace('__TOAST_XML__', toast_xml.replace("'", "''"))
        .replace('__APP_ID__', POWERSHELL_APP_ID)
    )
    encoded_script = base64.b64encode(script.encode('utf-16-le')).decode('ascii')
    subprocess.run(
        [POWERSHELL_PATH, '-NoProfile', '-NonInteractive', '-EncodedCommand', encoded_script],
        check=True,
        capture_output=True,
    )
