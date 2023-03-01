from WIDGJETS.services.data.apointmentsDATA import getMongoData_ApointmentsDays,getDayData,deleteApointmentData,editApointmentData
from WIDGJETS.services.data.auxFunctions.auxFunctions import getDayMonthYearWellFormated,mergeSort,SumHours
from WIDGJETS.services.apointmentClass import Apointment

def getApointmentDay(day):
    formatted_date = getDayMonthYearWellFormated(day)
    apointments = transformMongoDataAndSorted(formatted_date)
    #here receive the Data in a array with all of them
    return apointments
   
def getAppointments():
    days = getMongoData_ApointmentsDays()
    apointments = []
    #map Aqui  
    for day in days:
        apointments += transformMongoDataAndSorted(day)
    return apointments

def transformMongoDataAndSorted(day):
    apointmentsMongo = getDayData(day)
    apointmentsArray = []
    for data in apointmentsMongo:
        apointmentsArray += [data]
    #if day in apointment:
    size= len(apointmentsArray)
    mergeSort(apointmentsArray,0,size-1)
    apointmentsArray = list(map(
        lambda apointment: (f'{apointment["day"]}',f'{apointment["typeOfService"]}', f'{apointment["time"]}', f'{apointment["beggining"]}', f'{apointment["finish"]}',f'{apointment["_id"]}') ,apointmentsArray))
    return apointmentsArray

def deleteApointment(day,id_number):
    
    deleteApointmentData(day,id_number)


def editApointment(top_level,item_props,service,time,beggining):
    day = item_props["values"][0]
    id_number = item_props["values"][-1]
    finish = SumHours(time,beggining)
    data = Apointment(day,service,time,beggining,finish)
    editApointmentData(day,data,id_number)
    top_level.destroy()