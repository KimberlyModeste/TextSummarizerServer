from transformers import pipeline

def summarizer(text, min, max):
	# Retrieve the bart summarization model
	summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

	# Input those variables into the summarizer
	sum_list = summarizer(text, max_length=int(max), min_length=int(min), do_sample=False)

	# Seperate the text out from its dictionary
	summary = sum_list[0].get("summary_text")
	print(summary)

	# Sending back sentence
	return summary
