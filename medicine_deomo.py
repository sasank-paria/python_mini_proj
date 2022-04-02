import requests
import json
#query=self.search_midicine_textbar.text()
url = f"https://google-search3.p.rapidapi.com/api/v1/search/q= +buy online +netmeds+pharmeasy+1mg"

headers = {
	"X-User-Agent": "desktop",
	"X-Proxy-Location": "EU",
	"X-RapidAPI-Host": "google-search3.p.rapidapi.com",
	"X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
}

response = requests.request("GET", url, headers=headers)

response1=response.json()

with open("news.json", "w") as outfile:
    json.dump(response1, outfile)



label1_1=response1['results'][0]["title"]
label1_2=response1['results'][0]["link"]
label1_3=response1['results'][0]["description"]

label2_1=response1['results'][1]["title"]
label2_2=response1['results'][1]["link"]
label2_3=response1['results'][1]["description"]

label3_1=response1['results'][2]["title"]
label3_2=response1['results'][2]["link"]
label3_3=response1['results'][2]["description"]

label4_1=response1['results'][3]["title"]
label4_2=response1['results'][3]["link"]
label4_3=response1['results'][3]["description"]

label5_1=response1['results'][4]["title"]
label5_2=response1['results'][4]["link"]
label5_3=response1['results'][4]["description"]

label6_1=response1['results'][5]["title"]
label6_2=response1['results'][5]["link"]
label6_3=response1['results'][5]["description"]

label7_1=response1['results'][6]["title"]
label7_2=response1['results'][6]["link"]
label7_3=response1['results'][6]["description"]

label8_1=response1['results'][7]["title"]
label8_2=response1['results'][7]["link"]
label8_3=response1['results'][7]["description"]

print(label1_2)
