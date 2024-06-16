from typing import List
from pydantic import BaseModel

class PomodoroInfo(BaseModel):
    name: str
    description: str
    time_for_pomodoro_sec: int
    count: int

class PomodoroProgress(BaseModel):
    break_time_sec: int
    done: bool

class Pomodoro(BaseModel):
    pomodoro_info: PomodoroInfo
    pomodoro_progress: List[PomodoroProgress]