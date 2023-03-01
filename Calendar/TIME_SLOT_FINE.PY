import tkinter as tk
from datetime import datetime as dt, timedelta
import locale
import json
import datetime
##COlors tem de ser guardado num monog colletion diferente

locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

button_colors = ["green", "yellow", "red"]

class TimeSlotButton(tk.Button):
    all_buttons = []

    def __init__(self, parent, time_slot, **kwargs):
        super().__init__(parent, text=time_slot, bg="green", **kwargs)
        self.time_slot = time_slot
        self.color_index = 0
        self.config(command=self.change_color)
        self.all_buttons.append(self)

    def change_color(self):
        if self["state"] == "disabled":
            return
        if self.color_index < len(button_colors) - 1:
            self.color_index += 1
        self.config(bg=button_colors[self.color_index])

    def reset_color(self):
        self.config(bg="green")
        self.color_index = 0


class TimeSlotApp:
    def __init__(self, master, start_date):
        self.master = master
        self.master.title("Weekly Time Slot Agenda")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)

        self.times = [f"{hour}:00" for hour in range(9, 18)]
        self.num_days = 7
        self.start_date = start_date.replace(hour=9, minute=0, second=0, microsecond=0)
        self.end_date = self.start_date + timedelta(days=self.num_days)
        self.current_day_index = (self.start_date - start_date.replace(day=1)).days

        self.button_colors = ["green", "yellow", "red"]

        self.create_day_labels()
        self.create_time_slot_labels_and_buttons()
        # save_button = tk.Button(self.master, text="Save and Exit", command=self.save_and_close)
        # save_button.grid(row=len(self.times)+2, column=self.num_days//2, padx=5, pady=5)

    def create_day_labels(self):
        for i in range(self.num_days):
            day = self.start_date + timedelta(days=i)
            week_day = day.strftime("%A")
            week_day_pt = week_day.capitalize() if week_day != 'Saturday' and week_day != 'Sunday' else week_day
            week_day_pt = week_day_pt[:3]
            label = tk.Label(self.master, text=week_day_pt + " " + day.strftime("%d/%m/%Y"))

            label.grid(row=0, column=i+1, padx=5, pady=5)

    def create_time_slot_labels_and_buttons(self):
        for j, time in enumerate(self.times):
            label = tk.Label(self.master, text=time)
            label.grid(row=j+1, column=0, padx=5, pady=5)
            for i in range(self.num_days):
                button = TimeSlotButton(self.master, time, width=8, height=2)
                button.grid(row=j+1, column=i+1, padx=5, pady=5, sticky="NEWS")
                self.master.rowconfigure(j+1, weight=1)

    def reset_colors(self):
        for child in self.master.winfo_children():  
            if isinstance(child, TimeSlotButton):
                child.reset_color()

    def save_colors(self,month,first_day):
        colors = {}
        for button in TimeSlotButton.all_buttons:
            colors[f"{button.time_slot} day:{self.current_day_index + button.grid_info()['column']-1}"] = button.color_index
        with open('colors'+str(month)+ "_"+str(first_day)+ '.json', 'w') as f:
            json.dump(colors, f)

    def load_colors(self,start_date):
        try:
            month = start_date.month
            first_day = start_date.day
            with open('colors'+str(month)+ "_"+str(first_day)+ '.json', 'r') as f:
                colors = json.load(f)
                for button in TimeSlotButton.all_buttons:
                    color_index = colors.get(f"{button.time_slot} day:{self.current_day_index + button.grid_info()['column']-1}", 0)
                    button.color_index = color_index
                    button.config(bg=button_colors[color_index])
        except FileNotFoundError:
            print("Colors file not found. Defaulting to green.")

    def save_and_close(self,start_date):
        month = start_date.month
        first_day = start_date.day
        self.save_colors(month,first_day)
        self.master.destroy()


def divide_year_into_weeks(start_date,end_date, week_length=7):
    num_days = (end_date - start_date).days + 1
    num_weeks = (num_days + week_length - 1) // week_length
    weeks = []
    for i in range(num_weeks):
        start = i * week_length
        end = min(start + week_length, num_days)
        week = [start_date + datetime.timedelta(days=j) for j in range(start, end)]
        if len(week) < week_length:
            week += [None] * (week_length - len(week))
        weeks.append(week)
    return weeks


def showTimeSlot():
        startDate = '2/27/23'
        date_obj = datetime.datetime.strptime(startDate, '%m/%d/%y')
        start_date = datetime.date(date_obj.year, date_obj.month, date_obj.day)
        start_date2 = start_date + datetime.timedelta(days=7)
        start_date3 = start_date2 + datetime.timedelta(days=7)
        
        start_time = datetime.time(hour=9, minute=0, second=0)

        start_datetime = datetime.datetime.combine(start_date, start_time)
        root = tk.Tk()
        app = TimeSlotApp(root, start_date=start_datetime)
        root.protocol("WM_DELETE_WINDOW", lambda : app.save_and_close(start_datetime))
        app.load_colors(start_datetime)

        root.mainloop()

#showTimeSlot()
