import tkinter as tk
from ttkthemes import ThemedStyle
import tkinter as tk
from tkinter import ttk

class ShadowButton(ttk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(style="ShadowButton.TButton")
        
        self.bind("<Enter>", lambda event: self.config())
        self.bind("<Leave>", lambda event: self.config())

root = tk.Tk()
style = ttk.Style(root)

style.configure("ShadowButton.TButton",
                background="#4c4c4c", foreground="#fff",
                borderwidth=0, padding=10,
                font=("Helvetica", 14),
                anchor="center")

style.map("ShadowButton.TButton",
          background=[("active", "#5c5c5c")],
          relief=[("active", tk.SOLID)])

style.configure("ShadowButton.TButton", 
                lightcolor="#333",
                darkcolor="#000",
                bordercolor="#000",
                borderwidth=2,
                relief=tk.FLAT)

button = ShadowButton(root, text="Click me!")
button.pack(pady=10)

root.mainloop()

# def on_button_click():
#     print("Button clicked")

# root = tk.Tk()
# root.configure(bg="#333")

# button = tk.Button(root, text="Click me!", font=("Helvetica", 16), fg="#fff", bd=0,
#                    bg="#4c4c4c", activebackground="#5c5c5c",
#                    command=on_button_click)
# button.pack(pady=10)

# root.mainloop()

# root = tk.Tk()
# style = ThemedStyle(root)
# style.set_theme("equilux")

# label = tk.Label(root, text="Hello, world!", font=("Helvetica", 24))
# label.pack(padx=20, pady=20)

# button = tk.Button(root, text="Click me!", font=("Helvetica", 14))
# button.pack(padx=20, pady=20)

# root.mainloop()
