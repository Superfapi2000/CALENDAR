# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
import datetime
def compareTimes(date1,date2,symbol = ""):
	now = datetime.datetime.now()
	now2= datetime.datetime.now()
	date1 = getMinutesAndHoursInArray(date1)
	date1 = now.replace(hour=date1[0], minute=date1[1], second=0, microsecond=0)
	date2 = getMinutesAndHoursInArray(date2)
	date2 = now.replace(hour=date2[0], minute=date2[1], second=0, microsecond=0)
	if(symbol == ("<")):
		return date1 > date2
	if(symbol ==(">")):
		return date1 < date2
	else:
		return date1 <= date2
def getMinutesAndHoursInArray(time):
    minutes_hours = time.split(":")
    minutes_hours = list(map(int,minutes_hours))
    return minutes_hours

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if compareTimes(L[i]["beggining"],(R[j]["beggining"])):
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


# Driver code to test above

# This code is contributed by Mohit Kumra

def inBetweenTimes(hoursTest, hours1, hours2):
    if compareTimes(hoursTest,hours2,">"):
        if compareTimes(hoursTest,hours1,"<") :
            return True
    return False


def getMinutesAndHoursInArray(time):
    minutes_hours = time.split(":")
    minutes_hours = list(map(int,minutes_hours))
    return minutes_hours


def getRealTime():
    today = datetime.date.today()
    Day = {"Day":today.day,"Month":today.month, "Year":today.year}
    return Day

def checkIfItFitsSchedule(apointmentsData,date,newApointmentBegginingTime, newApointmentFinishingTime):
	flag = True
	for x in apointmentsData:
		beginingApointemtsTestHours = x["beggining"]
		finishingApointemtsTestHours = x["finish"]
		if(inBetweenTimes(newApointmentBegginingTime,beginingApointemtsTestHours,finishingApointemtsTestHours)):
			flag = False
		elif(inBetweenTimes(newApointmentFinishingTime,beginingApointemtsTestHours,finishingApointemtsTestHours)):
			flag = False
		if(newApointmentBegginingTime ==beginingApointemtsTestHours and newApointmentFinishingTime == finishingApointemtsTestHours):
			flag = False
	return flag
def getDayMonthYearWellFormated(dayString):
	date_obj = datetime.datetime.strptime(dayString, "%m/%d/%y")
	formatted_date = date_obj.strftime("%d-%m-%Y")
	dayformat = formatted_date.split("-")
	dayTrueFormat = str(int(dayformat[0])) + "-" + str(int(dayformat[1])) + "-" + str(dayformat[2])
	return dayTrueFormat
	
def SumHours(time,beggining):
    hours_MiutesTime = getMinutesAndHoursInArray(time)
    beggining = getMinutesAndHoursInArray(beggining)
    s = datetime.timedelta(minutes=hours_MiutesTime[1],hours=hours_MiutesTime[0])  + datetime.timedelta(hours=beggining[0], minutes=beggining[1])
    s = str(s)[:-3]# tirar os segundos e os dois pontos
    return s
def insertCustom(fields,day = ""):
    ##stinks
    if ("Day" == fields):
        if(day == ""):
            dayNULL = getRealTime()
            day = str(dayNULL["Day"])
        return getDayMonthYearWellFormated(day) 
    if(fields =="Time" or fields =="Beggining" ):
        return"hh:mm"
    else:
        return "massage"

