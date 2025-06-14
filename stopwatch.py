import tkinter as tk 
from tkinter import ttk 
import time


class StopWatch(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title("Stop Watch")
        self.geometry("300x150")
        self.configure(bg="#3498db")

        # Initialize variables
        self.time_elapsed = 0
        self.is_running = False

        # Label for displaying time
        self.label_timer = ttk.Label(self, text = "00:00:00:000", font=('Arial', 24), 
        anchor="center", foreground="white", background="#3498db")
        self.label_timer.pack(pady=20)

        # Start/Stop button
        self.button_start_stop = ttk.Button(self, text="Start", 
        command=self.start_stop, style="TButton")

        self.button_start_stop.pack(side = tk.LEFT, padx = 10)

        # Reset button
        self.button_reset = ttk.Button(self, text="Reset", 
        command=self.reset, style="TButton")

        self.button_reset.pack(side = tk.RIGHT, padx = 10)

        # Configure button style
        self.style = ttk.Style()
        self.style.configure("TButton", padding=7, font=("Helvatica", 12))

        # Initialize the stopwatch
        self.update_time()


    def start_stop(self):
        # Toggle start/stop functionality
        if self.is_running:
            self.is_running = False
            self.button_start_stop.config(text="Start")
        
        else:
            self.is_running = True
            self.button_start_stop.config(text="Stop")
            self.start_time = time.time() - self.time_elapsed
            self.update_time()



    def reset(self):
        # Reset the stopwatch
        self.is_running = False
        self.time_elapsed = 0
        self.label_timer.config(text="00:00:00:000")
        self.button_start_stop.config(text="Start")

    def update_time(self):
        # Update the displayed time
        if self.is_running:
            elapsed_time = time.time() - self.start_time
            self.time_elapsed = elapsed_time
        else:
            elapsed_time = self.time_elapsed

        # Calculate hours, minutes, seconds, and milliseconds
        hours = int(elapsed_time / 3600)
        minutes = int((elapsed_time % 3600) / 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time % 1) * 1000)

        # Format the time string
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}"

        # Update the label text
        self.label_timer.config(text=time_str)

        # Schedule the update after 10 milliseconds
        self.after(10, self.update_time)



if __name__ == "__main__":

    app = StopWatch()
    app.mainloop()