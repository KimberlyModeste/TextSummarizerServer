from transformers import pipeline
import sys

# Retrieve the bart summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Get the text, minimum and maximum based on test's I've done ahead of time
text = sys.argv[1]
min = sys.argv[2]
max = sys.argv[3]

# Input those variables into the summarizer
sum_list = summarizer(text, max_length=int(max), min_length=int(min), do_sample=False)

# Seperate the text out from its dictionary
summary = sum_list[0].get("summary_text")

# Sending back sentence as a hex so no information is lost.
print(summary.encode(encoding="utf-8").hex())