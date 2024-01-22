from transformers import pipeline
import sys


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
text = sys.argv[1]
min = sys.argv[2]
max = sys.argv[3]

sum_list = summarizer(text, max_length=int(max), min_length=int(min), do_sample=False)
summary = sum_list[0].get("summary_text")

print(summary.encode(encoding="utf-8").hex())