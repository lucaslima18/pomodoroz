import time


def progress_bar(total_seconds: int, state: str = None) -> None:
    bar_length = 30
    start_time = time.time()
    end_time = start_time + total_seconds
    
    #TODO: fazer funcionalidades de pausa e cancelamento de pomodoro
    while time.time() < end_time:
        elapsed_time = time.time() - start_time
        remaning_time = total_seconds - elapsed_time
        fraction = elapsed_time / total_seconds

        bar = int(fraction * bar_length + 1) * '█'
        padding = int(bar_length - len(bar)) * '░'

        ending = '\r' if remaning_time > 0 else '\n'
        minutes, seconds = divmod(int(remaning_time), 60)
        time_display = f'{minutes:02}:{seconds:02}'

        if state and 'pomodoro' in state:
            state_char = '🍅'

        elif state and 'break' in state:
            state_char = '💤'

        else:
            state_char = 'progress:'
        print(
            f'  {state_char} [{bar}{padding}] {int(fraction*100)}% | ⏰ {time_display}',
            end=ending
        )
        time.sleep(.01)
