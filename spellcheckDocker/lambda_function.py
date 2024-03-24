import json
import nltk

nltk.download('punkt', download_dir='/tmp/')

from symspellpy import SymSpell, Verbosity
from nltk.tokenize import sent_tokenize

import pkg_resources

def lambda_handler(event, context):
	test = json.loads(event['body'])
	text = test['text']

	#Tokenizing it into sentences make it easier to keep all the punctuation 
	text_arr = sent_tokenize(text)

	#Get SymSpell running
	sym_spell = SymSpell()

	#Open the Symspell dictionary
	dictionary_path = pkg_resources.resource_filename(
		"symspellpy", "frequency_dictionary_en_82_765.txt"
	)

	#Load symspell dictionary 
	sym_spell.load_dictionary(dictionary_path, 0, 1)

	new_string = ''
	# Splitting the words individually and looking them up the taking the top 
	# result and adding it to the new sentence. Sometimes the transfer casing doesnt work
	# So I made sure to capitalize the word anyway. Then if the word has a punctuation
	# attached to it, re-add it.
	for sentence in text_arr:
		for word in sentence.split(' '):
			temp=sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2, include_unknown=True, transfer_casing=True)[0].term
			if not word.islower():
				new_string+=temp.capitalize()+' '
			else:
				new_string+=temp+' '

			if not word[word.__len__()-1].isalpha():
				new_string= new_string[:-1]+word[word.__len__()-1]+' '

	# Deleting last character which is a space
	new_string = new_string[:-1]

	return { 'summary' : new_string }

