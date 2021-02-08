import requests
class IRCTC:
    def __init__(self):
        train_no= input("Enter train number: ")
        self.fetch_data(train_no)

    def fetch_data(self,train_no):
        data = requests.get(
            "http://indianrailapi.com/api/v2/TrainSchedule/apikey/329a6c020de530e4f5d7c04a7f0b358b/TrainNumber/{}".format(train_no))

        data = data.json()
        self.display_results(data)
    def display_results(self,data):
        for i in data['Route']:
            print(i['StationName'],"|",i['ArrivalTime'],"|",i['DepartureTime'],"|",i['Distance'],"KM")

obj1 = IRCTC()