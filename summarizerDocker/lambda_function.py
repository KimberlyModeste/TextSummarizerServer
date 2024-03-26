import json
import nltk

nltk.download('punkt', download_dir='/tmp/')
nltk.download('stopwords', download_dir='/tmp/')

from collections import Counter 
from nltk.corpus import stopwords
from transformers import pipeline
from nltk.tokenize import sent_tokenize, word_tokenize


def lambda_handler(event, context):
	test = json.loads(event['body'])
	text = test['text']
	length = test['length']
	
	sentences = sent_tokenize(text)

	if(len(sentences) >= 30):
		n = 25
		stop_words = set(stopwords.words('english'))

		words = [word.lower() for word in word_tokenize(text) if word.lower() not in stop_words and word.isalnum()]
		word_freq = Counter(words)

		sentence_scores = {}

		for sentence in sentences:
			sentence_words = [word.lower() for word in word_tokenize(sentence) if word.lower() not in stop_words and word.isalnum()]
			sentence_score = sum([word_freq[word] for word in sentence_words])
			if len(sentence_words) < 20:
				sentence_scores[sentence] = sentence_score

		summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n]
		text = ' '.join(summary_sentences)

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
			sum_list = summarizer(text, max_length=int(sum_vals[1][1]), min_length=int(sum_vals[1][0]), do_sample=False, truncation=True)
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