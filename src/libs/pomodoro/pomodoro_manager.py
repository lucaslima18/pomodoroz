import random

from typing import List, Dict
from datetime import timedelta

from ..schemas import PomodoroInfo, PomodoroProgress, Pomodoro


class PomodoroManager:
    def __init__(self, pomodoro_info: PomodoroInfo):
        self.pomodoro_info = pomodoro_info
        self.pomodoro_progress = self.__progress_calculate()

    def show_pomodoro(self):
        print(f"🏷️ Name: {self.pomodoro_info.name}")
        print(f"📝 Description: {self.pomodoro_info.description}")
        print(f"📈 Progress: {self.show_pomodoro_tomatoes()}")
        print(
            f"🕒 Total time: {timedelta(seconds=self.pomodoro_info.time_for_pomodoro_sec*self.pomodoro_info.count)}m\n\n"
        )
        print(self.motivational_phrase() + "\n\n")

    def show_pomodoro_tomatoes(self):
        try:
            return "".join(
                "🍏" if pomodoro["done"] else "🍅"
                for pomodoro in self.pomodoro_progress
            )

        except Exception as err:
            print(err)

    def end_pomodoro(self, pomodoro_to_end_index: int):
        self.pomodoro_progress[pomodoro_to_end_index]["done"] = True

    def motivational_phrase(self):
        phrases = [
            "Power comes in response to a need, not a desire. You have to create that need. – Goku 💪✨",
            "Sometimes, we have to look beyond what we want and do what’s best. – Piccolo 🧘‍♂️🌍",
            "There’s no such thing as fair or unfair in battle. There is only victory or in your case, defeat. – Vegeta ⚔️👊",
            "I am the hope of the universe. I am the answer to all living things that cry out for peace. – Goku 🌌🕊️",
            "Even the mightiest warriors experience fears. What makes them a true warrior is the courage that they possess to overcome their fears. – Vegeta 🛡️🔥",
            "You may have invaded my mind and my body, but there’s one thing a Saiyan always keeps: his pride! – Vegeta 🧠💪👑",
            "It's not about forcing your will on others. It's about inspiring others to pursue their own strength. – Goku 🌟💫",
            "To fight for others gives me power. I will fight for the world and everyone in it. – Gohan 🗡️🌍",
            "Push through the pain, giving up hurts more. – Vegeta 💥🛡️",
            "Every obstacle you overcome is another step forward towards your goal. – Goku 🚀🏆",
        ]

        return random.choice(phrases)

    def __progress_calculate(self) -> List[PomodoroProgress]:
        default_break_time_sec = 300
        try:
            if self.pomodoro_info.count > 4:
                breaks_without_addition = [
                    {"done": False, "break_time_sec": default_break_time_sec}
                    for _ in range(3)
                ]
                breaks_with_addition = [
                    {
                        "done": False,
                        "break_time_sec": default_break_time_sec
                        + (break_addition * default_break_time_sec),
                    }
                    for break_addition in range(self.pomodoro_info.count - 3)
                ]
                return breaks_without_addition + breaks_with_addition
            return [
                {"done": False, "break_time_sec": default_break_time_sec}
                for _ in range(self.pomodoro_info.count)
            ]
        except Exception as err:
            print(err)
