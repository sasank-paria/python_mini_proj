import json

import requests

url = "https://google-news.p.rapidapi.com/v1/topic_headlines"

querystring = {"lang":"en","country":"INDIA","topic":"HEALTH"}

headers = {
	"X-RapidAPI-Host": "google-news.p.rapidapi.com",
	"X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
}

response = requests.request("GET", url, headers=headers, params=querystring)

response1=response.json()

with open("news.json","w") as file:
	json.dump(response1,file)

p1=response1['feed']['updated']

p2=response1['articles'][0]['title']
p3=response1['articles'][0]['link']

p4=response1['articles'][1]['title']
p5=response1['articles'][1]['link']

p6=response1['articles'][2]['title']
p7=response1['articles'][2]['link']

p8=response1['articles'][3]['title']
p9=response1['articles'][3]['link']

p10=response1['articles'][4]['title']
p11=response1['articles'][4]['link']

p12=response1['articles'][5]['title']
p13=response1['articles'][5]['link']

p14=response1['articles'][6]['title']
p15=response1['articles'][6]['link']

p16=response1['articles'][7]['title']
p17=response1['articles'][7]['link']

p18=response1['articles'][8]['title']
p19=response1['articles'][8]['link']

p20=response1['articles'][9]['title']
p21=response1['articles'][9]['link']

p22=response1['articles'][10]['title']
p23=response1['articles'][10]['link']

p24=response1['articles'][11]['title']
p25=response1['articles'][11]['link']

p26=response1['articles'][12]['title']
p27=response1['articles'][12]['link']

p28=response1['articles'][13]['title']
p29=response1['articles'][13]['link']

p30=response1['articles'][14]['title']
p31=response1['articles'][14]['link']


print(p30)
print(p31)