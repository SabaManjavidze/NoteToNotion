from datetime import datetime

def print_time():
    push_date="2022-19-aug:1:45"
    push_format="%Y-%d-%b:%H:%M"
    formated=datetime.strptime(push_date,push_format)
    print(formated.isoformat())