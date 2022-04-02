import json

import requests

url = "https://trueway-places.p.rapidapi.com/FindPlacesNearby"

querystring = {"location":"19.076090,72.877426","type":"hospital","radius":"9000","language":"en"}

headers = {
	"X-RapidAPI-Host": "trueway-places.p.rapidapi.com",
	"X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
}

response = requests.request("GET", url, headers=headers, params=querystring)

response1=response.json()

with open("hospital.json","w") as file :
    json.dump(response1,file)


l1_1=response1['results'][0]['name']
l1_2=response1['results'][0]['address']
l1_3=response1['results'][0]['phone_number']
l1_4=response1['results'][0]['distance']

l2_1=response1['results'][1]['name']
l2_2=response1['results'][1]['address']
l1_3=response1['results'][1]['phone_number']
l1_4=response1['results'][1]['distance']

l1_1=response1['results'][2]['name']
l1_2=response1['results'][2]['address']
l1_3=response1['results'][2]['phone_number']
l1_4=response1['results'][2]['distance']

l1_1=response1['results'][3]['name']
l1_2=response1['results'][3]['address']
l1_3=response1['results'][3]['phone_number']
l1_4=response1['results'][3]['distance']

l1_1=response1['results'][4]['name']
l1_2=response1['results'][4]['address']
l1_3=response1['results'][4]['phone_number']
l1_4=response1['results'][4]['distance']

l1_1=response1['results'][5]['name']
l1_2=response1['results'][5]['address']
l1_3=response1['results'][5]['phone_number']
l1_4=response1['results'][5]['distance']

l1_1=response1['results'][6]['name']
l1_2=response1['results'][6]['address']
l1_3=response1['results'][6]['phone_number']
l1_4=response1['results'][6]['distance']

l1_1=response1['results'][7]['name']
l1_2=response1['results'][7]['address']
l1_3=response1['results'][7]['phone_number']
l1_4=response1['results'][7]['distance']

l1_1=response1['results'][8]['name']
l1_2=response1['results'][8]['address']
l1_3=response1['results'][8]['phone_number']
l1_4=response1['results'][8]['distance']

l1_1=response1['results'][9]['name']
l1_2=response1['results'][9]['address']
l1_3=response1['results'][9]['phone_number']
l1_4=response1['results'][9]['distance']


l1_1=response1['results'][10]['name']
l1_2=response1['results'][10]['address']
l1_3=response1['results'][10]['phone_number']
l1_4=response1['results'][10]['distance']


l1_1=response1['results'][11]['name']
l1_2=response1['results'][11]['address']
l1_3=response1['results'][11]['phone_number']
l1_4=response1['results'][11]['distance']
