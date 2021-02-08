import requests
class Status:
    def __init__(self):
        station_code=input("Enter station code in capital: ")

        self.fetch_data(station_code)
    def fetch_data(self,station_code):
        data = requests.get("http://indianrailapi.com/api/v2/LiveStation/apikey/329a6c020de530e4f5d7c04a7f0b358b/StationCode/{}/hours/4/".format(station_code))
        data=data.json()
        self.display_result(data)
    def display_result(self,data):
        for i in data['Trains']:
            print(i['Number'],"|",i['Name'],"|",i['ScheduleArrival'],"|",i['ScheduleDeparture'],"|",i['ExpectedArrival'],"|",i['ExpectedDeparture'],"|",i['Delay'],"Hrs")

obj2 = Status()


