import json

from transformers import pipeline


def lambda_handler(event, context):
	test = json.loads(event['body'])
	text = test['text']
	length = test['length']
	
	wordCounter = len(text.split(" "))
	sum_vals = {
		1 : [30, 130], 
		2 : [100, 300],
		3 : [150, 400],
		4 : [200, 500]
	}
	
	summary = ''
	
	summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
	
	if length == 1:
		if wordCounter >= sum_vals[1][0]:
			sum_list = summarizer(text, max_length=int(sum_vals[1][1]), min_length=int(sum_vals[1][0]), do_sample=False)
		else:
			return { 'summary': "This sentence is too short to summarize."}

	elif wordCounter >= sum_vals[length][0]:
		sum_list = summarizer(text, max_length=int(sum_vals[length][1]), min_length=int(sum_vals[length][0]), do_sample=False)

	else:
		sum_list = summarizer(text, max_length=int(sum_vals[length-1][1]), min_length=int(sum_vals[length-1][0]), do_sample=False)

	# Seperate the text out from its dictionary
	summary = sum_list[0].get("summary_text")

	# Sending back sentence
	return {'summary': summary}