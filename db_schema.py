from datetime import date


class PropertyType():
    def __init__(self,value):
        self.property={
                "type":value.name,
                value.name:value.values()
        }
class CheckBoxType:
    def __init__(self,value:bool):
        self.name="checkbox"
        self.value=value
    def values(self):
        return self.value

class NumberType:
    def __init__(self,number:int):
        self.name="number"
        self.number=number
    def values(self):
        return self.number

class TitleType:
    def __init__(self,text:str):
        self.name="title"
        self.text=text
    def values(self):
        return [PropertyType(TextType(self.text)).property]

class TextType:
    def __init__(self,text:str):
        self.name="text"
        self.text=text
    def values(self):
        return {"content":str(self.text)}

class DateType:
    def __init__(self,start:date,end:date):
        self.name="date"
        self.start=start
        self.end=end
    def values(self):
        return {"start":self.start,"end":self.end}
class Schema:
        def __init__(self,date:DateType,didCount:CheckBoxType,
        pushUps:TitleType,totalPushups:NumberType):
            self.date=PropertyType(date)
            self.didCount=PropertyType(didCount)
            self.pushUps=PropertyType(pushUps)
            self.totalPushups=PropertyType(totalPushups)
        def values(self):
            return {
                "Date":self.date.property,
                "Did Count":self.didCount.property,
                "Push Ups":self.pushUps.property,
                "Total Push Ups":self.totalPushups.property,
            }
    