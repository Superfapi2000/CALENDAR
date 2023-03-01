from WIDGJETS.services.data.apointmentsDATA import apointmentsData,addApointmentToData 
class Apointment:
    def __init__(self,day,typeOfService,time,beggining,finish):
        self.day = day
        self.typeOfService = typeOfService
        self.time = time
        self.beggining = beggining
        self.finish = finish
    def createAppointment(self):
            addApointmentToData(self)
def deleteApointment(day,typeOfService,beggining):
    #deleteApointment(day,typeOfService,beggining)
    dayOfTheApointment = apointmentsData[day] 
    filterdList = filter(lambda  it: (not (typeOfService == it.typeOfService and beggining == it.beggining)),dayOfTheApointment)
    apointmentsData[day] = list(filterdList)


def createNewApointment(day,typeOfService,time,beggining,finish):
    service = Apointment(day,typeOfService,time,beggining,finish)
    print("""""",day)
    service.createAppointment()
    return service
