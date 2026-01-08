
import tkinter as tk
from tkinter import ttk

import random
import threading
import time

from winotify import Notification, audio


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Water reminder")

        self.app_controlling = AppController()

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.heading_label = ttk.Label(self,
                                       text="Water reminder",
                                       font=("Arial", 18))
        self.heading_label.grid(row=0, column=0, padx=5, pady=5)

        self.config_frame = ConfigFrame(self,
                                        controller=self.app_controlling)
        self.config_frame.grid(row=1, column=0)
        self.app_controlling.config = self.config_frame


class ConfigFrame(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.controller = controller

        self.period_var = tk.IntVar(value=5)

        self.stop_event = threading.Event()
        self.thread = None

        timer_label = ttk.Label(self,
                                text="Reminder Setup",
                                font=("Arial", 16))
        timer_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.timer_spinbox = ttk.Spinbox(self,
                                         from_=5,
                                         to=60,
                                         values=(5, 15, 30, 45, 60),
                                         textvariable=self.period_var,
                                         width=5,
                                         font=("Arial", 16))
        self.timer_spinbox.grid(row=1, column=0, rowspan=2, padx=5, pady=5)

        self.start_button = ttk.Button(self,
                                       text="Start",
                                       command=self.on_start)
        self.start_button.grid(row=1, column=1, padx=5, pady=3)

        self.stop_button = ttk.Button(self,
                                      text="Stop",
                                      state=tk.DISABLED,
                                      command=self.on_stop)
        self.stop_button.grid(row=2, column=1, padx=5, pady=3)

    def on_start(self):
        self.disable_widgets()
        self.controller.start_notificator(self.period_var.get())

    def on_stop(self):
        self.enable_widgets()
        self.controller.stop_notificator()

    def disable_widgets(self):
        self.timer_spinbox.configure(state=tk.DISABLED)
        self.start_button.configure(state=tk.DISABLED)
        self.stop_button.configure(state=tk.NORMAL)

    def enable_widgets(self):
        self.timer_spinbox.configure(state=tk.NORMAL)
        self.start_button.configure(state=tk.NORMAL)
        self.stop_button.configure(state=tk.DISABLED)


class AppController:
    def __init__(self):
        self.config = None

    def start_notificator(self, period):
        self.config.stop_event.clear()

        self.config.thread = threading.Thread(
            target=Setup.run,
            args=(period, self.config.stop_event),
            daemon=True)
        self.config.thread.start()

    def stop_notificator(self):
        self.config.stop_event.set()


class Setup:
    WATER_QUOTES = [
        "Drink me – your body says thanks!",
        "Take a break, grab some water!",
        "More water, more focus!",
        "Hydration is motivation!",
        "A sip for your energy!",
        "Thirsty? Grab the bottle!",
        "Better water than a headache!",
        "Refill yourself – drink up!",
        "Your body screams: water!",
        "Clear mind needs clear water!"
    ]

    @staticmethod
    def notification_setup():
        message = random.choice(Setup.WATER_QUOTES)

        toast = Notification(app_id="Water Reminder",
                             title="Reminder",
                             msg=message,
                             duration="short")
        toast.set_audio(audio.Mail, loop=False)
        toast.show()

    @staticmethod
    def run(period, stop_event):
        while not stop_event.is_set():
            time.sleep(period)
            Setup.notification_setup()


root = MainWindow()
root.mainloop()
