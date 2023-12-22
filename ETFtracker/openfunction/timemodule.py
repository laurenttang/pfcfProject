from datetime import datetime

#dateString = "Monday, May 13, 2020 20:01:56"
#dateFormatter = "%A, %B %d, %Y %H:%M:%S"
def Str_to_time(dateString,dateFormatter):
    #dateString = "20230912 11:50:23"
    #dateFormatter = "%Y%m%d %H:%M:%S"
    return datetime.strptime(dateString, dateFormatter)