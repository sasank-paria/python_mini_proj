import json

import requests

url = "https://pincode.p.rapidapi.com/"

payload = {
	"searchBy": "pincode",
	"value": f"{pincode}"
}
headers = {
	"content-type": "application/json",
	"Content-Type": "application/json",
	"X-RapidAPI-Host": "pincode.p.rapidapi.com",
	"X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
}

response = requests.request("POST", url, json=payload, headers=headers)

response1=response.json()

with open("pincode_info.json",'w') as file:
	json.dump(response1,file)

pin=response1[0]['pin']
region=response1[0]['region']
taluka=response1[0]['taluk']
district=response1[0]['district']
state=response1[0]['circle']
