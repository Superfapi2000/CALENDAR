import tkinter as tk
from datetime import datetime, timedelta
import locale

import json
locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

button_colors = ["green", "yellow", "red"]

def create_day_labels(root, start_date, num_days):
    for i in range(num_days):
        day = start_date + timedelta(days=i)
        week_day = day.strftime("%A")
        week_day_pt = week_day.capitalize() if week_day != 'Saturday' and week_day != 'Sunday' else week_day
        week_day_pt = week_day_pt[:3]
        label = tk.Label(root, text=week_day_pt + " " + day.strftime("%d/%m/%Y"))
        label.grid(row=0, column=i+1, padx=5, pady=5)

from functools import partial

def create_time_slot_labels_and_buttons(master, times, num_days,startDate):

    for j, time in enumerate(times):
        label = tk.Label(master, text=time)
        label.grid(row=j+1, column=0, padx=5, pady=5)
        ##        
        ###
        for i in range(num_days):
            
            button = tk.Button(master, text=time, bg="green", width=8, height=2)
            button.grid(row=j+1, column=i+1, padx=5, pady=5, sticky="NEWS")
            button.config(command=partial(change_color, button))
            master.rowconfigure(j+1, weight=1)

def change_color(button):
    if button["state"] == "disabled":
        return
    color_index = button_colors.index(button.cget("bg"))
    if color_index < len(button_colors) - 1:
        color_index += 1
    button.config(bg=button_colors[color_index])

def reset_colors(master):
    for child in master.winfo_children():  
        if isinstance(child, tk.Button):
            child.config(bg="green")

def save_colors(master, start_date):
    month = start_date.month
    first_day = start_date.day
    colors = {}
    for child in master.winfo_children():  
        if isinstance(child, tk.Button):
            color_index = button_colors.index(child.cget("bg"))
            row = child.grid_info()['row']-1
            column = child.grid_info()['column']-1
            colors[f"{child['text']}_day:{column}"] = color_index
    with open(f'colors{month}_{first_day}hi.json', 'w') as f:
        json.dump(colors, f)
    master.destroy()

def load_colors(master, start_date):
    try:
        month = start_date.month
        first_day = start_date.day
        with open(f'colors{month}_{first_day}hi.json', 'r') as f:
            colors = json.load(f)
            for child in master.winfo_children():
                if isinstance(child, tk.Button):
                    key = f"{child['text']}_day:{child.grid_info()['column']-1}"
                    if key in colors:
                        color_index = colors[key]
                        child.config(bg=button_colors[color_index])
    except FileNotFoundError:
        print("Colors file not found. Defaulting to green.")

# def save_and_close(toplevel, master, start_date):
#     save_colors(master, start_date)

def showTimeSlot(root,startDate):
    start_date = datetime.now()
    start_date = datetime.strptime(startDate, '%m/%d/%y')
    
    times = [f"{hour}:00" for hour in range(9, 18)]
    num_days = 7
    
    root = tk.Toplevel(root)
    root.title("Weekly Time Slot Agenda")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    create_day_labels(root, start_date, num_days)
    create_time_slot_labels_and_buttons(root, times, num_days,start_date)
    root.protocol("WM_DELETE_WINDOW", lambda : save_colors(root,start_date))
    
    load_colors(root, start_date)
    root.mainloop()
    
