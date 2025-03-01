import time
import csv
import ttkbootstrap as ttk
from tkinter import filedialog, messagebox
from ttkbootstrap.constants import *

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("⏱️ Stopwatch - Modern UI")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.style = ttk.Style(theme="cosmo")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.laps = []

        self.time_label = ttk.Label(root, text="00:00:00", font="Arial 40 bold", bootstyle="primary")
        self.time_label.pack(pady=20)

        self.start_btn = ttk.Button(root, text="Start", bootstyle="success-outline", command=self.start)
        self.stop_btn = ttk.Button(root, text="Stop", bootstyle="danger-outline", command=self.stop)
        self.reset_btn = ttk.Button(root, text="Reset", bootstyle="warning-outline", command=self.reset)
        self.lap_btn = ttk.Button(root, text="Lap", bootstyle="info-outline", command=self.record_lap)
        
        self.start_btn.pack(side="left", expand=True, padx=5, pady=10)
        self.stop_btn.pack(side="left", expand=True, padx=5, pady=10)
        self.reset_btn.pack(side="left", expand=True, padx=5, pady=10)
        self.lap_btn.pack(side="left", expand=True, padx=5, pady=10)

        self.lap_frame = ttk.Frame(root)
        self.lap_frame.pack(fill="both", expand=True, pady=10)
        self.lap_tree = ttk.Treeview(self.lap_frame, columns=("Lap", "Time"), show="headings")
        self.lap_tree.heading("Lap", text="Lap")
        self.lap_tree.heading("Time", text="Time")
        self.lap_tree.pack(fill="both", expand=True)

        root.bind("<space>", lambda e: self.start() if not self.running else self.stop())
        root.bind("r", lambda e: self.reset())
        root.bind("l", lambda e: self.record_lap())

        self.theme_btn = ttk.Button(root, text="Toggle Theme", bootstyle="secondary-outline", command=self.toggle_theme)
        self.theme_btn.pack(pady=5)

        self.update_display()

    def update_display(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
        self.time_label.config(text=time.strftime("%H:%M:%S", time.gmtime(self.elapsed_time)))
        self.root.after(100, self.update_display)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")

    def stop(self):
        if self.running:
            self.running = False
            self.start_btn.config(state="normal")
            self.stop_btn.config(state="disabled")

    def reset(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.laps.clear()
        for row in self.lap_tree.get_children():
            self.lap_tree.delete(row)
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")

    def record_lap(self):
        if self.running:
            lap_time = time.strftime("%H:%M:%S", time.gmtime(self.elapsed_time))
            self.laps.append(lap_time)
            self.lap_tree.insert("", "end", values=(len(self.laps), lap_time))

    def toggle_theme(self):
        current_theme = self.style.theme_use()
        new_theme = "darkly" if current_theme == "cosmo" else "cosmo"
        self.style.theme_use(new_theme)

root = ttk.Window(themename="cosmo")
app = Stopwatch(root)
root.mainloop()
