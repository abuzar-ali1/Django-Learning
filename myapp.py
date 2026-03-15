import requests 
import json

# # URL = "http://127.0.0.1:8000/stucreate/"

# # data = {
# #     'name' : 'Younis Ali',
# #     'roll' : 3478,
# #     'city' : 'karachi'
# # }



# # json_data = json.dumps(data)

# # r = requests.post(url = URL , data = json_data)



# # data = r.json()

# # print(data)



URL_2 = "http://127.0.0.1:8000/studentapi/"


# def get_data(id = None):
#     data = {}
#     if id is not None:
#         data = {'id' : id}
#     json_data = json.dumps(data)
#     r = requests.get(url = URL_2 , data = json_data)
#     data = r.json()
#     print(data) 



# get_data(3)    


def update_data():
    data = {
        'id' : 3,
        'name' : 'Rahman Ali',
        'roll' : 1234,
        'city' : 'KPK',
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL_2 , data = json_data)
    data = r.json()
    print(data)    



update_data()