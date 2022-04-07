#ho gya
import requests
import json
url = "https://bing-news-search1.p.rapidapi.com/news"

querystring = {"count":"12","category":"Health","mkt":"en-GB","safeSearch":"Off","textFormat":"Raw"}

headers = {
	"X-BingApis-SDK": "true",
	"X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com",
	"X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
}

response = requests.request("GET", url, headers=headers, params=querystring)

response1=response.json()

# with open("news.json","w") as file:
# 	json.dump(response1,file)

#print(response1)



p2=response1['value'][0]['name']
p3=response1['value'][0]['url']

p4=response1['value'][1]['name']
p5=response1['value'][1]['url']

p6=response1['value'][2]['name']
p7=response1['value'][2]['url']

p8=response1['value'][3]['name']
p9=response1['value'][3]['url']

p10=response1['value'][4]['name']
p11=response1['value'][4]['url']

p12=response1['value'][5]['name']
p13=response1['value'][5]['url']

p14=response1['value'][6]['name']
p15=response1['value'][6]['url']

p16=response1['value'][7]['name']
p17=response1['value'][7]['url']

p18=response1['value'][8]['name']
p19=response1['value'][8]['url']

p20=response1['value'][9]['name']
p21=response1['value'][9]['url']

p22=response1['value'][10]['name']
p23=response1['value'][10]['url']

p24=response1['value'][11]['name']
p25=response1['value'][11]['url']

# p26=response1['value'][12]['name']
# p27=response1['value'][12]['url']
#
# p28=response1['value'][13]['name']
# p29=response1['value'][13]['url']
#
# p30=response1['value'][14]['name']
# p31=response1['value'][14]['url']

