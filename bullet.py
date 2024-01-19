import sys
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from nltk.tokenize import sent_tokenize

text = text = sys.argv[1]
sentences = sent_tokenize(text)

parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer_luhn = LuhnSummarizer()

summary = summarizer_luhn(parser.document, int(sentences.__len__()/3))


dp = []
for i in summary:
	lp = str(i)
	dp.append(lp)

final_sentence = ""
for d in dp:
	final_sentence += "\u2022 "+d+"\n"


print(final_sentence.encode(encoding="utf-8").hex())