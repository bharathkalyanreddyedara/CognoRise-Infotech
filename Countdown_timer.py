import tkinter as tk
import time
from threading import Thread


def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = f'{mins:02d}:{secs:02d}'
        timer_label.config(text=time_format)
        root.update()
        time.sleep(1)
        seconds -= 1
    timer_label.config(text="Time's up!")


def start_timer():
    try:
        total_seconds = int(entry.get()) * 60
        if total_seconds <= 0:
            raise ValueError("Time must be a positive number.")
        timer_thread = Thread(target=countdown_timer, args=(total_seconds,))
        timer_thread.start()
    except ValueError as e:
        timer_label.config(text=f"Invalid input: {e}")


root = tk.Tk()
root.title("Countdown Timer")

entry_label = tk.Label(root, text="Enter time in minutes:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

timer_label = tk.Label(root, text="00:00", font=('Helvetica', 48))
timer_label.pack()

root.mainloop()
