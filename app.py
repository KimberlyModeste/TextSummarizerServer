from flask import Flask, request
from flask_cors import CORS, cross_origin

import pyAPI.bullet 
import pyAPI.summarizer
import pyAPI.spellchecker

app = Flask('__name__')

# Added cors stuff
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Does all summary stuff
@app.route("/summary", methods=['POST', 'GET'])
@cross_origin()
def summary():
	data = request.get_json()
	wordCounter = len(data['text'].split(" "))
	sum_vals = {
		1 : [30, 130], 
		2 : [100, 300],
		3 : [150, 400],
		4 : [200, 500]
	}
	length = data['length']

	result = ""
	if length == 0:
		result = pyAPI.bullet.bullet(data['text'])
	else:
		if length == 1:
			if wordCounter >= sum_vals[1][0]:
				result = pyAPI.summarizer.summarizer(data['text'], sum_vals[1][0], sum_vals[1][1])
			else:
				result = "This sentence is too short to summarize."
				print("This sentence is too short to summarize.")

		elif wordCounter >= sum_vals[length][0]:
			result = pyAPI.summarizer.summarizer(data['text'], sum_vals[length][0], sum_vals[length][1])

		else:
			result = pyAPI.summarizer.summarizer(data['text'], sum_vals[length-1][0], sum_vals[length-1][1])

	return {'summary': result}

#Does all the spellchecking
@app.route("/spellcheck", methods=['POST', 'GET'])
@cross_origin()
def spellcheck():
	data = request.get_json()

	result = pyAPI.spellchecker.spellcheck(data['text'])

	return {'summary' : result}


if __name__ == "__main__":
	app.run(debug=True)
