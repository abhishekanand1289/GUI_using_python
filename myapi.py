import requests

class Api:
	def __init__(self):
		self.url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

	def sent_analysis(self,text):
		querystring = {"text": text}

		headers = {
			"x-rapidapi-key": "0a8452d372msh486db09e2873768p141df1jsnc09784a911a5",
			"x-rapidapi-host": "twinword-sentiment-analysis.p.rapidapi.com"
		}

		response = requests.get(self.url, headers=headers, params=querystring)
		return response