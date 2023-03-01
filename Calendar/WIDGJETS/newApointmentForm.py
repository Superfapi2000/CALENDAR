###
import tkinter as tk
from WIDGJETS.services.data.auxFunctions.auxFunctions import SumHours,getDayMonthYearWellFormated
from WIDGJETS.services.apointmentClass import createNewApointment
# Define the options
times = ["01:00", "00:30", "00:20"]

begginigValues = ["11:00", "11:30", "12:00"]


typesOfServices = ["massagem"]

def getAlldataForNewAppointment(top_level,day,service,time,beggining):
    try:
        day = getDayMonthYearWellFormated(day)
        finish = SumHours(time,beggining)
        
        createNewApointment(day,service,time,beggining,finish)
        top_level.destroy()
        #root.destroy()
    except:
        print("error")



def newApointment_window(root,day):
    top_level = newApointmentLayout(root)

    submit_button = tk.Button(top_level, text="Submit", command=lambda: getAlldataForNewAppointment(top_level,day,service.get(), time.get(), beggining.get()))
    submit_button.pack()



def newApointmentLayout(root):
    global service,time,beggining
    # Create the top level window
    top_level = tk.Toplevel(root)
    top_level.title("Make Apointment")
    # Create a label for the first option
    option1_label = tk.Label(top_level, text="Select Type Of service:")
    option1_label.pack()
    # Create a StringVar to store the selected option
    service = tk.StringVar()
    # Define the options
    # Create the Radiobuttons for the options
    for services in typesOfServices:
        tk.Radiobutton(top_level, text=services, variable=service, value=services).pack()
    # Create a label for the second option
    option2_label = tk.Label(top_level, text="Select Time for the service:")
    option2_label.pack()
    # Create a StringVar to store the selected option
    time = tk.StringVar()
    # Define the options
    # Create the Radiobuttons for the options
    for t in times:
        tk.Radiobutton(top_level, text=t, variable=time, value=t).pack()
    # Create a label for the third option
    option3_label = tk.Label(top_level, text="Select A beggining time:")
    option3_label.pack()
    # Create a StringVar to store the selected option
    beggining = tk.StringVar()
    # Define the options
    # Create the Radiobuttons for the options
    for beginingTime in begginigValues:
        tk.Radiobutton(top_level, text=beginingTime, variable=beggining, value=beginingTime).pack()
    return top_level