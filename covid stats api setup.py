import json

import requests

url = "https://covid-193.p.rapidapi.com/statistics"

querystring = {"country":"India"}

headers = {
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com",
	"X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
}

response = requests.request("GET", url, headers=headers, params=querystring)

response1=response.json()

with open("coviddata.json","w") as file:
    json.dump(response1,file)

p1=response1['response'][0]['country']
p2=response1['response'][0]['population']
p3=response1['response'][0]['cases']['active']
p4=response1['response'][0]['cases']['critical']
p5=response1['response'][0]['cases']['recovered']
p6=response1['response'][0]['cases']['total']
p7=response1['response'][0]['deaths']['total']
p8=response1['response'][0]['day']
p9=response1['response'][0]['time']

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
