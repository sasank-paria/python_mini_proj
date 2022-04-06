import json

import pandas
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

print(response1)
p1=response1['response'][0]['country']
p2=response1['response'][0]['population']
p3=response1['response'][0]['cases']['active']
p4=response1['response'][0]['cases']['critical']
p5=response1['response'][0]['cases']['recovered']
p6=response1['response'][0]['cases']['total']
p7=response1['response'][0]['deaths']['total']
p8=response1['response'][0]['day']
p9=response1['response'][0]['time']

# self.l1.setText(p1)
# self.l2.setText(p2)
# self.l3.setText(p3)
# self.l4.setText(p4)
# self.l5.setText(p5)
# self.l6.setText(p6)
# self.l7.setText(p7)
# self.l8.setText(p8)
# self.l9.setText(p9)

data=pandas.Series(response1)
print(data)

import matplotlib.pyplot as plt
import numpy as np

y = np.array([p7, p5, p4, p3])
mylabels = ["deaths", "recovered", "critical", "active"]

plt.pie(y, labels = mylabels)

plt.show()



x = np.array(["deaths", "recovered", "critical", "active"])
y = np.array([p7, p5, p4, p3])

plt.bar(x,y)
plt.show()