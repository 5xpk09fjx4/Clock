import tkinter as tk
from tkinter import font
import time

class ClockApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Orologio")
        self.root.configure(bg="black")
        
        self.time_label = tk.Label(self.root, font=("Arial", 60), fg="white", bg="black") #opzioni font colori e caratteri
        self.time_label.pack(pady=20)
        
        self.update_time()
    
    def update_time(self):
        current_time = time.strftime("%H:%M:%S %d/%m/%Y") #Mostra Ora e Data
        self.time_label.configure(text=current_time)
        self.time_label.after(1000, self.update_time)

app = ClockApp()
app.root.mainloop()
