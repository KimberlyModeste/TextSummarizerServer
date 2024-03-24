import json
import math
import nltk

nltk.download('punkt', download_dir='/tmp/')

from sumy.summarizers.luhn import LuhnSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from nltk.tokenize import sent_tokenize

def lambda_handler(event, context):
    test = json.loads(event['body'])
    text = test['text']

    sentences = sent_tokenize(text)
    
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    summarizer_luhn = LuhnSummarizer()
    
    summary = summarizer_luhn(parser.document, int(math.ceil(sentences.__len__()/3)))

    document_parser = []
    for i in summary:
        line_parser = str(i)
        document_parser.append(line_parser)

    final_sentence = ""
    for document in document_parser:
        final_sentence += "\u2022 "+document+"\n"
    
    return { 'summary' : final_sentence}
    # return { 'summary' : 'returned'}