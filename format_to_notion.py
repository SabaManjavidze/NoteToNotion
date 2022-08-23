

def format_to_notion(pushUps,start,end,didCount):
    formated = {
               "Push Ups":{
                   "type":"title",
                   "title": [{
                       "type": "text",
                       "text": {"content": pushUps},
                   }],
               },
               "Date":{
                   "type":"date",
                   "date":{
                       "start":start,
                       "end":end
                   }
               },
               "Did Count":{
                   "type":"checkbox",
                   "checkbox":didCount,
               },
        }
    total_push_ups={
            "type":"number"
        }
    total_num=0
    for pushup in pushUps.split(","):
        total_num+=int(pushup)
    total_push_ups["number"]=total_num
    formated["Total Push Ups"]=total_push_ups
    return formated