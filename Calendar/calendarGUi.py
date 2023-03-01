from tkinter import *
from tkcalendar import *
from WIDGJETS.showApointmentsWindow import showApointmentsWindow
from WIDGJETS.services.data.auxFunctions.auxFunctions import getRealTime
from VOICE_WIDGET.VOICE_TEST import createNewApointmentVoice
from WIDGJETS.newApointmentForm import newApointment_window
from WIDGJETS.timeSlots2 import showTimeSlot
BUTTON_SIZE_W = 17
BUTTON_SIZE_H = 3
BUTTON_FONT = ("Helvetica", 16)
def drawCalendar():
    root = Tk()
    root.title('NewCalender.py')
    root.geometry('1000x420')# 30 + 20 adiciona a posicçao relativa

    currDay = getRealTime()
    cal = Calendar(root, selectmode="day",year=currDay["Year"],month=currDay["Month"],day =currDay["Day"])
    cal.grid(row=0, column=1, sticky="nsew")
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    
   
    calendarLayout(root,cal)
    root.mainloop()


def calendarLayout(root,calendar):        
    my_button = Button(root, text="Get Day Apoitments",  command= lambda : showApointmentsWindow(root,"day",calendar.get_date()),font=BUTTON_FONT,width=BUTTON_SIZE_W, height=BUTTON_SIZE_H)
    my_button.grid(row =1 ,column = 0 ,sticky="SW")
    my_button = Button(root, text="Make Apointment", command =  lambda : newApointment_window(root,day = calendar.get_date()),font=BUTTON_FONT,width=BUTTON_SIZE_W, height=BUTTON_SIZE_H)
    my_button.grid(row = 3 ,column = 0 , sticky="SW")
    #my_button = Button(root, text="Delete Apointment", command =  lambda : deleteApointmentWindow(root,day = calendar.get_date()),font=BUTTON_FONT,width=BUTTON_SIZE_W, height=BUTTON_SIZE_H)
    #my_button.grid(row = 1 ,column = 1 , sticky="NS")
    my_button = Button(root, text="Show All Apointments", command= lambda : showApointmentsWindow(root,"All",calendar.get_date()),font=BUTTON_FONT,width=BUTTON_SIZE_W, height=BUTTON_SIZE_H)
    my_button.grid(row =1 ,column = 3 , sticky= "SE")
    my_button = Button(root, text="Voice Test",command=createNewApointmentVoice,font=BUTTON_FONT,width=BUTTON_SIZE_W, height=BUTTON_SIZE_H)
    my_button.grid(row =3 ,column = 3 ,sticky="SE")
    my_button = Button(root, text="Time Slot",command=lambda : showTimeSlot(root,calendar.get_date()),font=BUTTON_FONT,width=BUTTON_SIZE_W, height=BUTTON_SIZE_H)#
    my_button.grid(row =1,column = 1 )
   ## por os butoes x  x    
    #               x x 






drawCalendar()