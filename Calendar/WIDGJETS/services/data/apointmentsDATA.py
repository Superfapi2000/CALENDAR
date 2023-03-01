from WIDGJETS.services.data.auxFunctions.auxFunctions import checkIfItFitsSchedule,mergeSort as MSort
from WIDGJETS.services.data.mongoDBstorage import updateMongoDBStorage
from WIDGJETS.services.data.mongoDBstorage import getMongoData_ApointmentsDay, getMongoData_ApointmentsDays,deleteApointmentMongoData,editApointmentMongoData
apointmentsData = {}

def addApointmentToData(apointment):
    print("here",apointment.day)
    apointmentsDays = getMongoData_ApointmentsDays()
    if apointment.day not in apointmentsDays:
                print("###")
                updateMongoDBStorage(apointment.day,apointment)


    else:
        apointmentsArray = []
        apointmentsData = getMongoData_ApointmentsDay(apointment.day)
        for document in apointmentsData:
            apointmentsArray += [document]
        MSort(apointmentsArray,0,len(apointmentsArray)-1)
        #reduceTheArray By Type and By beginning Time being higher than the finish
        #put in a fuction To Optimize Data
        if(checkIfItFitsSchedule(apointmentsArray,apointment.day,apointment.beggining,apointment.finish)):
            print("###$$")
            updateMongoDBStorage(apointment.day,apointment)
        else:
            print("error adding your time")

def getDayData(day):

    return getMongoData_ApointmentsDay(day)

def deleteApointmentData(day,objectID):
    deleteApointmentMongoData(day,objectID)
    
def editApointmentData(day,data,id_number):
    editApointmentMongoData(day,data,id_number)

