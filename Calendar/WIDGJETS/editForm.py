import tkinter as tk
from WIDGJETS.services.dataServices import editApointment
times = ["01:00", "00:30", "00:20"]

begginigValues = ["11:00", "11:30", "12:00"]


typesOfServices = ["massagem"]



def editForm(root,item_props):
    top_level = newApointmenLayout(root)
    
    submit_button = tk.Button(top_level, text="Submit", command=lambda: editApointment(top_level,item_props,serviceE.get(), timeE.get(), begginingE.get()))
    submit_button.pack()
   


def newApointmenLayout(root):
    global serviceE,timeE,begginingE
    # Create the top level window
    top_level = tk.Toplevel(root)
    top_level.title("Make Apointment")
    # Create a label for the first option
    option1_label = tk.Label(top_level, text="Select Type Of service:")
    option1_label.pack()
    # Create a StringVar to store the selected option
    serviceE = tk.StringVar()
    # Define the options
    # Create the Radiobuttons for the options
    for services in typesOfServices:
        tk.Radiobutton(top_level, text=services, variable=serviceE, value=services).pack()
    # Create a label for the second option
    option2_label = tk.Label(top_level, text="Select Time for the service:")
    option2_label.pack()
    # Create a StringVar to store the selected option
    timeE = tk.StringVar()
    # Define the options
    # Create the Radiobuttons for the options
    for t in times:
        tk.Radiobutton(top_level, text=t, variable=timeE, value=t).pack()
    # Create a label for the third option
    option3_label = tk.Label(top_level, text="Select A beggining time:")
    option3_label.pack()
    # Create a StringVar to store the selected option
    begginingE = tk.StringVar()
    # Define the options
    # Create the Radiobuttons for the options
    for beginingTime in begginigValues:
        tk.Radiobutton(top_level, text=beginingTime, variable=begginingE, value=beginingTime).pack()
    return top_level