import requests 
import json

# # URL = "http://127.0.0.1:8000/stucreate/"

# data = {
#     'name' : 'Younis Ali',
#     'roll' : 3478,
#     'city' : 'karachi'
# }



# json_data = json.dumps(data)

# r = requests.post(url = URL , data = json_data)



# data = r.json()

# print(data)


URL = 'http://127.0.0.1:8000/todo/'
def add_data():
    data = {
    'title' : 'Studying',
    'desc' : 'sssssssssssssssssssssssssssszzo please do some thing best ',
    'is_done' : True,
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL ,  data= json_data)
    data = r.json()
    print(data)



# add_data()

URL_2 = "http://127.0.0.1:8000/studentapi/"


def get_data(id):
    # data = {}
    # if id is not None:
    data = {'id' : id}
    json_data = json.dumps(data)
    r = requests.get(url = URL , data = json_data)
    data = r.json()
    print(data) 



# get_data(3)    


def update_data():
    data = {
        'id' : 3,
        'title' : 'Rahman Ali',
        'is_done' : True
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL , data = json_data)
    data = r.json()
    print(data)    



update_data()



def delete_data():
    data = { 'id' : 3 }
    json_data = json.dumps(data)
    r = requests.delete(url = URL_2 , data = json_data)
    data = r.json()
    print(data)    



# delete_data()