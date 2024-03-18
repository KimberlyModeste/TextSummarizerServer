import math
import nltk
# nltk.download('punkt')

from sumy.summarizers.luhn import LuhnSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from nltk.tokenize import sent_tokenize

def bullet(text):

	# Tokenize the sentences
	# I used to determine how many sentences there are
	sentences = sent_tokenize(text)

	# Create a parser based on the text
	parser = PlaintextParser.from_string(text, Tokenizer("english"))

	# Create a Luhn Summarizer var
	summarizer_luhn = LuhnSummarizer()

	# Use the Luhn summarizer to summarize the the document created by the parser
	# and how long we want our summarized document to be being a 3rd of its origial length to the ceiling
	summary = summarizer_luhn(parser.document, int(math.ceil(sentences.__len__()/3)))

	# Changing the returned values to strings because they are of class sumy.models.dom
	document_parser = []
	for i in summary:
		line_parser = str(i)
		document_parser.append(line_parser)

	# Setting up the sentences to have a bullet point before them and be on a seperate line
	final_sentence = ""
	for document in document_parser:
		final_sentence += "\u2022 "+document+"\n"

	return final_sentence
