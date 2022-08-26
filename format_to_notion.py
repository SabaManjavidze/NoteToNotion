

import json
from db_schema import CheckBoxType, DateType, NumberType, Schema, TitleType


def format_to_notion(pushUps,start,end,didCount):
    total_num=0
    for pushup in pushUps.split(","):
        total_num+=int(pushup)
    date = DateType(start,end)
    pushUpsArr = TitleType(pushUps)
    total_num_prop=NumberType(total_num)
    did_count_prop=CheckBoxType(didCount)
    formated = Schema(
        date=date,
        didCount=did_count_prop,
        pushUps=pushUpsArr,
        totalPushups=total_num_prop
    )
    return formated.values()
