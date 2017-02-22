import json
import requests
import numpy as np

_url = 'https://westus.api.cognitive.microsoft.com/vision/v1.0/analyze'
_key = '5261f96d07fc460ab78dc7b0f643b4f1'

def description(filename):
	with open(filename,'rb') as f:
		data = f.read()

	params = {
		'visualFeatures': 'Description'
	}
	headers = dict()
	headers['Ocp-Apim-Subscription-Key'] = _key
	headers['Content-Type'] = 'application/octet-stream'

	response = requests.request('post',_url,data=data,headers=headers,params=params)

	return response.json()['description']['captions'][0]['text']
#print response.json()['description']['tags']