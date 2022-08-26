from datetime import datetime
from format_to_notion import format_to_notion

def convert_to_iso(year,month,day,time):
    initial_format="%Y-%d-%b:%H:%M"
    converted =datetime.strptime(f'{year}-{day}-{month}:{time}',initial_format).isoformat()
    return converted

def format_pushups():
    file = open("./private/note.txt","r")
    textLines=file.readlines()
    formated_arr=[]
    year=""
    for i,line in enumerate(textLines):
        day=""
        month=""
        startTime=""
        endTime=""
        totalPushups=0
        didCount=True
        if(line.startswith("year")==False):
            split_line=line.split(" - ")
            dayNmonth=split_line[0]
            timeNcount=split_line[1]  # 60,20  time: 1:45-2:04  didn't count\n

            dayNmonthSplit=dayNmonth.split(" ")
            day=dayNmonthSplit[0]
            month=dayNmonthSplit[1]

            if(str("didn't count") in str(timeNcount)):
                didCount=False
                timeNcount.strip("\n")
                
            timeOnlySplit=timeNcount.split("time: ")
            pushups = timeOnlySplit[0].split(",")
            
            for pushup in pushups:
                totalPushups+=int(pushup)
                
            timeStampSplit=timeOnlySplit[1].split("-")
            startTime=timeStampSplit[0]
            if(didCount==True):
                endTime=timeStampSplit[1].strip("\n")
            else:
                endTime=timeStampSplit[1].split(" ")[0].strip("\n")

            start = convert_to_iso(year,month,day,startTime)
            end = convert_to_iso(year,month,day,endTime)

            formated_item = format_to_notion(timeOnlySplit[0],start,end,didCount)
            formated_arr.append(formated_item)
        else:
           year=line.split("year: ")[1].strip("\n--")
    file.close()
    return formated_arr